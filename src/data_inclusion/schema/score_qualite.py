from typing import Callable, Mapping

import pendulum

from data_inclusion.schema import (
    ModeAccueil,
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
    Service,
)


def adresse_bien_definie(service: Service) -> float | None:
    critere_applicable = (
        service.modes_accueil and ModeAccueil.EN_PRESENTIEL in service.modes_accueil
    ) or (
        service.modes_orientation_beneficiaire
        and ModeOrientationBeneficiaire.SE_PRESENTER
        in service.modes_orientation_beneficiaire
    )

    if critere_applicable:
        return 1.0 if service.adresse else 0.0

    return None


def telephone_bien_defini(service: Service) -> float | None:
    critere_applicable = (
        service.modes_orientation_accompagnateur
        and ModeOrientationAccompagnateur.TELEPHONER
        in service.modes_orientation_accompagnateur
    ) or (
        service.modes_orientation_beneficiaire
        and ModeOrientationBeneficiaire.TELEPHONER
        in service.modes_orientation_beneficiaire
    )

    if critere_applicable:
        return 1.0 if service.telephone else 0.0

    return None


def courriel_bien_defini(service: Service) -> float | None:
    critere_applicable = (
        service.modes_orientation_accompagnateur
        and ModeOrientationAccompagnateur.ENVOYER_UN_MAIL
        in service.modes_orientation_accompagnateur
    ) or (
        service.modes_orientation_beneficiaire
        and ModeOrientationBeneficiaire.ENVOYER_UN_MAIL
        in service.modes_orientation_beneficiaire
    )

    if critere_applicable:
        return 1.0 if service.courriel else 0.0

    return None


def au_moins_un_mode_orientation(service: Service) -> float:
    return (
        1.0
        if service.modes_orientation_accompagnateur
        or service.modes_orientation_beneficiaire
        else 0.0
    )


def date_maj_recente(service: Service) -> float:
    SIX_MONTHS = pendulum.duration(months=6)
    TWO_YEARS = pendulum.duration(years=2)

    if service.date_maj is None:
        return 0.0

    age = pendulum.instance(service.date_maj).diff(pendulum.now())

    if age < SIX_MONTHS:
        return 1.0
    elif SIX_MONTHS < age < TWO_YEARS:
        return (TWO_YEARS - age) / (TWO_YEARS - SIX_MONTHS)
    else:
        return 0.0


def au_moins_une_thematique(service: Service) -> float:
    return 1.0 if service.thematiques else 0.0


def au_moins_un_profil(service: Service) -> float:
    return 1.0 if service.profils else 0.0


def coordonnees_de_contact_bien_definies(service: Service) -> float:
    return (
        1.0
        if service.telephone or service.courriel or service.adresse or service.prise_rdv
        else 0.0
    )


def presentation_bien_definie(service: Service) -> float:
    return 1.0 if service.presentation_resume or service.presentation_detail else 0.0


# Les critères sont implémentés sous forme de fonctions qui prennent un service en
# entrée et renvoient un score entre 0 et 1.
# Dans le cas où le critère n'est pas applicable, une fonction peut renvoyer None.
# Par exemple, le critère "adresse_bien_definie" ne s'applique que si le service propose
# un mode d'accueil en présentiel ou une orientation bénéficiaire en présentiel.
CritereFn = Callable[[Service], float | None]

CRITERES: list[CritereFn] = [
    adresse_bien_definie,
    au_moins_un_mode_orientation,
    au_moins_un_profil,
    au_moins_une_thematique,
    coordonnees_de_contact_bien_definies,
    courriel_bien_defini,
    date_maj_recente,
    presentation_bien_definie,
    telephone_bien_defini,
]


def score(service: Service) -> tuple[float, Mapping[str, float | None]]:
    resultats = {critere.__name__: critere(service) for critere in CRITERES}

    resultats_pertinents = {k: v for k, v in resultats.items() if v is not None}
    score = sum([v for v in resultats_pertinents.values()]) / len(resultats_pertinents)

    return score, resultats
