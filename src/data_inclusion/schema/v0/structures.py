from datetime import date
from typing import Annotated

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field

from .labels_nationaux import LabelNational
from .thematiques import Thematique
from .typologies_de_structures import TypologieStructure


class Structure(BaseModel):
    # fields
    id: str
    siret: common.CodeSiret | None = None
    rna: common.CodeRna | None = None
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
    commune: str | None = None
    code_postal: common.CodePostal | None = None
    code_insee: common.CodeCommune | None = None
    adresse: str | None = None
    complement_adresse: str | None = None
    longitude: float | None = None
    latitude: float | None = None
    typologie: TypologieStructure | None = None
    telephone: Annotated[
        str | None,
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
    ] = None
    courriel: Annotated[
        EmailStr | None,
        Field(
            description="""
                Courriel à utiliser pour obtenir des informations complémentaires sur
                la structure.

                Doit suivre le format de la RFC 5322.
            """,
            default=None,
            examples=["exemple@inclusion.gouv.fr"],
        ),
    ] = None
    site_web: Annotated[
        HttpUrl | None,
        Field(
            description="""
                Site internet de la structure.

                L’URL est validée par un appel HTTP GET (redirections prises en compte).
                Doit suivre le format de la RFC 3986.
            """,
            default=None,
            examples=["https://www.asso-mon-entraide.net/"],
        ),
    ] = None
    presentation_resume: Annotated[str | None, Field(max_length=280)] = None
    presentation_detail: str | None = None
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
    antenne: bool | None = None
    lien_source: HttpUrl | None = None
    horaires_ouverture: str | None = None
    accessibilite: HttpUrl | None = None
    labels_nationaux: set[LabelNational] | None = None
    labels_autres: set[str] | None = None
    thematiques: set[Thematique] | None = None
