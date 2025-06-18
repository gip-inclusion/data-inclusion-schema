from typing import Callable, Mapping

import pendulum

from data_inclusion.schema.v1 import (
    Frais,
    ModeAccueil,
    ModeMobilisation,
    Service,
)


def adresse_bien_definie(service: Service) -> float | None:
    critere_applicable = (
        service.modes_accueil and ModeAccueil.EN_PRESENTIEL in service.modes_accueil
    ) or (
        service.modes_mobilisation
        and ModeMobilisation.SE_PRESENTER in service.modes_mobilisation
    )

    if critere_applicable:
        return 1.0 if service.adresse else 0.0

    return None


def telephone_bien_defini(service: Service) -> float | None:
    critere_applicable = (
        service.modes_mobilisation
        and ModeMobilisation.TELEPHONER in service.modes_mobilisation
    )
    if critere_applicable:
        return 1.0 if service.telephone else 0.0

    return None


def courriel_bien_defini(service: Service) -> float | None:
    critere_applicable = (
        service.modes_mobilisation
        and ModeMobilisation.ENVOYER_UN_COURRIEL in service.modes_mobilisation
    )

    if critere_applicable:
        return 1.0 if service.courriel else 0.0

    return None


def modes_mobilisation_bien_definis(service: Service) -> float:
    match service:
        case Service(modes_mobilisation=None, mobilisable_par=None):
            return 0.0
        case Service(modes_mobilisation=modes_mobilisation, mobilisable_par=None) if (
            modes_mobilisation is not None
        ):
            return 0.5
        case Service(modes_mobilisation=None, mobilisable_par=mobilisable_par) if (
            mobilisable_par is not None
        ):
            return 0.5
        case Service(
            modes_mobilisation=modes_mobilisation, mobilisable_par=mobilisable_par
        ) if modes_mobilisation is not None and mobilisable_par is not None:
            return 1.0
        case _:
            raise ValueError()


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
    return 1.0 if service.publics else 0.0


def au_moins_un_moyen_de_contact(service: Service) -> float:
    return (
        1.0
        if any(
            (
                service.courriel,
                service.lien_mobilisation,
                service.telephone,
            )
        )
        else 0.0
    )


def description_bien_definie(service: Service) -> float:
    SEUIL_MINIMUM = 200
    SEUIL_BON = 400

    if len(service.description) < SEUIL_MINIMUM:
        return 0.0
    elif len(service.description) < SEUIL_BON:
        # simple interpolation linéaire entre 0 et 1
        return (len(service.description) - SEUIL_MINIMUM) / (SEUIL_BON - SEUIL_MINIMUM)
    else:
        return 1.0


def frais_bien_definis(service: Service) -> float:
    match service:
        case Service(frais=None):
            return 0.0
        case Service(frais=Frais.PAYANT, frais_precisions=None):
            return 0.5
        case Service(frais=Frais.PAYANT, frais_precisions=frais_precisions) if (
            frais_precisions
        ):
            return 1.0
        case Service(frais=Frais.GRATUIT):
            return 1.0
        case _:
            raise ValueError()


# Les critères sont implémentés sous forme de fonctions qui prennent un service en
# entrée et renvoient un score entre 0 et 1.
# Dans le cas où le critère n'est pas applicable, une fonction peut renvoyer None.
# Par exemple, le critère "adresse_bien_definie" ne s'applique que si le service propose
# un mode d'accueil en présentiel ou une orientation bénéficiaire en présentiel.
CritereFn = Callable[[Service], float | None]

CRITERES: list[CritereFn] = [
    adresse_bien_definie,
    modes_mobilisation_bien_definis,
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
