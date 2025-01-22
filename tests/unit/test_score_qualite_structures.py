from unittest.mock import ANY

import pendulum
import pytest
from freezegun import freeze_time

import data_inclusion.schema.score_qualite.structure as score_qualite
from data_inclusion.schema import (
    Structure,
    Thematique,
)


def structure_factory(**kwargs):
    if "date_maj" not in kwargs:
        kwargs["date_maj"] = pendulum.today()
    return Structure(id="1", source="3", nom="foo", **kwargs)


@pytest.mark.parametrize(
    ("structure", "attendu"),
    [
        pytest.param(
            structure_factory(
                adresse=None,
            ),
            0.0,
            id="se_presenter_sans_adresse",
        ),
        pytest.param(
            structure_factory(
                adresse="1 rue de la paix",
            ),
            1.0,
            id="se_presenter_avec_adresse",
        ),
    ],
)
def test_critere_adresse_bien_definie(structure: Structure, attendu: float):
    assert score_qualite.adresse_bien_definie(structure) == attendu


@pytest.mark.parametrize(
    ("structure", "attendu"),
    [
        pytest.param(
            structure_factory(
                telephone=None,
            ),
            0.0,
            id="accompagnateur_peut_telephoner_sans_telephone",
        ),
        pytest.param(
            structure_factory(
                telephone="3615",
            ),
            1.0,
            id="accompagnateur_peut_telephoner_avec_telephone",
        ),
    ],
)
def test_critere_telephone_bien_defini(structure: Structure, attendu: float):
    assert score_qualite.telephone_bien_defini(structure) == attendu


@pytest.mark.parametrize(
    ("structure", "attendu"),
    [
        pytest.param(
            structure_factory(
                courriel=None,
            ),
            0.0,
            id="sans_telephone_ok",
        ),
        pytest.param(
            structure_factory(
                courriel="lorem@ipsum.dolor",
            ),
            1.0,
            id="accompagnateur_envoyer_un_mail_avec_courriel",
        ),
    ],
)
def test_critere_courriel_bien_defini(structure: Structure, attendu: float):
    assert score_qualite.courriel_bien_defini(structure) == attendu


@freeze_time("2024-01-01")
@pytest.mark.parametrize(
    ("age", "attendu"),
    [
        pytest.param(pendulum.Duration(), 1.0, id="aujourdhui"),
        pytest.param(pendulum.Duration(months=6), 1.0, id="6_mois"),
        pytest.param(pendulum.Duration(months=15), 0.5, id="entre_6_mois_et_2_ans"),
        pytest.param(pendulum.Duration(years=2), 0.0, id="2_ans"),
    ],
)
def test_critere_date_maj_recente(age: pendulum.Duration, attendu: float):
    structure = structure_factory(date_maj=pendulum.today() - age)

    assert abs(score_qualite.date_maj_recente(structure) - attendu) < 0.01


@pytest.mark.parametrize(
    ("thematiques", "attendu"),
    [
        pytest.param(None, 0.0, id="nul"),
        pytest.param([], 0.0, id="vide"),
        pytest.param([Thematique.FAMILLE], 1.0, id="thematique_definie"),
    ],
)
def test_critere_au_moins_une_thematique(thematiques: list[Thematique], attendu: float):
    structure = structure_factory(thematiques=thematiques)

    assert score_qualite.au_moins_une_thematique(structure) == attendu


@pytest.mark.parametrize(
    ("structure", "attendu"),
    [
        pytest.param(
            structure_factory(
                telephone=None,
                courriel=None,
                adresse=None,
            ),
            0.0,
            id="aucunes_coordonnees",
        ),
        pytest.param(
            structure_factory(
                telephone="3615",
                courriel=None,
                adresse=None,
            ),
            1.0,
            id="telephone_defini",
        ),
        pytest.param(
            structure_factory(
                telephone=None,
                courriel="lorem@ipsum.dolor",
                adresse=None,
            ),
            1.0,
            id="courriel_defini",
        ),
        pytest.param(
            structure_factory(
                telephone=None,
                courriel=None,
                adresse="1 rue de la paix",
            ),
            1.0,
            id="adresse_definie",
        ),
    ],
)
def test_critere_coordonnees_de_contact_bien_definies(
    structure: Structure, attendu: float
):
    assert score_qualite.coordonnees_de_contact_bien_definies(structure) == attendu


@pytest.mark.parametrize(
    ("structure", "attendu"),
    [
        pytest.param(
            structure_factory(
                presentation_resume=None,
                presentation_detail=None,
            ),
            0.0,
            id="aucune_presentation",
        ),
        pytest.param(
            structure_factory(
                presentation_resume="." * 200,
                presentation_detail=None,
            ),
            0.0,
            id="presentation_bien_trop_courte",
        ),
        pytest.param(
            structure_factory(
                presentation_resume="." * 100,
                presentation_detail="." * 200,
            ),
            0.5,
            id="presentation_assez_courte",
        ),
        pytest.param(
            structure_factory(
                presentation_resume=None,
                presentation_detail="." * 400,
            ),
            1.0,
            id="presentation_longue",
        ),
    ],
)
def test_critere_presentation_bien_definie(structure: Structure, attendu: float):
    assert score_qualite.presentation_bien_definie(structure) == attendu


@pytest.mark.parametrize(
    ("structure", "attendu"),
    [
        pytest.param(
            structure_factory(
                thematiques=[Thematique.FAMILLE],
                telephone="3615",
                presentation_detail="longue présentation" * 100,
                courriel="lorem@ipsum.dolor",
                adresse="1 rue de la paix",
            ),
            1.0,
            id="structure_parfait",
        ),
        pytest.param(
            structure_factory(
                adresse="1 rue de la paix",
                telephone="3615",
                courriel="lorem@ipsum.dolor",
                presentation_detail="longue présentation" * 100,
                date_maj=pendulum.today() - pendulum.Duration(years=3),
                thematiques=[Thematique.FAMILLE],
            ),
            round((len(score_qualite.CRITERES) - 1) / len(score_qualite.CRITERES), 2),
            id="structure_presque_parfait_sans_date_maj",
        ),
        pytest.param(
            structure_factory(
                date_maj=pendulum.today() - pendulum.Duration(years=3),
            ),
            0.0,
            id="structure_faisandé",
        ),
    ],
)
def test_score(structure: Structure, attendu: float):
    # le score est la moyenne des critères applicables

    score, details = score_qualite.score_structure(structure)

    assert score == attendu
    assert details == {
        "adresse_bien_definie": ANY,
        "au_moins_une_thematique": ANY,
        "presentation_bien_definie": ANY,
        "coordonnees_de_contact_bien_definies": ANY,
        "courriel_bien_defini": ANY,
        "date_maj_recente": ANY,
        "telephone_bien_defini": ANY,
    }
