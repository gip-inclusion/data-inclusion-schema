import pendulum
import pydantic
import pytest
from freezegun import freeze_time

from data_inclusion.schema.v1 import Service, Structure


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
