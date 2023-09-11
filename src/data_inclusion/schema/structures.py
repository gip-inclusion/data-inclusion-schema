from datetime import date, datetime
from typing import Optional

from pydantic import ConfigDict, EmailStr, HttpUrl, StringConstraints
from typing_extensions import Annotated

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel
from data_inclusion.schema.labels_nationaux import LabelNational
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_structures import Typologie


class Structure(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # fields
    id: str
    siret: Optional[common.CodeSiret] = None
    rna: Optional[common.CodeRna] = None
    nom: str
    commune: str
    code_postal: common.CodePostal
    code_insee: Optional[common.CodeCommune] = None
    adresse: str
    complement_adresse: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    typologie: Optional[Typologie] = None
    telephone: Optional[str] = None
    courriel: Optional[EmailStr] = None
    site_web: Optional[HttpUrl] = None
    presentation_resume: Optional[
        Annotated[str, StringConstraints(max_length=280)]
    ] = None
    presentation_detail: Optional[str] = None
    source: Optional[str] = None
    date_maj: date | datetime
    antenne: bool = False
    lien_source: Optional[HttpUrl] = None
    horaires_ouverture: Optional[str] = None
    accessibilite: Optional[HttpUrl] = None
    labels_nationaux: Optional[list[LabelNational]] = None
    labels_autres: Optional[list[str]] = None
    thematiques: Optional[list[Thematique]] = None
