from datetime import date, datetime
from typing import Optional

from pydantic import ConfigDict, EmailStr, HttpUrl, StringConstraints
from typing_extensions import Annotated

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel
from data_inclusion.schema.frais import Frais
from data_inclusion.schema.modes_accueil import ModeAccueil
from data_inclusion.schema.modes_orientation import (
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
)
from data_inclusion.schema.profils import Profil
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_services import TypologieService
from data_inclusion.schema.zones_de_diffusion import ZoneDiffusionType


class Service(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # fields
    id: str
    structure_id: Optional[str] = None
    source: str
    nom: str
    presentation_resume: Optional[
        Annotated[str, StringConstraints(max_length=280)]
    ] = None
    presentation_detail: Optional[str] = None
    types: Optional[list[TypologieService]] = None
    thematiques: Optional[list[Thematique]] = None
    prise_rdv: Optional[HttpUrl] = None
    frais: Optional[list[Frais]] = None
    frais_autres: Optional[str] = None
    profils: Optional[list[Profil]] = None
    pre_requis: Optional[list[str]] = None
    cumulable: Optional[bool] = None
    justificatifs: Optional[list[str]] = None
    formulaire_en_ligne: Optional[HttpUrl] = None
    commune: Optional[str] = None
    code_postal: Optional[common.CodePostal] = None
    code_insee: Optional[common.CodeCommune] = None
    adresse: Optional[str] = None
    complement_adresse: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    recurrence: Optional[str] = None
    date_creation: Optional[date] = None
    date_suspension: Optional[date] = None
    lien_source: Optional[HttpUrl] = None
    telephone: Optional[str] = None
    courriel: Optional[EmailStr] = None
    contact_public: Optional[bool] = None
    date_maj: Optional[date | datetime] = None
    modes_accueil: Optional[list[ModeAccueil]] = None
    zone_diffusion_type: Optional[ZoneDiffusionType] = None
    zone_diffusion_code: Optional[
        common.CodeCommune
        | common.CodeEPCI
        | common.CodeDepartement
        | common.CodeRegion
    ] = None
    zone_diffusion_nom: Optional[str] = None
    contact_nom_prenom: Optional[str] = None
    modes_orientation_beneficiaire: Optional[list[ModeOrientationBeneficiaire]] = None
    modes_orientation_beneficiaire_autres: Optional[str] = None
    modes_orientation_accompagnateur: Optional[
        list[ModeOrientationAccompagnateur]
    ] = None
    modes_orientation_accompagnateur_autres: Optional[str] = None
