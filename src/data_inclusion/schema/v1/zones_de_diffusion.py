from data_inclusion.schema.v1.base import EnhancedEnum


class ZoneDiffusionType(EnhancedEnum):
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
