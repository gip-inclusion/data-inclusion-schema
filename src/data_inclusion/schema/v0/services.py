from datetime import date
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field

from .frais import Frais
from .modes_accueil import ModeAccueil
from .modes_orientation import (
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
)
from .profils import Profil
from .thematiques import Thematique
from .typologies_de_services import TypologieService
from .zones_de_diffusion import ZoneDiffusionType


class Service(BaseModel):
    # fields
    id: str
    structure_id: str
    source: str
    nom: Annotated[
        str,
        Field(
            description="""
                Nom du service.

                Chaîne de caractères entre 3 et 150 caractères,
                ne se terminant pas par un point.
            """,
            examples=["Atelier insertion et posture professionnelle"],
            min_length=3,
            max_length=150,
        ),
    ]
    presentation_resume: Annotated[Optional[str], Field(max_length=280)] = None
    presentation_detail: Optional[str] = None
    types: Optional[set[TypologieService]] = None
    thematiques: Optional[set[Thematique]] = None
    prise_rdv: Optional[HttpUrl] = None
    frais: Optional[set[Frais]] = None
    frais_autres: Optional[str] = None
    profils: Optional[set[Profil]] = None
    profils_precisions: Optional[str] = None
    pre_requis: Optional[set[str]] = None
    cumulable: Optional[bool] = None
    justificatifs: Optional[set[str]] = None
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
    telephone: Annotated[
        Optional[str],
        Field(
            description="""
                Numéro de téléphone à utiliser pour obtenir des informations
                complémentaires sur le service. Si le mode de mobilisation est
                `telephoner`, peut être utilisé pour mobiliser le service.

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
                le service. Si le mode de mobilisation est `envoyer-un-email`, peut
                être utilisé pour mobiliser le service.

                Doit suivre le format de la RFC 5322.
                Vérification de l’existence du destinataire (envoi d’un courrier
                de notification)

                Si non conforme ou destinataire inexistant, suppression de la valeur.
            """,
            examples=["exemple@inclusion.gouv.fr"],
            default=None,
        ),
    ]
    contact_public: Optional[bool] = None
    date_maj: Annotated[
        date,
        Field(
            description="""
                Date de dernière modification du service chez le producteur de données.
            """,
            examples=["2025-02-14"],
            title="Date de dernière modification",
        ),
    ]
    modes_accueil: Optional[set[ModeAccueil]] = None
    zone_diffusion_type: Optional[ZoneDiffusionType] = None
    zone_diffusion_code: Optional[
        common.CodeCommune
        | common.CodeEPCI
        | common.CodeDepartement
        | common.CodeRegion
    ] = None
    zone_diffusion_nom: Optional[str] = None
    contact_nom_prenom: Optional[str] = None
    page_web: Annotated[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers une page web dédiée au service sur le site web de la
                structure. Ce champ n’est pas destiné à recevoir un lien vers le site
                d’un producteur de donnée.
            """,
            examples=[
                "https://insersol.fr/biclou-atelier-reparation-participatif-solidaire/"
            ],
        ),
    ] = None
    modes_orientation_beneficiaire: Optional[set[ModeOrientationBeneficiaire]] = None
    modes_orientation_beneficiaire_autres: Optional[str] = None
    modes_orientation_accompagnateur: Optional[set[ModeOrientationAccompagnateur]] = (
        None
    )
    modes_orientation_accompagnateur_autres: Optional[str] = None
    volume_horaire_hebdomadaire: Annotated[
        Optional[float],
        Field(
            description="""
                Durée du service en heures sur une semaine.

                L’absence de valeur signifie que le service n’est pas concerné
                (exemple aide financière) ou que l’information n’est pas
                disponible.

                Champ utilisé dans le cadre des 15h-20h d’activité
                hebdomadaire des BRSA.
            """,
            examples=[1],
            ge=0,
        ),
    ] = None
    nombre_semaines: Annotated[
        Optional[int],
        Field(
            description="""
                Nombre de semaines sur lequel dure le service.

                Ne peut pas être inférieur à 1. L’absence de valeur
                signifie que le service n’est pas concerné (exemple aide financière)
                ou que l’information n’est pas disponible.

                Champ utilisé dans le cadre des 15h-20h d’activité hebdomadaire
                des BRSA.
            """,
            examples=[3],
            ge=1,
        ),
    ] = None
