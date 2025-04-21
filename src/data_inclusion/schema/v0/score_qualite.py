from typing import Callable, Mapping

import pendulum

from .frais import Frais
from .modes_accueil import ModeAccueil
from .modes_orientation import (
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
)
from .services import Service


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


def date_maj_recente(service: Service) -> float | None:
    SIX_MOIS = pendulum.duration(months=6)
    DEUX_ANS = pendulum.duration(years=2)

    if service.source in ["agefiph", "france-travail"]:
        return None

    if service.date_maj is None:
        return 0.0

    age = pendulum.instance(service.date_maj).diff(pendulum.now())

    if age < SIX_MOIS:
        return 1.0
    elif SIX_MOIS < age < DEUX_ANS:
        # simple interpolation linéaire entre 0 et 1
        return (DEUX_ANS - age) / (DEUX_ANS - SIX_MOIS)
    else:
        return 0.0


def au_moins_une_thematique(service: Service) -> float:
    return 1.0 if service.thematiques else 0.0


def au_moins_un_public(service: Service) -> float:
    return 1.0 if service.profils else 0.0


def au_moins_un_frais(service: Service) -> float:
    return 1.0 if service.frais else 0.0


def au_moins_un_moyen_de_contact(service: Service) -> float:
    return (
        1.0
        if any(
            (
                service.courriel,
                service.formulaire_en_ligne,
                service.page_web,
                service.prise_rdv,
                service.telephone,
            )
        )
        else 0.0
    )


def description_bien_definie(service: Service) -> float:
    SEUIL_MINIMUM = 200
    SEUIL_BON = 400

    longueur_presentation = 0

    if service.presentation_resume:
        longueur_presentation = len(service.presentation_resume)

    if service.presentation_detail:
        longueur_presentation += len(service.presentation_detail)

    if longueur_presentation < SEUIL_MINIMUM:
        return 0.0
    elif longueur_presentation < SEUIL_BON:
        # simple interpolation linéaire entre 0 et 1
        return (longueur_presentation - SEUIL_MINIMUM) / (SEUIL_BON - SEUIL_MINIMUM)
    else:
        return 1.0


def frais_bien_definis(service: Service) -> float | None:
    critere_applicable = service.frais and (
        Frais.PAYANT in service.frais or Frais.GRATUIT_SOUS_CONDITIONS in service.frais
    )

    if critere_applicable:
        return 1.0 if service.frais_autres else 0.0

    return None


# Les critères sont implémentés sous forme de fonctions qui prennent un service en
# entrée et renvoient un score entre 0 et 1.
# Dans le cas où le critère n'est pas applicable, une fonction peut renvoyer None.
# Par exemple, le critère "adresse_bien_definie" ne s'applique que si le service propose
# un mode d'accueil en présentiel ou une orientation bénéficiaire en présentiel.
CritereFn = Callable[[Service], float | None]

CRITERES: list[CritereFn] = [
    adresse_bien_definie,
    au_moins_un_frais,
    au_moins_un_mode_orientation,
    au_moins_un_public,
    au_moins_une_thematique,
    au_moins_un_moyen_de_contact,
    courriel_bien_defini,
    date_maj_recente,
    frais_bien_definis,
    description_bien_definie,
    telephone_bien_defini,
]


def score(service: Service) -> tuple[float, Mapping[str, float | None]]:
    resultats = {critere.__name__: critere(service) for critere in CRITERES}

    resultats_pertinents = {
        k: round(v, 2) for k, v in resultats.items() if v is not None
    }
    score = sum([v for v in resultats_pertinents.values()]) / len(resultats_pertinents)

    return round(score, 2), resultats
