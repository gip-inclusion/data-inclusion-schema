from data_inclusion.schema.base import EnhancedEnum


class TypeService(EnhancedEnum):
    """Types de services"""

    ACCOMPAGNEMENT = (
        "accompagnement",
        "Accompagnement",
        "Accompagnement global pour le retour à l’emploi",
    )
    AIDE_FINANCIERE = (
        "aide-financiere",
        "Aide financière",
        "Prise en charge financière, aide ou rémunération soutenant le "
        "retour à l’emploi",
    )
    AIDE_MATERIELLE = (
        "aide-materielle",
        "Aide materielle",
        "Accéder à du matériel soutenant le retour à l’emploi (voiture, vélo, "
        "ordinateur, alimentation, etc)",
    )
    ATELIER = (
        "atelier",
        "Atelier",
        "Groupe de travail constitué autour d’une activité, d’un thème "
        "soutenant le retour à l’emploi",
    )
    FORMATION = (
        "formation",
        "Formation",
        "Formation dispensée par des professionnels pour les bénéficiaires",
    )
    INFORMATION = (
        "information",
        "Information",
        "Premier niveau d’information apporté par des professionnels du secteur",
    )
