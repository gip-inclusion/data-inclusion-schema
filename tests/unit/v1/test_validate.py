import pendulum
import pydantic
import pydantic_core
import pytest
from freezegun import freeze_time

from data_inclusion.schema.v1 import Service, Structure


def has_error(loc: str, errors_details: list[pydantic_core.ErrorDetails]) -> bool:
    return any(error["loc"] == (loc,) for error in errors_details)


@freeze_time("2024-01-01")
@pytest.mark.parametrize("model", [Structure, Service])
@pytest.mark.parametrize(
    ("date_maj", "est_valide"),
    [
        # la date de maj doit être au 21e siècle
        (pendulum.date(year=1999, month=12, day=31), False),
        (pendulum.date(year=2000, month=1, day=1), True),
        # la date de maj ne peut pas être dans le futur
        (pendulum.date(year=2024, month=1, day=1), True),
        (pendulum.date(year=2024, month=1, day=2), False),
    ],
)
def test_date_maj_valide(factory, date_maj, est_valide):
    try:
        factory(date_maj=date_maj)
    except pydantic.ValidationError as exc:
        assert not est_valide
        assert "date_maj" in str(exc)
    else:
        assert est_valide


@pytest.mark.parametrize("model", [Structure, Service])
@pytest.mark.parametrize(
    ("nom", "est_valide"),
    [
        ("*" * 2, False),
        ("*" * 3, True),
        ("*" * 150, True),
        ("*" * 151, False),
    ],
)
def test_longueur_nom(model, nom, est_valide):
    try:
        model.model_validate({"nom": nom})
    except pydantic.ValidationError as exc:
        assert est_valide != has_error("nom", exc.errors())
    else:
        assert est_valide


@pytest.mark.parametrize("model", [Structure, Service])
@pytest.mark.parametrize(
    ("nom", "is_error"),
    [
        ("Centre social Le Tournesol.", True),
        ("Centre social Le Tournesol", False),
        ("Centre social Le Tournesol etc.", False),
    ],
)
def test_nom_ne_se_termine_pas_par_un_point(model, nom, is_error):
    try:
        model.model_validate({"nom": nom})
    except pydantic.ValidationError as exc:
        assert not has_error("nom", exc.errors())

    try:
        model.model_validate({"nom": nom}, context={"ignore_warnings": False})
    except pydantic.ValidationError as exc:
        assert is_error == has_error("nom", exc.errors())
    else:
        pytest.fail()
