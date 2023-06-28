from data_inclusion.schema.base import EnhancedEnum


class ModeOrientationAccompagnateur(EnhancedEnum):
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
    ENVOYER_UN_MAIL_AVEC_UNE_FICHE_DE_PRESCRIPTION = (
        "envoyer-un-mail-avec-une-fiche-de-prescription",
        "Envoyer un mail avec une fiche de prescription",
        None,
    )
    ENVOYER_UN_MAIL_AVEC_DES_DOCUMENTS_A_COMPLETER = (
        "envoyer-un-mail-avec-des-documents-a-completer",
        "Envoyer un mail avec des documents à compléter",
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


class ModeOrientationBeneficiaire(EnhancedEnum):
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
