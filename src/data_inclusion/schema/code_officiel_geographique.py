from data_inclusion.schema.base import EnhancedEnum


class TypeCOG(EnhancedEnum):
    COMMUNE = (
        "commune",
        "Commune",
        None,
    )
    REGION = (
        "region",
        "Région",
        None,
    )
    DEPARTEMENT = (
        "departement",
        "Département",
        None,
    )
