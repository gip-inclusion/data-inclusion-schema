from data_inclusion.schema.base import EnhancedEnum


class Profil(EnhancedEnum):
    SENIORS_65 = (
        "seniors-65",
        "Seniors (+ 65 ans)",
        None,
    )
    FAMILLES_ENFANTS = (
        "familles-enfants",
        "Familles/enfants",
        None,
    )
    ADULTES = (
        "adultes",
        "Adultes",
        None,
    )
    JEUNES_16_26 = (
        "jeunes-16-26",
        "Jeunes (16-26 ans)",
        None,
    )
    PUBLIC_LANGUES_ETRANGERES = (
        "public-langues-etrangeres",
        "Public langues étrangères",
        None,
    )
    DEFICIENCE_VISUELLE = (
        "deficience-visuelle",
        "Déficience visuelle",
        None,
    )
    SURDITE = (
        "surdite",
        "Surdité",
        None,
    )
    HANDICAPS_PSYCHIQUES = (
        "handicaps-psychiques",
        (
            "Handicaps psychiques : troubles psychiatriques donnant lieu à des"
            " atteintes comportementales"
        ),
        None,
    )
    HANDICAPS_MENTAUX = (
        "handicaps-mentaux",
        "Handicaps mentaux : déficiences limitant les activités d’une personne",
        None,
    )
    FEMMES = (
        "femmes",
        "Femmes",
        "Le lieu propose des accompagnements réservés aux femmes.",
    )
    PERSONNES_HANDICAPEES = (
        "personnes-handicapees",
        "Personnes handicapées",
        (
            "Ce terme est privilégié pour désigner une incapacité persistante et "
            "significative subie par une personne dans son environnement."
        ),
    )
    PERSONNES_EN_SITUATION_DE_HANDICAP = (
        "personnes-en-situation-de-handicap",
        "Personnes en situation de handicap",
        (
            "Une personne se déplaçant temporairement en béquilles des suites d’une "
            "intervention médicale est en situation de handicap sans toutefois être "
            "handicapée."
        ),
    )
    PERSONNES_EN_SITUATION_ILLETTRISME = (
        "personnes-en-situation-illettrisme",
        "Personnes en situation d’illettrisme",
        None,
    )
    BENEFICIAIRES_RSA = (
        "beneficiaires-rsa",
        "Bénéficiaires du Revenu de Solidarité Active (RSA)",
        None,
    )
    DEMANDEURS_EMPLOI = (
        "demandeurs-demploi",
        "Demandeurs ou demandeuses d’emploi",
        None,
    )
