from data_inclusion.schema.base import EnhancedEnum


class TypeCOG(EnhancedEnum):
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
