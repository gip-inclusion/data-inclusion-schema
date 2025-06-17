from data_inclusion.schema.base import EnhancedEnum


class Frais(EnhancedEnum):
    """Frais"""

    GRATUIT = (
        "gratuit",
        "Gratuit",
        "Je peux accéder gratuitement au lieu et à ses services",
    )
    PAYANT = (
        "payant",
        "Payant",
        "L’accès au lieu et/ou à ses services est payant",
    )
