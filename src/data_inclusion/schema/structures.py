from datetime import date, datetime
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl, StringConstraints

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel
from data_inclusion.schema.labels_nationaux import LabelNational
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_structures import Typologie


class Structure(BaseModel):
    # fields
    id: Annotated[
        str,
        Field(
            description="""
                Identifiant unique de la structure. Doit être stable et immuable.
            """,
            examples=[
                "c3d15659-0000-0000-0000-04d50f6ace57"
            ],
        ),
    ]
    siret: Annoted[
        Optional[common.CodeSiret],
        Field(
            description="""
                Système d'identification du répertoire des établissements. Il est composé de 14 chiffres.
            """,
            examples=[
                "362 521 879 00034"
            ],
        ),
    ] = None
    rna: Annoted[
        Optional[common.CodeRna],
        Field(
             description="""
                Système d'identification du Répertoire National des Associations. Il est composé de la lettre W suivis de 9 chiffres.
            """,
            examples=[
                "W153264789"
            ],
        ),
    ] = None
    nom: Annotated[
        str,
        Field(
            description="""
                Nom de la structure.
            """,
            examples=[
                "Mission locale de Marseille"
            ],
        ),
    ]
    commune: Annoted[
        Optional[str],
        Field(
            description="""
                Nom de la ville où est située la structure.
            """,
            examples=[
                "Marseille"
            ],
        ),
    ] = None
    code_postal: Annoted[
        Optional[common.CodePostal],
        Field(
            description="""
                Code postal de la commune où est située la structure.
            """,
            examples=[
                "13000"
            ],
        ),
    ] = None
    code_insee: Annoted[
        Optional[common.CodeCommune],
        Field(
            description="""
                Code INSEE de la commune où est située la structure.
            """,
            examples=[
                "13055"
            ],
        ),
    ] = None
    adresse: Annoted[
        Optional[str],
        Field(
            description="""
                Numéro et voie de l'adresse où est située la structure.
            """,
            examples=[
                "35 rue Paradis"
            ],
        ),
    ] = None
    complement_adresse: Annoted[
        Optional[str],
        Field(
            description="""
                Informations postales supplémentaires.
            """,
            examples=[
                "Centre d'activités Le Folgoët"
            ],
        ),
    ] = None
    longitude: Annoted[
        Optional[float],
        Field(
            description="""
                Longitude de l'adresse où est située la structure.
            """
        ),
    ] = None
    latitude: Annoted[
        Optional[float],
        Field(
            description="""
                Latitude de l'adresse où est située l'offre de service.
            """
        ),
    ] = None
    typologie: Annoted[
        Optional[Typologie],
        Field(
            description="""
                Typologie de la structure.
            """,
            examples=[
                "Mission locale",
                "Association"
            ],
        ),
    ] = None
    telephone: Annoted[
        Optional[str],
        Field(
            description="""
                 Numéro de téléphone de la structure.
            """
        ),
    ] = None
    courriel: Annoted[
        Optional[EmailStr],
        Field(
            description="""
                 Adresse email de la structure.
            """
        ),
    ] = None
    site_web: Annoted[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers le site web de la structure. Ce champ n'est pas destiné à recevoir un lien vers le site
                d'un producteur de donnée.
            """,
            examples=[
                "https://missionlocalemarseille.fr/"
            ],
        ),
    ] = None
    presentation_resume: Annoted[
        Optional[str],
        StringConstraints(max_length=280),
        Field(
            description="""
                Présentation succincte de la structure.
            """,
            examples=[
                "Association Loi 1901 créée en 1997 sous l’impulsion de la Ville de Marseille, la Mission Locale de Marseille a pour objectif l’accompagnement et l’insertion des jeunes par l’emploi et la formation."
            ],
        ),
    ] = None
    presentation_detail: Annoted[
        Optional[str],
        Field(
            description="""
                Présentation détaillée de la structure.
            """
        ),    
    ] = None
    source: Annotated[
        str,
        Field(
            description="""
                Nom du producteur de données dont provient la structure.
            """,
            examples=[
                "france-travail"
            ],
        ),
    ]
    date_maj: Annoted[
        Optional[date | datetime],
        Field(
            description="""
                 Date à laquelle les données de la structure ont été mises à jour.
            """
        ),
    ] = None
    antenne: Annoted[
        Optional[bool],
        Field(
            description="""
                 Indique si la structure est une antenne d'une organisation nationale.
            """
        ),
    ] = None
    lien_source: Annoted[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers la page web de la structure sur le site web du producteur de données. Différent du champ site_web qui renvoie sur le site web de la structure.
            """,
            examples=[
                "https://dora.inclusion.beta.gouv.fr/structures/mission-locale-de-ma-hcwe"
            ],
        ),
    ] = None
    horaires_ouverture: Annoted[
        Optional[str],
        Field(
            description="""
                Horaires d'ouverture de la structure au format OpenStreetMap.
            """,
            examples=[
                "Tu 08:00-12:00; Th 14:00-18:00"
            ],
        ),
    ] = None
    accessibilite: Annoted[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers la structure dans le référentiel numérique de l'accessibilité.
            """,
            examples=[
                "https://acceslibre.beta.gouv.fr/app/92-courbevoie/a/restauration-rapide/erp/0zo/"
            ],
        ),
    ] = None
    labels_nationaux: Annoted[
        Optional[set[LabelNational]],
        Field(
            description="""
                Nom du réseau national à laquelle la structure appartient.
            """,
            examples=[
                "France Travail"
            ], 
        ),
    ] = None
    labels_autres: Annoted[
        Optional[set[str]],
        Field(
            description="""
                Nom du réseau national à laquelle la structure appartient (si non présent dans la liste labels_nationaux).
            """,
            examples=[
                "Mission locale"
            ],
        ),
    ] = None
    thematiques: Annoted[
        Optional[set[Thematique]],
        Field(
            description="""
                Thématique abordée par la structure.
            """,
            examples=[
                "Trouver un emploi"
            ],
        ),
    ] = None
