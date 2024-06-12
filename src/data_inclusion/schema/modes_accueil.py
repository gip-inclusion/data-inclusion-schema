from data_inclusion.schema.base import EnhancedEnum


class ModeAccueil(EnhancedEnum):
    A_DISTANCE = (
        "a-distance",
        "À distance",
        "L'offre de service est délivrée à distance, par téléphone ou internet.",
    )
    EN_PRESENTIEL = (
        "en-presentiel",
        "En présentiel",
        "L'offre de service est délivrée en présentiel dans les locaux spécifiés par la structure.",
    )
