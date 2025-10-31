import pendulum
import pydantic
import pytest
from freezegun import freeze_time

from data_inclusion.schema import validation
from data_inclusion.schema.v1 import Service, Structure


def has_error(loc: str, exc: pydantic.ValidationError) -> bool:
    return any(error["loc"] == (loc,) for error in exc.errors())


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
        assert est_valide != has_error("nom", exc)
    else:
        assert est_valide


@pytest.mark.parametrize("model", [Structure, Service])
@pytest.mark.parametrize(
    ("nom", "mode", "est_valide"),
    [
        ("Centre social Le Tournesol.", validation.Mode.NORMAL, True),
        ("Centre social Le Tournesol.", validation.Mode.STRICT, False),
        ("Centre social Le Tournesol", validation.Mode.NORMAL, True),
        ("Centre social Le Tournesol etc.", validation.Mode.NORMAL, True),
    ],
)
def test_nom_ne_se_termine_pas_par_un_point(model, mode, nom, est_valide):
    try:
        model.model_validate({"nom": nom}, context={"mode": mode})
    except pydantic.ValidationError as exc:
        assert est_valide != has_error("nom", exc)
    else:
        assert est_valide
