from data_inclusion.schema.base import EnhancedEnum


class ModeMobilisation(EnhancedEnum):
    ENVOYER_UN_COURRIEL = (
        "envoyer-un-courriel",
        "Envoyer un courriel",
        "Envoyer un courriel au courriel associé au service ou à la structure.",
    )
    SE_PRESENTER = (
        "se-presenter",
        "Se présenter",
        "Se présenter directement à l’adresse associée au service ou à la structure.",
    )
    TELEPHONER = (
        "telephoner",
        "Téléphoner",
        "Téléphoner au numéro associée au service ou à la structure.",
    )
    UTILISER_LIEN_MOBILISATION = (
        "utiliser-lien-mobilisation",
        "Utiliser le lien de mobilisation",
        "Utiliser le lien indiqué dans le champ service.lien_mobilisation.",
    )


class MobilisablePar(EnhancedEnum):
    USAGERS = (
        "usagers",
        "Usagers",
        "Mobilisable par les usagers.",
    )
    PROFESSIONNELS = (
        "professionnels",
        "Professionnels",
        "Mobilisable par les professionnels.",
    )
