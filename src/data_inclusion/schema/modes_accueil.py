from data_inclusion.schema.base import EnhancedEnum


class ModeAccueil(EnhancedEnum):
    A_DISTANCE = (
        "a-distance",
        "À distance",
        None,
    )
    EN_PRESENTIEL = (
        "en-presentiel",
        "En présentiel",
        None,
    )
