from data_inclusion.schema.base import EnhancedEnum


class MobilisablePar(EnhancedEnum):
    USAGERS = (
        "usagers",
        "Usagers",
        "Service mobilisable par les usagers",
    )
    PROFESSIONNELS = (
        "professionnels",
        "Professionnels",
        "Service mobilisable par les professionnels",
    )
