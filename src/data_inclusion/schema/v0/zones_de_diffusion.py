from data_inclusion.schema.base import EnhancedEnum


class ZoneDiffusionType(EnhancedEnum):
    """Types de zones de diffusion"""

    COMMUNE = (
        "commune",
        "Commune",
        None,
    )
    EPCI = (
        "epci",
        "Intercommunalité (EPCI)",
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
    PAYS = (
        "pays",
        "Pays",
        None,
    )
