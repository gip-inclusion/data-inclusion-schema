from datetime import date
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field

from .labels_nationaux import LabelNational
from .thematiques import Thematique
from .typologies_de_structures import TypologieStructure


class Structure(BaseModel):
    # fields
    id: str
    siret: Optional[common.CodeSiret] = None
    rna: Optional[common.CodeRna] = None
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
                de préférence au format E.164.
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
    site_web: Annotated[
        Optional[HttpUrl],
        Field(
            description="""
                Site internet de la structure.

                L’URL est validée par un appel HTTP GET (redirections prises en compte).
                Doit suivre le format de la RFC 3986.
            """,
            default=None,
            examples=["https://www.asso-mon-entraide.net/"],
        ),
    ]
    presentation_resume: Annotated[Optional[str], Field(max_length=280)] = None
    presentation_detail: Optional[str] = None
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
    antenne: Optional[bool] = None
    lien_source: Optional[HttpUrl] = None
    horaires_ouverture: Optional[str] = None
    accessibilite: Optional[HttpUrl] = None
    labels_nationaux: Optional[set[LabelNational]] = None
    labels_autres: Optional[set[str]] = None
    thematiques: Optional[set[Thematique]] = None
