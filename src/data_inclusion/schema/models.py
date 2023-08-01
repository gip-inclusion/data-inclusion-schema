from datetime import date, datetime
from typing import Optional

import pydantic
from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl, StringConstraints
from typing_extensions import Annotated

from data_inclusion.schema.code_officiel_geographique import TypeCOG
from data_inclusion.schema.frais import Frais
from data_inclusion.schema.labels_nationaux import LabelNational
from data_inclusion.schema.modes_accueil import ModeAccueil
from data_inclusion.schema.modes_orientation import (
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
)
from data_inclusion.schema.profils import Profil
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_services import TypologieService
from data_inclusion.schema.typologies_de_structures import Typologie


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
    pre_requis: Optional[str] = None
    cumulable: Optional[bool] = None
    justificatifs: Optional[str] = None
    formulaire_en_ligne: Optional[HttpUrl] = None
    commune: Optional[str] = None
    code_postal: Optional[
        Annotated[
            str, StringConstraints(min_length=5, max_length=5, pattern=r"^\d{5}$")
        ]
    ] = None
    code_insee: Optional[
        Annotated[str, StringConstraints(min_length=5, max_length=5)]
    ] = None
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
    zone_diffusion_type: Optional[TypeCOG] = None
    zone_diffusion_code: Optional[
        Annotated[str, StringConstraints(pattern=r"^\w{5}$")]  # code commune
        | Annotated[str, StringConstraints(pattern=r"^\d{9}$")]  # code epci
        | Annotated[str, StringConstraints(pattern=r"^\w{2,3}$")]  # code departement
        | Annotated[str, StringConstraints(pattern=r"^\d{2}$")]  # code region
    ] = None
    zone_diffusion_nom: Optional[str] = None
    contact_nom_prenom: Optional[str] = None
    modes_orientation_beneficiaire: Optional[list[ModeOrientationBeneficiaire]] = None
    modes_orientation_accompagnateur: Optional[
        list[ModeOrientationAccompagnateur]
    ] = None


class Structure(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # fields
    id: str
    siret: Optional[
        Annotated[
            str, StringConstraints(min_length=14, max_length=14, pattern=r"^\d{14}$")
        ]
    ] = None
    rna: Optional[
        Annotated[
            str, StringConstraints(min_length=10, max_length=10, pattern=r"^W\d{9}$")
        ]
    ] = None
    nom: str
    commune: str
    code_postal: Annotated[
        str, StringConstraints(min_length=5, max_length=5, pattern=r"^\d{5}$")
    ]
    code_insee: Optional[
        Annotated[str, StringConstraints(min_length=5, max_length=5)]
    ] = None
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


def generate_structures_json_schema():
    """Generate the structures file json schema from the `Structure` model."""

    adapter = pydantic.TypeAdapter(list[Structure])
    schema = adapter.json_schema()

    return {
        "title": "Structures de l'insertion",
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": (
            "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
            "/main/structures.json"
        ),
        "description": "",
        **schema,
    }


def generate_services_json_schema():
    """Generate the services file json schema from the `Service` model."""

    adapter = pydantic.TypeAdapter(list[Service])
    schema = adapter.json_schema()

    return {
        "title": "Services de l'insertion",
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": (
            "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
            "/main/services.json"
        ),
        "description": "",
        **schema,
    }
