from datetime import date
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.v0 import LabelNational, TypologieStructure


class Structure(BaseModel):
    # fields
    id: str
    siret: Optional[common.CodeSiret] = None
    nom: Annotated[
        str,
        Field(
            description="""
                Nom de la structure.

                Chaîne de caractères entre 3 et 150 caractères,
                ne se terminant pas par un point.
            """,
            examples=["Centre social Le Tournesol"],
            min_length=3,
            max_length=150,
        ),
    ]
    commune: Optional[str] = None
    code_postal: Optional[common.CodePostal] = None
    code_insee: Optional[common.CodeCommune] = None
    adresse: Optional[str] = None
    complement_adresse: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    typologie: Optional[TypologieStructure] = None
    telephone: Annotated[
        Optional[str],
        Field(
            description="""
                Numéro de téléphone à utiliser pour obtenir des informations
                complémentaires sur la structure.

                Chaîne de caractères contenant un seul numéro de téléphone,
                de préfèrence au format E.164.
            """,
            examples=["+33123456789"],
            default=None,
            title="Téléphone",
        ),
    ]
    courriel: Annotated[
        Optional[EmailStr],
        Field(
            description="""
                Courriel à utiliser pour obtenir des informations complémentaires sur
                la structure.

                Doit suivre le format de la RFC 5322.
            """,
            default=None,
            examples=["exemple@inclusion.gouv.fr"],
        ),
    ]
    site_web: Optional[HttpUrl] = None
    description: Annotated[
        str,
        Field(
            description="""
                Description de la structure.

                Entre 50 et 2000 caractères.
            """,
            examples=[
                """L’association 3027 offre un accès gratuit aux arts, à la culture et
                au sport pour toutes et tous sans distinction et en priorité aux
                personnes en situation de précarité et d’isolement."""
            ],
            min_length=50,
            max_length=2000,
        ),
    ]
    source: str
    date_maj: Annotated[
        date,
        Field(
            description="""
                Date de dernière modification de la
                structure chez le producteur de données.
            """,
            examples=["2025-02-14"],
            title="Date de dernière modification",
        ),
    ]
    horaires_ouverture: Optional[str] = None
    accessibilite: Optional[HttpUrl] = None
    labels_nationaux: Optional[set[LabelNational]] = None
    labels_autres: Optional[set[str]] = None
