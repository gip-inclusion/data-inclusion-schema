from typing import Callable, Mapping

import pendulum

from data_inclusion.schema import (
    Structure,
)


def adresse_bien_definie(structure: Structure) -> float | None:
    return 1.0 if structure.adresse else 0.0


def telephone_bien_defini(structure: Structure) -> float | None:
    return 1.0 if structure.telephone else 0.0


def courriel_bien_defini(structure: Structure) -> float | None:
    return 1.0 if structure.courriel else 0.0


def date_maj_recente(structure: Structure) -> float:
    SIX_MOIS = pendulum.duration(months=6)
    DEUX_ANS = pendulum.duration(years=2)

    if structure.date_maj is None:
        return 0.0

    age = pendulum.instance(structure.date_maj).diff(pendulum.now())

    if age < SIX_MOIS:
        return 1.0
    elif SIX_MOIS < age < DEUX_ANS:
        # simple interpolation linéaire entre 0 et 1
        return (DEUX_ANS - age) / (DEUX_ANS - SIX_MOIS)
    else:
        return 0.0


def au_moins_une_thematique(structure: Structure) -> float:
    return 1.0 if structure.thematiques else 0.0


def coordonnees_de_contact_bien_definies(structure: Structure) -> float:
    return (
        1.0 if structure.telephone or structure.courriel or structure.adresse else 0.0
    )


def presentation_bien_definie(structure: Structure) -> float:
    SEUIL_MINIMUM = 200
    SEUIL_BON = 400

    longueur_presentation = 0

    if structure.presentation_resume:
        longueur_presentation = len(structure.presentation_resume)

    if structure.presentation_detail:
        longueur_presentation += len(structure.presentation_detail)

    if longueur_presentation < SEUIL_MINIMUM:
        return 0.0
    elif longueur_presentation < SEUIL_BON:
        # simple interpolation linéaire entre 0 et 1
        return (longueur_presentation - SEUIL_MINIMUM) / (SEUIL_BON - SEUIL_MINIMUM)
    else:
        return 1.0


CritereFn = Callable[[Structure], float | None]

CRITERES: list[CritereFn] = [
    adresse_bien_definie,
    au_moins_une_thematique,
    coordonnees_de_contact_bien_definies,
    courriel_bien_defini,
    date_maj_recente,
    presentation_bien_definie,
    telephone_bien_defini,
]


def score_structure(structure: Structure) -> tuple[float, Mapping[str, float | None]]:
    resultats = {critere.__name__: critere(structure) for critere in CRITERES}

    resultats_pertinents = {
        k: round(v, 2) for k, v in resultats.items() if v is not None
    }
    score = sum([v for v in resultats_pertinents.values()]) / len(resultats_pertinents)

    return round(score, 2), resultats
