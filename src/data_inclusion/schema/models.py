from datetime import date, datetime
from typing import Optional

import pydantic
from pydantic import BaseModel, EmailStr, Extra, HttpUrl, constr

from data_inclusion.schema.code_officiel_geographique import TypeCOG
from data_inclusion.schema.frais import Frais
from data_inclusion.schema.labels_nationaux import LabelNational
from data_inclusion.schema.modes_accueil import ModeAccueil
from data_inclusion.schema.profils import Profil
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_services import TypologieService
from data_inclusion.schema.typologies_de_structures import Typologie


class Service(BaseModel):
    id: str
    structure_id: Optional[str]
    source: str
    nom: str
    presentation_resume: Optional[constr(max_length=280)]
    presentation_detail: Optional[str]
    types: Optional[list[TypologieService]]
    thematiques: Optional[list[Thematique]]
    prise_rdv: Optional[HttpUrl]
    frais: Optional[list[Frais]]
    frais_autres: Optional[str]
    profils: Optional[list[Profil]]
    pre_requis: Optional[str]
    cumulable: Optional[bool]
    justificatifs: Optional[str]
    formulaire_en_ligne: Optional[HttpUrl]
    commune: Optional[str]
    code_postal: Optional[constr(min_length=5, max_length=5, regex=r"^\d{5}$")]
    code_insee: Optional[constr(min_length=5, max_length=5)]
    adresse: Optional[str]
    complement_adresse: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    recurrence: Optional[str]
    date_creation: Optional[date]
    date_suspension: Optional[date]
    lien_source: Optional[HttpUrl]
    telephone: Optional[str]
    courriel: Optional[EmailStr]
    contact_public: Optional[bool]
    date_maj: Optional[date | datetime]
    modes_accueil: Optional[list[ModeAccueil]]
    zone_diffusion_type: Optional[TypeCOG]
    zone_diffusion_code: Optional[
        constr(regex=r"^\w{5}$")  # code commune
        | constr(regex=r"^\w{2,3}$")  # code departement
        | constr(regex=r"^\d{2}$")  # code region
    ]
    zone_diffusion_nom: Optional[str]

    class Config:
        extra = Extra.forbid


class Structure(BaseModel):
    id: str
    siret: Optional[constr(min_length=14, max_length=14, regex=r"^\d{14}$")]
    rna: Optional[constr(min_length=10, max_length=10, regex=r"^W\d{9}$")]
    nom: str
    commune: str
    code_postal: constr(min_length=5, max_length=5, regex=r"^\d{5}$")
    code_insee: Optional[constr(min_length=5, max_length=5)]
    adresse: str
    complement_adresse: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    typologie: Optional[Typologie]
    telephone: Optional[str]
    courriel: Optional[EmailStr]
    site_web: Optional[HttpUrl]
    presentation_resume: Optional[constr(max_length=280)]
    presentation_detail: Optional[str]
    source: Optional[str]
    date_maj: date | datetime
    antenne: bool = False
    lien_source: Optional[HttpUrl]
    horaires_ouverture: Optional[str]
    accessibilite: Optional[HttpUrl]
    labels_nationaux: Optional[list[LabelNational]]
    labels_autres: Optional[list[str]]
    thematiques: Optional[list[Thematique]]

    class Config:
        extra = Extra.forbid


def generate_structures_json_schema():
    """Generate the structures file json schema from the `Structure` model."""

    # json schema for a file containing a **list** of structures
    return {
        "title": "Structures de l'insertion",
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": (
            "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
            "/main/structures.json"
        ),
        "description": "",
        "type": "array",
        "items": {
            "$ref": "#/definitions/Structure",
        },
        # Pydantic generates the json schema of a **single** structure from the
        # `Structure` model. Only the definitions are extracted.
        "definitions": pydantic.schema_of(Structure)["definitions"],
    }


def generate_services_json_schema():
    """Generate the services file json schema from the `Service` model."""

    # json schema for a file containing a **list** of services
    return {
        "title": "Services de l'insertion",
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": (
            "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
            "/main/services.json"
        ),
        "description": "",
        "type": "array",
        "items": {
            "$ref": "#/definitions/Service",
        },
        # Pydantic generates the json schema of a **single** service from the
        # `Service` model. Only the definitions are extracted.
        "definitions": pydantic.schema_of(Service)["definitions"],
    }
