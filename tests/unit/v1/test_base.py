from data_inclusion.schema.v1 import ModeAccueil


def test_enum_str():
    assert str(ModeAccueil.A_DISTANCE) == "a-distance"
    assert repr(ModeAccueil.A_DISTANCE) == "<ModeAccueil.A_DISTANCE: 'a-distance'>"
