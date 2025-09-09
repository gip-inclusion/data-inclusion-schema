import pytest

from data_inclusion.schema.v1 import (
    Service,
    Structure,
)

from . import factories


@pytest.fixture
def factory(model):
    if model == Service:
        return factories.service_factory
    elif model == Structure:
        return factories.structure_factory
    raise ValueError(f"Unknown model: {model}")
