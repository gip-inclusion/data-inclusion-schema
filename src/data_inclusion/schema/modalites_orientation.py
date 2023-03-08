from data_inclusion.schema.base import EnhancedEnum


class ModaliteOrientationBeneficiaire(EnhancedEnum):
    COMPLETER_LE_FORMULAIRE_DADHESION = (
        "completer-le-formulaire-dadhesion",
        "Compléter le formulaire d’adhésion",
        None,
    )
    ENVOYER_UN_MAIL = (
        "envoyer-un-mail",
        "Envoyer un mail",
        None,
    )
    SE_PRESENTER = (
        "se-presenter",
        "Se présenter",
        None,
    )
    TELEPHONER = (
        "telephoner",
        "Téléphoner",
        None,
    )
    AUTRE = (
        "autre",
        "Autre",
        None,
    )
