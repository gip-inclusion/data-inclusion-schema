from data_inclusion.schema.base import EnhancedEnum


class ModeMobilisation(EnhancedEnum):
    ENVOYER_UN_COURRIEL = (
        "envoyer-un-courriel",
        "Envoyer un courriel",
        (
            "Envoyer un courriel à l’adresse électronique associée au service, ou à"
            " défaut à la structure."
        ),
    )
    SE_PRESENTER = (
        "se-presenter",
        "Se présenter",
        "Se présenter directement à l’adresse associée au service ou à la structure.",
    )
    TELEPHONER = (
        "telephoner",
        "Téléphoner",
        "Téléphoner au numéro associé au service, ou à défaut à la structure.",
    )
    UTILISER_LIEN_MOBILISATION = (
        "utiliser-lien-mobilisation",
        "Utiliser le lien de mobilisation",
        "Utiliser le lien de mobilisation du service.",
    )


class PersonneMobilisatrice(EnhancedEnum):
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
