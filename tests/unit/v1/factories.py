import pendulum

from data_inclusion.schema.v1 import (
    Service,
    Structure,
)


def service_factory(**kwargs):
    defaults = {
        "id": "1",
        "structure_id": "2",
        "nom": "foo",
        "date_maj": pendulum.today(),
        "source": "3",
        "description": "." * 500,
    }
    kwargs = defaults | kwargs
    return Service(**kwargs)


def structure_factory(**kwargs):
    defaults = {
        "id": "1",
        "nom": "foo",
        "date_maj": pendulum.today(),
        "source": "3",
    }
    kwargs = defaults | kwargs
    return Structure(**kwargs)
