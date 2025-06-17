from datetime import date
from typing import Annotated, Literal, Optional

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.v1 import (
    Frais,
    ModeAccueil,
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
    Public,
    Thematique,
    TypologieService,
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
    prise_rdv: Optional[HttpUrl] = None
    frais: Annotated[
        Optional[Frais],
        Field(
            description="""
                Indique si l’accès au service est payant ou gratuit.

                Si le service comporte des frais, ceux-ci devraient être précisés dans
                le champ `frais_precisions`.
            """,
            examples=[Frais.GRATUIT, Frais.PAYANT],
        ),
    ] = None
    frais_precisions: Annotated[
        Optional[str],
        Field(
            title="Précisions sur les frais",
            description="""
                Précisions sur les éventuels frais pour accéder au service.
            """,
            examples=[
                "10€ pour l’adhésion annuelle",
                "Tarif réduit pour les bénéficiaires du RSA",
            ],
        ),
    ] = None
    publics: Annotated[
        Optional[set[Public]],
        Field(
            title="Publics",
            description="""
            Publics visés par le service.

            Des informations complémentaires peuvent être précisées dans le champ
            `publics_precisions`.
        """,
            examples=[Public.FEMMES, Public.RESIDENTS_QPV_FRR],
            min_length=1,
        ),
    ] = None
    publics_precisions: Annotated[
        Optional[str],
        Field(
            title="Précisions sur les publics",
            description="""
            Précisions sur les publics visés par le service.
        """,
            examples=["Le jeune entre 15 et 18 ans."],
        ),
    ] = None
    conditions_acces: Annotated[
        Optional[str],
        Field(
            description="""
            Conditions d’accès au service.

            Il peut s’agir de prérequis ou de justificatifs à présenter.
        """,
            examples=["Maîtrise de la langue française à l’oral et à l’écrit"],
            title="Conditions d’accès",
        ),
    ] = None
    formulaire_en_ligne: Optional[HttpUrl] = None
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
    zone_eligibilite: Annotated[
        Optional[
            list[
                common.CodeCommune
                | common.CodeEPCI
                | common.CodeRegion
                | common.CodePays
                | Literal["france"]
            ]
        ],
        Field(
            title="Zone d’éligibilité",
            min_length=1,
            description="""
            Zone géographique d’éligibilité du service.

            Contient une liste de codes issus du Code Officiel Géographique maintenu par
            l’INSEE.

            Chaque code dans cette liste peut être un code commune, un code département,
            un code EPCI ou un code pays.

            Si le service est éligible à l’ensemble d’une région, lister les codes des
            departements de cette région.

            Si le service est éligible sur l’ensemble du territoire national, utiliser
            le code `france` (France) ou le code pays `99100`.

            data·inclusion vérifie la validité des codes fournis. Les codes invalides
            sont supprimés de la liste.

            [Le Code Officiel Géographique de l’INSEE](https://www.insee.fr/fr/information/2560452).

            [Outil de recherche des codes](https://www.insee.fr/fr/recherche/recherche-geographique).
        """,  # noqa: E501
            examples=[
                ["france"],
                ["2A", "2B"],
                ["200093201"],
                ["2A", "2B", "200093201"],
            ],
        ),
    ] = None
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
    horaires_accueil: Annotated[
        Optional[str],
        Field(
            description="""
            Horaires d’accueil du public pour ce service.

            Si le champ n’est pas renseigné, les horaires d’accueil de la structure
            peuvent être utilisés.

            Doit être au format OpenStreetMap Opening Hours.

            [Spécification du format OSM Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

            [Outil d’aide à la saisie](https://projets.pavie.info/yohours/).
        """,
            title="Horaires d’accueil du public",
            examples=["Mo-Fr 08:30-12:30; PH off"],
        ),
    ] = None
