from datetime import date
from typing import Annotated, Literal

from pydantic import EmailStr, HttpUrl, field_validator

from data_inclusion.schema import common, validation
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.v1 import (
    Frais,
    ModeAccueil,
    ModeMobilisation,
    PersonneMobilisatrice,
    Public,
    Thematique,
    TypeService,
)


class Service(BaseModel):
    #####################
    ### Champs requis ###
    #####################
    source: Annotated[
        str,
        Field(
            description="""
            Identifiant du producteur original de la donnée.
            """,
            examples=["emplois-de-linclusion", "france-travail", "dora"],
        ),
    ]
    structure_id: Annotated[
        str,
        Field(
            description="""
            Identifiant unique de la structure rattachée au service.
            """,
            title="ID structure",
            examples=["dora--42", "cd35--mjc-13-grandjour"],
        ),
    ]
    id: Annotated[
        str,
        Field(
            description="""
            Identifiant unique du service, obtenu par une combinaison de l’identifiant
            du producteur et de l’identifiant du service (fourni par le producteur).
            """,
            examples=[
                "emplois-de-linclusion--17",
                "france-travail--ccas-provence-alpes-cote-dazur-2024-01-01",
                "dora--AidantsConnect:2024-47BXY",
            ],
        ),
    ]
    nom: Annotated[
        str,
        Field(
            description="""
                Nom du service.

                Chaîne de caractères entre 3 et 150 caractères. Idéalement ne se termine
                pas par un point (sauf "etc.").
            """,
            examples=["Atelier insertion et posture professionnelle"],
            min_length=3,
            max_length=150,
        ),
    ]

    @field_validator("nom")
    @validation.avertissement
    def nom_ne_se_termine_pas_par_un_point(cls, value: str) -> str:
        if value.endswith(".") and not value.endswith("etc."):
            raise ValueError("Le nom du service ne doit pas se terminer par un point.")
        return value

    description: Annotated[
        str,
        Field(
            description="""
                Description du service.

                Idéalement entre 200 et 2000 caractères. Privilégier des phrases courtes
                et un langage simple.
            """,
            examples=[
                """
                    Cet atelier-conseil vous permet d’identifier les compétences à
                    développer pour atteindre vos objectifs d’évolution professionnelle
                    et à découvrir les différentes modalités de formation.

                    Durée d’une journée et inscription via votre espace France Travail.
                """
            ],
            min_length=5,
            max_length=10000,
        ),
    ]
    lien_source: Annotated[
        HttpUrl | None,
        Field(
            description="""
                Lien pour accéder au service sur le site web du producteur.
            """,
            examples=[
                "https://dora.inclusion.beta.gouv.fr/services/ass-pour-droit-a-l-i-nhes"
            ],
        ),
    ] = None
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

    @field_validator("date_maj")
    def date_maj_valide(cls, value: date) -> date:
        if value < date(2000, 1, 1):
            raise ValueError(
                "La date de dernière modification doit être au 21e siècle."
            )
        if value > date.today():
            raise ValueError(
                "La date de dernière modification ne peut pas être dans le futur."
            )
        return value

    #########################
    ### Champs optionnels ###
    #########################
    type: Annotated[
        TypeService | None,
        Field(
            description="""
            Type de service.
            """,
            examples=[TypeService.ACCOMPAGNEMENT],
        ),
    ] = None
    thematiques: Annotated[
        set[Thematique] | None,
        Field(
            description="""
                Thématiques adressées par le service.
            """,
            examples=[
                [Thematique.NUMERIQUE__ACQUERIR_UN_EQUIPEMENT],
                [
                    Thematique.SANTE__CONSTITUER_UN_DOSSIER_MDPH_INVALIDITE,
                    Thematique.LOGEMENT_HEBERGEMENT__SE_MAINTENIR_DANS_LE_LOGEMENT,
                ],
            ],
        ),
    ] = None
    frais: Annotated[
        Frais | None,
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
        str | None,
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
        set[Public] | None,
        Field(
            title="Publics",
            description="""
            Publics visés par le service.

            Un bénéficiaire est éligible s’il appartient à (au moins) un des publics
            spécifiés.

            Les services sans publics spécifiques doivent contenir uniquement la valeur
            `tous-publics`. Celle-ci ne peut pas être utilisée avec d’autres valeurs.

            Des informations complémentaires peuvent être précisées dans le champ
            `publics_precisions`.
        """,
            min_length=1,
            examples=[
                [Public.FEMMES],
                [Public.RESIDENTS_QPV_FRR],
                [Public.TOUS_PUBLICS],
            ],
        ),
    ] = None

    @field_validator("publics")
    def tous_publics(cls, value: list[Public] | None) -> list[Public] | None:
        if value is not None and Public.TOUS_PUBLICS in value and len(value) > 1:
            raise ValueError(
                "`tous-publics` ne peut pas être utilisé avec d’autres valeurs."
            )
        return value

    publics_precisions: Annotated[
        str | None,
        Field(
            title="Précisions sur les publics",
            description="""
            Précisions sur les publics visés par le service.
        """,
            examples=["Le jeune entre 15 et 18 ans."],
        ),
    ] = None
    conditions_acces: Annotated[
        str | None,
        Field(
            description="""
            Conditions d’accès au service.

            Il peut s’agir de prérequis ou de justificatifs à présenter.
        """,
            examples=["Maîtrise de la langue française à l’oral et à l’écrit"],
            title="Conditions d’accès",
        ),
    ] = None
    commune: str | None = None
    code_postal: common.CodePostal | None = None
    code_insee: common.CodeCommune | None = None
    adresse: str | None = None
    complement_adresse: str | None = None
    longitude: float | None = None
    latitude: float | None = None
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
            title="Téléphone",
        ),
    ] = None
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
        ),
    ] = None
    modes_accueil: set[ModeAccueil] | None = None
    zone_eligibilite: Annotated[
        list[
            common.CodeCommune
            | common.CodeDepartement
            | common.CodeEPCI
            | common.CodePays
            | Literal["france"]
        ]
        | None,
        Field(
            title="Zone d’éligibilité",
            min_length=1,
            description="""
            Zone géographique d’éligibilité du service.

            Contient une liste de codes issus du [Code Officiel Géographique](https://www.insee.fr/fr/information/2560452)
            maintenu par l’INSEE.

            Chaque code dans cette liste peut être un code commune, un code département,
            un code EPCI ou un code pays.

            Si le service est éligible à l’ensemble d’une région, lister les codes des
            departements de cette région.

            Si le service est éligible sur l’ensemble du territoire national, utiliser
            le code `france` (France) ou le code pays `99100`.

            data·inclusion vérifie la validité des codes fournis. Les codes invalides
            sont supprimés de la liste.

            [Outil de recherche des codes](https://www.insee.fr/fr/recherche/recherche-geographique)
        """,  # noqa: E501
            examples=[
                ["75056"],
                ["2A", "2B"],
                ["200093201"],
                ["2A", "2B", "200093201"],
                ["france"],
            ],
        ),
    ] = None
    contact_nom_prenom: str | None = None
    lien_mobilisation: Annotated[
        HttpUrl | None,
        Field(
            description="""
                Lien pour accéder ou mobiliser l’offre de service.
            """,
            examples=["https://www.actionlogement.fr/demande-cfi"],
        ),
    ] = None
    modes_mobilisation: Annotated[
        set[ModeMobilisation] | None,
        Field(
            description="""
                Modes de mobilisation de l’offre de service.
            """,
            examples=[
                ["envoyer-un-courriel"],
            ],
            min_length=1,
        ),
    ] = None
    mobilisable_par: Annotated[
        set[PersonneMobilisatrice] | None,
        Field(
            description="""
                Indique qui peut mobiliser le service : usagers, professionnels ou les
                deux.
            """,
            examples=[
                ["professionnels"],
                ["usagers"],
            ],
            min_length=1,
        ),
    ] = None
    mobilisation_precisions: Annotated[
        str | None,
        Field(
            description="""
                Précisions sur les modes de mobilisation du service.
            """,
            examples=[
                """
                    La demande est à faire depuis l’espace personnel
                    du demandeur d’emploi, rubrique « mes aides »,
                    formulaire spécifique « Aide à la mobilité ».
                """
            ],
        ),
    ] = None
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
    horaires_accueil: Annotated[
        str | None,
        Field(
            description="""
            Horaires d’accueil du public pour ce service.

            Si le champ n’est pas renseigné, les horaires d’accueil de la structure
            peuvent être utilisés.

            Doit être au format [OpenStreetMap Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

            [Outil d’aide à la saisie](https://projets.pavie.info/yohours/).
        """,
            title="Horaires d’accueil du public",
            examples=["Mo-Fr 08:30-12:30; PH off"],
        ),
    ] = None
