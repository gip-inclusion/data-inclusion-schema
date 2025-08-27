from datetime import date
from typing import Annotated

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
    presentation_resume: Annotated[str | None, Field(max_length=280)] = None
    presentation_detail: str | None = None
    types: set[TypologieService] | None = None
    thematiques: set[Thematique] | None = None
    prise_rdv: HttpUrl | None = None
    frais: set[Frais] | None = None
    frais_autres: str | None = None
    profils: set[Profil] | None = None
    profils_precisions: str | None = None
    pre_requis: set[str] | None = None
    cumulable: bool | None = None
    justificatifs: set[str] | None = None
    formulaire_en_ligne: HttpUrl | None = None
    commune: str | None = None
    code_postal: common.CodePostal | None = None
    code_insee: common.CodeCommune | None = None
    adresse: str | None = None
    complement_adresse: str | None = None
    longitude: float | None = None
    latitude: float | None = None
    recurrence: str | None = None
    date_creation: date | None = None
    date_suspension: date | None = None
    lien_source: HttpUrl | None = None
    telephone: Annotated[
        str | None,
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
        EmailStr | None,
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
    contact_public: bool | None = None
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
    modes_accueil: set[ModeAccueil] | None = None
    zone_diffusion_type: ZoneDiffusionType | None = None
    zone_diffusion_code: None | (
        common.CodeCommune
        | common.CodeEPCI
        | common.CodeDepartement
        | common.CodeRegion
    ) = None
    zone_diffusion_nom: str | None = None
    contact_nom_prenom: str | None = None
    page_web: Annotated[
        HttpUrl | None,
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
    modes_orientation_beneficiaire: set[ModeOrientationBeneficiaire] | None = None
    modes_orientation_beneficiaire_autres: str | None = None
    modes_orientation_accompagnateur: set[ModeOrientationAccompagnateur] | None = None
    modes_orientation_accompagnateur_autres: str | None = None
    volume_horaire_hebdomadaire: Annotated[
        float | None,
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
        int | None,
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
