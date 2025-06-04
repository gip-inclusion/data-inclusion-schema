from datetime import date
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.v1 import (
    Frais,
    ModeAccueil,
    ModeMobilisation,
    PersonneMobilisatrice,
    Profil,
    Thematique,
    TypologieService,
    ZoneDiffusionType,
)


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
    description: Annotated[
        str,
        Field(
            description="""
                Description du service.

                Entre 50 et 2000 caractères.

                Ce champ est pris en compte dans le calcul du score de qualité.
            """,
            examples=[
                """Cet atelier-conseil vous permet d’identifier les compétences à
                développer pour atteindre vos objectifs d’évolution professionnelle et à
                découvrir les différentes modalités de formation.

                Durée d’une journée et inscription via votre espace France Travail."""
            ],
            min_length=50,
            max_length=2000,
        ),
    ]
    types: Optional[set[TypologieService]] = None
    thematiques: Optional[set[Thematique]] = None
    frais: Optional[set[Frais]] = None
    frais_autres: Optional[str] = None
    profils: Optional[set[Profil]] = None
    profils_precisions: Optional[str] = None
    pre_requis: Optional[set[str]] = None
    justificatifs: Optional[set[str]] = None
    commune: Optional[str] = None
    code_postal: Optional[common.CodePostal] = None
    code_insee: Optional[common.CodeCommune] = None
    adresse: Optional[str] = None
    complement_adresse: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
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
    lien_mobilisation: Annotated[
        Optional[HttpUrl],
        Field(
            description="""
                Lien pour accéder ou mobiliser l’offre de service.
            """,
            examples=["https://www.actionlogement.fr/demande-cfi"],
        ),
    ] = None
    modes_mobilisation: Annotated[
        Optional[set[ModeMobilisation]],
        Field(
            description="""
                Modes de mobilisation de l’offre de service.
                Les valeurs proviennent d’un référentiel disponible
                sur notre documentation.
            """,
            examples=[
                "envoyer-un-courriel",
            ],
            min_items=1,
        ),
    ] = None
    mobilisable_par: Annotated[
        Optional[set[PersonneMobilisatrice]],
        Field(
            description="""
                Indique qui peut mobiliser le service : usagers, professionnels ou les
                deux.
            """,
            examples=[
                ["professionnels"],
                ["usagers"],
            ],
            min_items=1,
        ),
    ] = None
    mobilisation_precisions: Annotated[
        Optional[str],
        Field(
            description="""
                Précisions sur les modes de mobilisation du service.
            """,
            examples=[
                """La demande est à faire depuis l’espace personnel
                du demandeur d’emploi, rubrique « mes aides »,
                formulaire spécifique « Aide à la mobilité »."""
            ],
        ),
    ] = None
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
