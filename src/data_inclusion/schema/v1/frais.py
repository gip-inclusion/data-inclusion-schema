from data_inclusion.schema.base import EnhancedEnum


class Frais(EnhancedEnum):
    """Frais"""

    GRATUIT = (
        "gratuit",
        "Gratuit",
        "L’accès au lieu et/ou à ses services est gratuit",
    )
    PAYANT = (
        "payant",
        "Payant",
        "L’accès au lieu et/ou à ses services est payant",
    )
