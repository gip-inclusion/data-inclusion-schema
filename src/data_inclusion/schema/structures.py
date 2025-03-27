import textwrap
from datetime import date
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl, StringConstraints

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.labels_nationaux import LabelNational
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_structures import TypologieStructure


class Structure(BaseModel):
    # fields
    id: str
    siret: Optional[common.CodeSiret] = None
    rna: Optional[common.CodeRna] = None
    nom: Annotated[
        Annotated[str, StringConstraints(min_length=3, max_length=150)],
        Field(
            description="Nom de la structure.",
            examples=["Centre social Le Tournesol"],
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
    telephone: Optional[str] = None
    courriel: Optional[EmailStr] = None
    site_web: Optional[HttpUrl] = None
    presentation_resume: Optional[Annotated[str, StringConstraints(max_length=280)]] = (
        None
    )
    presentation_detail: Optional[str] = None
    source: str
    date_maj: Annotated[
        date,
        Field(
            description=textwrap.dedent("""\
                Date de dernière modification de la
                structure chez le producteur de données.
            """),
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
