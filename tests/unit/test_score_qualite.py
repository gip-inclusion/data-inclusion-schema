from unittest.mock import ANY

import pendulum
import pytest
from freezegun import freeze_time

from data_inclusion.schema import (
    Frais,
    ModeAccueil,
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
    Profil,
    Service,
    Thematique,
    score_qualite,
)


def service_factory(**kwargs):
    if "source" not in kwargs:
        kwargs["source"] = "3"
    return Service(id="1", structure_id="2", nom="foo", **kwargs)


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                adresse=None,
            ),
            None,
            id="sans_adresse_ok",
        ),
        pytest.param(
            service_factory(
                adresse=None,
                modes_orientation_beneficiaire=[
                    ModeOrientationBeneficiaire.SE_PRESENTER
                ],
            ),
            0.0,
            id="se_presenter_sans_adresse",
        ),
        pytest.param(
            service_factory(
                adresse=None,
                modes_accueil=[
                    ModeAccueil.EN_PRESENTIEL,
                ],
            ),
            0.0,
            id="en_presentiel_sans_adresse",
        ),
        pytest.param(
            service_factory(
                adresse="1 rue de la paix",
                modes_orientation_beneficiaire=[
                    ModeOrientationBeneficiaire.SE_PRESENTER
                ],
            ),
            1.0,
            id="se_presenter_avec_adresse",
        ),
        pytest.param(
            service_factory(
                adresse="1 rue de la paix",
                modes_accueil=[
                    ModeAccueil.EN_PRESENTIEL,
                ],
            ),
            1.0,
            id="en_presentiel_avec_adresse",
        ),
    ],
)
def test_critere_adresse_bien_definie(service: Service, attendu: float):
    assert score_qualite.adresse_bien_definie(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                telephone=None,
            ),
            None,
            id="sans_telephone_ok",
        ),
        pytest.param(
            service_factory(
                telephone=None,
                modes_orientation_accompagnateur=[
                    ModeOrientationAccompagnateur.TELEPHONER
                ],
            ),
            0.0,
            id="accompagnateur_peut_telephoner_sans_telephone",
        ),
        pytest.param(
            service_factory(
                telephone=None,
                modes_orientation_beneficiaire=[ModeOrientationBeneficiaire.TELEPHONER],
            ),
            0.0,
            id="beneficiaire_peut_telephoner_sans_telephone",
        ),
        pytest.param(
            service_factory(
                telephone="3615",
                modes_orientation_accompagnateur=[
                    ModeOrientationAccompagnateur.TELEPHONER
                ],
            ),
            1.0,
            id="accompagnateur_peut_telephoner_avec_telephone",
        ),
        pytest.param(
            service_factory(
                telephone="3615",
                modes_orientation_beneficiaire=[ModeOrientationBeneficiaire.TELEPHONER],
            ),
            1.0,
            id="beneficiaire_peut_telephoner_avec_telephone",
        ),
    ],
)
def test_critere_telephone_bien_defini(service: Service, attendu: float):
    assert score_qualite.telephone_bien_defini(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                courriel=None,
            ),
            None,
            id="sans_telephone_ok",
        ),
        pytest.param(
            service_factory(
                courriel=None,
                modes_orientation_accompagnateur=[
                    ModeOrientationAccompagnateur.ENVOYER_UN_MAIL
                ],
            ),
            0.0,
            id="accompagnateur_envoyer_un_mail_sans_courriel",
        ),
        pytest.param(
            service_factory(
                courriel=None,
                modes_orientation_beneficiaire=[
                    ModeOrientationBeneficiaire.ENVOYER_UN_MAIL
                ],
            ),
            0.0,
            id="beneficiaire_envoyer_un_mail_sans_courriel",
        ),
        pytest.param(
            service_factory(
                courriel="lorem@ipsum.dolor",
                modes_orientation_accompagnateur=[
                    ModeOrientationAccompagnateur.ENVOYER_UN_MAIL
                ],
            ),
            1.0,
            id="accompagnateur_envoyer_un_mail_avec_courriel",
        ),
        pytest.param(
            service_factory(
                courriel="lorem@ipsum.dolor",
                modes_orientation_beneficiaire=[
                    ModeOrientationBeneficiaire.ENVOYER_UN_MAIL
                ],
            ),
            1.0,
            id="beneficiaire_envoyer_un_mail_avec_courriel",
        ),
    ],
)
def test_critere_courriel_bien_defini(service: Service, attendu: float):
    assert score_qualite.courriel_bien_defini(service) == attendu


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
    service = service_factory(date_maj=pendulum.today() - age)

    assert score_qualite.date_maj_recente(service) == pytest.approx(attendu, rel=0.01)


@freeze_time("2024-01-01")
@pytest.mark.parametrize(
    ("source", "attendu"),
    [
        ("agefiph", None),
        ("france-travail", None),
        ("foobar", pytest.approx(0.0)),
    ],
)
def test_critere_date_maj_recente_sources(source, attendu):
    service = service_factory(date_maj="2021-01-01", source=source)
    assert score_qualite.date_maj_recente(service) == attendu


@pytest.mark.parametrize(
    ("thematiques", "attendu"),
    [
        pytest.param(None, 0.0, id="nul"),
        pytest.param([], 0.0, id="vide"),
        pytest.param([Thematique.FAMILLE], 1.0, id="thematique_definie"),
    ],
)
def test_critere_au_moins_une_thematique(thematiques: list[Thematique], attendu: float):
    service = service_factory(thematiques=thematiques)

    assert score_qualite.au_moins_une_thematique(service) == attendu


@pytest.mark.parametrize(
    ("profils", "attendu"),
    [
        pytest.param(None, 0.0, id="nul"),
        pytest.param([], 0.0, id="vide"),
        pytest.param([Profil.ADULTES], 1.0, id="profil_defini"),
    ],
)
def test_critere_au_moins_un_profil(profils: list[Profil], attendu: float):
    service = service_factory(profils=profils)

    assert score_qualite.au_moins_un_public(service) == attendu


@pytest.mark.parametrize(
    ("frais", "attendu"),
    [
        pytest.param(None, 0.0, id="nul"),
        pytest.param([], 0.0, id="vide"),
        pytest.param([Frais.ADHESION], 1.0, id="frais_defini"),
    ],
)
def test_critere_au_moins_un_frais(frais: list[Frais], attendu: float):
    service = service_factory(frais=frais)

    assert score_qualite.au_moins_un_frais(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                modes_orientation_beneficiaire=None,
                modes_orientation_accompagnateur=None,
            ),
            0.0,
            id="modes_orientation_nuls",
        ),
        pytest.param(
            service_factory(
                modes_orientation_beneficiaire=[],
                modes_orientation_accompagnateur=[],
            ),
            0.0,
            id="modes_orientation_vides",
        ),
        pytest.param(
            service_factory(
                modes_orientation_beneficiaire=[ModeOrientationBeneficiaire.TELEPHONER],
                modes_orientation_accompagnateur=None,
            ),
            1.0,
            id="modes_orientation_beneficiaire_defini",
        ),
        pytest.param(
            service_factory(
                modes_orientation_beneficiaire=None,
                modes_orientation_accompagnateur=[
                    ModeOrientationAccompagnateur.TELEPHONER
                ],
            ),
            1.0,
            id="modes_orientation_accompagnateur_defini",
        ),
    ],
)
def test_critere_au_moins_un_mode_orientation(service: Service, attendu: float):
    assert score_qualite.au_moins_un_mode_orientation(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                courriel=None,
                formulaire_en_ligne=None,
                page_web=None,
                prise_rdv=None,
                telephone=None,
            ),
            0.0,
            id="aucunes_coordonnees",
        ),
        pytest.param(
            service_factory(
                courriel=None,
                formulaire_en_ligne=None,
                page_web=None,
                prise_rdv=None,
                telephone="3615",
            ),
            1.0,
            id="telephone_defini",
        ),
        pytest.param(
            service_factory(
                courriel="lorem@ipsum.dolor",
                formulaire_en_ligne=None,
                page_web=None,
                prise_rdv=None,
                telephone=None,
            ),
            1.0,
            id="courriel_defini",
        ),
        pytest.param(
            service_factory(
                courriel=None,
                formulaire_en_ligne=None,
                page_web=None,
                prise_rdv="https://foo.bar",
                telephone=None,
            ),
            1.0,
            id="prise_rdv_defini",
        ),
        pytest.param(
            service_factory(
                courriel=None,
                formulaire_en_ligne="https://foo.bar",
                page_web=None,
                prise_rdv=None,
                telephone=None,
            ),
            1.0,
            id="formulaire_en_ligne_defini",
        ),
        pytest.param(
            service_factory(
                courriel=None,
                formulaire_en_ligne=None,
                page_web="https://foo.bar",
                prise_rdv=None,
                telephone=None,
            ),
            1.0,
            id="page_web_defini",
        ),
    ],
)
def test_critere_au_moins_un_moyen_de_contact(service: Service, attendu: float):
    assert score_qualite.au_moins_un_moyen_de_contact(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                presentation_resume=None,
                presentation_detail=None,
            ),
            0.0,
            id="aucune_presentation",
        ),
        pytest.param(
            service_factory(
                presentation_resume="." * 200,
                presentation_detail=None,
            ),
            0.0,
            id="description_bien_trop_courte",
        ),
        pytest.param(
            service_factory(
                presentation_resume="." * 100,
                presentation_detail="." * 200,
            ),
            0.5,
            id="presentation_assez_courte",
        ),
        pytest.param(
            service_factory(
                presentation_resume=None,
                presentation_detail="." * 400,
            ),
            1.0,
            id="presentation_longue",
        ),
    ],
)
def test_critere_description_bien_definie(service: Service, attendu: float):
    assert score_qualite.description_bien_definie(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                frais=None,
            ),
            None,
            id="frais_non_definis",
        ),
        pytest.param(
            service_factory(
                frais=[],
            ),
            None,
            id="frais_vides",
        ),
        *[
            pytest.param(
                service_factory(
                    frais=[f],
                ),
                0.0,
                id=f"{f}_sans_precisions",
            )
            for f in [Frais.PAYANT, Frais.GRATUIT_SOUS_CONDITIONS]
        ],
        *[
            pytest.param(
                service_factory(
                    frais=[f],
                    frais_autres="lorem ipsum",
                ),
                1.0,
                id=f"{f}_avec_precisions",
            )
            for f in [Frais.PAYANT, Frais.GRATUIT_SOUS_CONDITIONS]
        ],
    ],
)
def test_critere_frais_bien_definis(service: Service, attendu: float):
    assert score_qualite.frais_bien_definis(service) == attendu


@pytest.mark.parametrize(
    ("service", "attendu"),
    [
        pytest.param(
            service_factory(
                date_maj=pendulum.today(),
                thematiques=[Thematique.FAMILLE],
                frais=[Frais.ADHESION],
                profils=[Profil.ADULTES],
                telephone="3615",
                modes_orientation_beneficiaire=[ModeOrientationBeneficiaire.TELEPHONER],
                presentation_detail="longue présentation" * 100,
            ),
            1.0,
            id="service_parfait",
        ),
        pytest.param(
            service_factory(
                adresse="1 rue de la paix",
                telephone="3615",
                courriel="lorem@ipsum.dolor",
                frais=[Frais.PAYANT],
                frais_autres="lorem ipsum",
                presentation_detail="longue présentation" * 100,
                modes_accueil=[ModeAccueil.EN_PRESENTIEL],
                modes_orientation_beneficiaire=[ModeOrientationBeneficiaire.TELEPHONER],
                modes_orientation_accompagnateur=[
                    ModeOrientationAccompagnateur.ENVOYER_UN_MAIL
                ],
                date_maj=pendulum.today() - pendulum.Duration(years=3),
                thematiques=[Thematique.FAMILLE],
                profils=[Profil.ADULTES],
            ),
            round((len(score_qualite.CRITERES) - 1) / len(score_qualite.CRITERES), 2),
            id="service_presque_parfait_sans_date_maj",
        ),
        pytest.param(
            service_factory(
                date_maj=pendulum.today() - pendulum.Duration(years=3),
            ),
            0.0,
            id="service_faisandé",
        ),
    ],
)
def test_score(service: Service, attendu: float):
    # le score est la moyenne des critères applicables

    score, details = score_qualite.score(service)

    assert score == attendu
    assert details == {
        "adresse_bien_definie": ANY,
        "au_moins_un_frais": ANY,
        "au_moins_un_mode_orientation": ANY,
        "au_moins_un_moyen_de_contact": ANY,
        "au_moins_un_public": ANY,
        "au_moins_une_thematique": ANY,
        "courriel_bien_defini": ANY,
        "date_maj_recente": ANY,
        "description_bien_definie": ANY,
        "frais_bien_definis": ANY,
        "telephone_bien_defini": ANY,
    }
