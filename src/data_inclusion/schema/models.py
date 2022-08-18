from datetime import date, datetime
from enum import Enum
from typing import Optional

import pydantic
from pydantic import BaseModel, EmailStr, Extra, HttpUrl, constr


class Typologie(str, Enum):
    ACI = "ACI"
    ACIPHC = "ACIPHC"
    AFPA = "AFPA"
    AI = "AI"
    ASE = "ASE"
    ASSO = "ASSO"
    ASSO_CHOMEUR = "ASSO_CHOMEUR"
    Autre = "Autre"
    BIB = "BIB"
    CAARUD = "CAARUD"
    CADA = "CADA"
    CAF = "CAF"
    CAP_EMPLOI = "CAP_EMPLOI"
    CAVA = "CAVA"
    CC = "CC"
    CCAS = "CCAS"
    CCONS = "CCONS"
    CD = "CD"
    CHRS = "CHRS"
    CHU = "CHU"
    CIAS = "CIAS"
    CIDFF = "CIDFF"
    CITMET = "CITMET"
    CPH = "CPH"
    CS = "CS"
    CSAPA = "CSAPA"
    DEETS = "DEETS"
    DEPT = "DEPT"
    DIPLP = "DIPLP"
    E2C = "E2C"
    EA = "EA"
    EATT = "EATT"
    EI = "EI"
    EITI = "EITI"
    EPCI = "EPCI"
    EPIDE = "EPIDE"
    ETTI = "ETTI"
    FAIS = "FAIS"
    GEIQ = "GEIQ"
    HUDA = "HUDA"
    MDE = "MDE"
    MDEF = "MDEF"
    MDPH = "MDPH"
    MDS = "MDS"
    MJC = "MJC"
    ML = "ML"
    MQ = "MQ"
    MSA = "MSA"
    MUNI = "MUNI"
    OACAS = "OACAS"
    ODC = "ODC"
    OF = "OF"
    OIL = "OIL"
    OPCS = "OPCS"
    PAD = "PAD"
    PE = "PE"
    PENSION = "PENSION"
    PIJ_BIJ = "PIJ_BIJ"
    PIMMS = "PIMMS"
    PJJ = "PJJ"
    PLIE = "PLIE"
    PREF = "PREF"
    PREVENTION = "PREVENTION"
    REG = "REG"
    RFS = "RFS"
    RS_FJT = "RS_FJT"
    SCP = "SCP"
    SPIP = "SPIP"
    TIERS_LIEUX = "TIERS_LIEUX"
    UDAF = "UDAF"


class LabelNational(str, Enum):
    ACTION_LOGEMENT = "ACTION_LOGEMENT"
    ADIE = "ADIE"
    AFPA = "AFPA"
    AGEFIPH = "AGEFIPH"
    AIDANTS_CONNECT = "AIDANTS_CONNECT"
    ALLIANCE_VILLES_EMPLOI = "ALLIANCE_VILLES_EMPLOI"
    ANLCI = "ANLCI"
    APEC = "APEC"
    APELS = "APELS"
    APPRENTIS_DAUTEUIL = "APPRENTIS_DAUTEUIL"
    APTIC = "APTIC"
    BANQUES_ALIMENTAIRES = "BANQUES_ALIMENTAIRES"
    BGE = "BGE"
    CAF = "CAF"
    CAMPUS_CONNECTE = "CAMPUS_CONNECTE"
    CCI = "CCI"
    CHANTIER_ECOLE = "CHANTIER_ECOLE"
    CHEOPS = "CHEOPS"
    CIDFF = "CIDFF"
    CNAM = "CNAM"
    COORACE = "COORACE"
    CREPI = "CREPI"
    CRESUS = "CRESUS"
    CROIX_ROUGE = "CROIX_ROUGE"
    DIHAL = "DIHAL"
    DUO_FOR_A_JOB = "DUO_FOR_A_JOB"
    ECOLES_DE_LA_DEUXIEME_CHANCE = "ECOLES_DE_LA_DEUXIEME_CHANCE"
    EGEE = "EGEE"
    EMMAUS = "EMMAUS"
    ENVIE = "ENVIE"
    EPIDE = "EPIDE"
    ESPACE_EMPLOI_AGRIC_ARRCO = "ESPACE_EMPLOI_AGRIC_ARRCO"
    FABRIQUE_DE_TERRITOIRE = "FABRIQUE_DE_TERRITOIRE"
    FACE = "FACE"
    FEDE_PRO_FEM = "FEDE_PRO_FEM"
    FEDERATION_DES_ACTEURS_DE_LA_SOLIDARITE = "FEDERATION_DES_ACTEURS_DE_LA_SOLIDARITE"
    FEDERATION_DES_ENTREPRISES_DINSERTION = "FEDERATION_DES_ENTREPRISES_DINSERTION"
    FORCE_FEMMES = "FORCE_FEMMES"
    FRANCE_ACTIVE = "FRANCE_ACTIVE"
    FRANCE_SERVICE = "FRANCE_SERVICE"
    FRENCH_TECH = "FRENCH_TECH"
    GEIQ = "GEIQ"
    GRAND_TEST_COUVEUSE_DENTREPRISE = "GRAND_TEST_COUVEUSE_DENTREPRISE"
    GRANDES_ECOLES_DU_NUMERIQUE = "GRANDES_ECOLES_DU_NUMERIQUE"
    HUP = "HUP"
    INAE = "INAE"
    INITIATIVE_FRANCE = "INITIATIVE_FRANCE"
    KONEXIO = "KONEXIO"
    LA_CRAVATE_SOLIDAIRE = "LA_CRAVATE_SOLIDAIRE"
    LA_RESSOURCERIE = "LA_RESSOURCERIE"
    LES_PREMIERES = "LES_PREMIERES"
    LINKLUSION = "LINKLUSION"
    MAISONS_DE_LEMPLOI = "MAISONS_DE_LEMPLOI"
    MDPH = "MDPH"
    MISSION_LOCALE = "MISSION_LOCALE"
    MOBIN = "MOBIN"
    NQT = "NQT"
    POINT_CONSEIL_BUDGET = "POINT_CONSEIL_BUDGET"
    POINT_JUSTICE = "POINT_JUSTICE"
    POLE_EMPLOI = "POLE_EMPLOI"
    POSITIVE_PLANET = "POSITIVE_PLANET"
    PROXITE = "PROXITE"
    RESEAU_ENTREPRENDRE = "RESEAU_ENTREPRENDRE"
    RESSOURCERIES = "RESSOURCERIES"
    RESTOS_DU_COEUR = "RESTOS_DU_COEUR"
    SCCONSEIL = "SCCONSEIL"
    SECOURS_POPULAIRE = "SECOURS_POPULAIRE"
    SIAO = "SIAO"
    SIMPLON = "SIMPLON"
    SINCA = "SINCA"
    SNC = "SNC"
    SOIXANTE_MILLE_REBONDS = "60000_REBONDS"
    SPORT_DANS_LA_VILLE = "SPORT_DANS_LA_VILLE"
    TOUS_TES_POSSIBLE = "TOUS_TES_POSSIBLE"
    TZCLD = "TZCLD"
    UNAF = "UNAF"
    UNAI = "UNAI"
    UNCCAS = "UNCCAS"
    UNEA = "UNEA"
    UNIS_CITE = "UNIS_CITE"


class Thematique(str, Enum):
    CHOISIR_UN_METIER = "choisir-un-metier"
    CREATION_ACTIVITE = "creation-activite"
    MOBILITE = "mobilite"
    NUMERIQUE = "numerique"
    PREPARER_SA_CANDIDATURE = "preparer-sa-candidature"
    TROUVER_UN_EMPLOI = "trouver-un-emploi"


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
    structure_parente: Optional[str]
    lien_source: Optional[HttpUrl]
    horaires_ouverture: Optional[str]
    accessibilite: Optional[HttpUrl]
    labels_nationaux: Optional[list[LabelNational]]
    labels_autres: Optional[list[str]]
    thematiques: Optional[list[Thematique]]

    class Config:
        extra = Extra.forbid

    @pydantic.root_validator
    def has_pivot_or_reference_to_parent(cls, values: dict) -> dict:
        has_rna = values.get("rna", None) is not None
        has_siret = values.get("siret", None) is not None
        has_reference = values.get("structure_parente", None) is not None
        if not (has_rna or has_siret or has_reference):
            raise ValueError("absence de pivot ou de référence à une structure parente")
        return values


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
