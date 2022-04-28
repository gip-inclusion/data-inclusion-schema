from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr, Extra, schema_json_of, EmailStr, HttpUrl


class Typologie(str, Enum):
    ACI = "ACI"
    ACIPHC = "ACIPHC"
    AFPA = "AFPA"
    AI = "AI"
    ASE = "ASE"
    ASSO = "ASSO"
    CADA = "CADA"
    CAF = "CAF"
    CAP_EMPLOI = "CAP_EMPLOI"
    CAVA = "CAVA"
    CC = "CC"
    CCAS = "CCAS"
    CD = "CD"
    CHRS = "CHRS"
    CHU = "CHU"
    CIAS = "CIAS"
    CIDFF = "CIDFF"
    CPH = "CPH"
    CS = "CS"
    CT = "CT"
    DEETS = "DEETS"
    DIPLP = "DIPLP"
    EA = "EA"
    EATT = "EATT"
    EI = "EI"
    EITI = "EITI"
    EPCI = "EPCI"
    ETTI = "ETTI"
    FAIS = "FAIS"
    GEIQ = "GEIQ"
    ML = "ML"
    MQ = "MQ"
    MSA = "MSA"
    MSAP = "MSAP"
    MUNI = "MUNI"
    OACAS = "OACAS"
    OF = "OF"
    PE = "PE"
    PIJ_BIJ = "PIJ_BIJ"
    PIMMS = "PIMMS"
    PJJ = "PJJ"
    PLIE = "PLIE"
    SCP = "SCP"
    SPIP = "SPIP"
    UDAF = "UDAF"
    ASSO_CHOMEUR = "ASSO_CHOMEUR"
    Autre = "Autre"
    PREF = "PREF"
    REG = "REG"
    DEPT = "DEPT"
    TIERS_LIEUX = "TIERS_LIEUX"
    CAARUD = "CAARUD"
    CSAPA = "CSAPA"
    E2C = "E2C"
    EPIDE = "EPIDE"
    HUDA = "HUDA"
    ODC = "ODC"
    OIL = "OIL"
    OPCS = "OPCS"
    PENSION = "PENSION"
    PREVENTION = "PREVENTION"
    RS_FJT = "RS_FJT"


class Structure(BaseModel):
    id: str
    siret: constr(min_length=14, max_length=14, regex=r"^\d{14}$")
    rna: Optional[constr(min_length=10, max_length=10, regex=r"^W\d{9}$")]
    nom: str
    commune: str
    code_postal: constr(min_length=5, max_length=5, regex=r"^\d{5}$")
    code_insee: constr(min_length=5, max_length=5)
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
    id_antenne: Optional[str]

    class Config:
        extra = Extra.forbid


if __name__ == "__main__":
    print(
        schema_json_of(
            Structure,
            title="",
            indent=2,
        )
    )
