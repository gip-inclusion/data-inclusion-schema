from datetime import date
from typing import Annotated

from pydantic import EmailStr, HttpUrl, field_validator

from data_inclusion.schema import common, validation
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.v1 import ReseauPorteur


class Structure(BaseModel):
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
    id: Annotated[
        str,
        Field(
            description="""
            Identifiant unique de la structure, obtenu par une combinaison de
            l’identifiant producteur et de l’identifiant de la structure
            (fourni par le producteur).
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
                Nom de la structure.

                Chaîne de caractères entre 3 et 150 caractères,
                ne se terminant pas par un point.
            """,
            examples=["Centre social Le Tournesol"],
            min_length=3,
            max_length=150,
        ),
    ]

    @field_validator("nom")
    @validation.avertissement
    def nom_valide(cls, value: str) -> str:
        if value.endswith(".") and not value.endswith("etc."):
            raise ValueError(
                "Le nom de la structure ne doit pas se terminer par un point."
            )
        return value

    date_maj: Annotated[
        date,
        Field(
            description="""
                Date de dernière modification de la
                structure chez le producteur de données.
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
    description: Annotated[
        str | None,
        Field(
            description="""
                Description de la structure.
            """,
            examples=[
                """
                    L’association 3027 offre un accès gratuit aux arts, à la culture et
                    au sport pour toutes et tous sans distinction et en priorité aux
                    personnes en situation de précarité et d’isolement.
                """
            ],
            min_length=5,
            max_length=10000,
        ),
    ] = None
    lien_source: Annotated[
        HttpUrl | None,
        Field(
            description="""
                Lien pour accéder à la structure sur le site web du producteur.
            """,
            examples=[
                "https://dora.inclusion.beta.gouv.fr/structures/ass-pour-droit-a-l-i-nhes"
            ],
        ),
    ] = None
    siret: Annotated[
        common.CodeSiret | None,
        Field(
            title="Numéro SIRET",
            description="""
                Un numéro SIRET associé à la structure.

                Lorsque la structure correspond à un établissement dans la base sirene,
                le numéro SIRET doit être celui de cet établissement.

                Si la structure ne correspond pas strictement à un établissement de la
                base sirene, le numéro SIRET du siège social peut être utilisé.

                data·inclusion vérifie régulièrement la validité des numéros SIRET
                fournis. Les SIRETs inconnus sont retirés. Lorsque l’établissement
                associé à un SIRET a fait l’objet d’une succession (d’après la base
                sirene), data·inclusion remplace ce SIRET par celui de l’établissement
                successeur. Lorsque l’établissement associé est déclaré fermé et sans
                successeur, data·inclusion retire la structure.
            """,
            examples=["13003013300016"],
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
                complémentaires sur la structure.

                Chaîne de caractères contenant un seul numéro de téléphone,
                de préfèrence au format E.164.
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
                la structure.

                Doit suivre le format de la RFC 5322.
            """,
            examples=["exemple@inclusion.gouv.fr"],
        ),
    ] = None
    site_web: HttpUrl | None = None
    horaires_accueil: Annotated[
        str | None,
        Field(
            description="""
            Horaires d’accueil du public par la structure.

            Un service peut avoir un horaire d’accueil différent. Se référer aux
            horaires des services.

            Doit être au format [OpenStreetMap Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

            [Outil d’aide à la saisie](https://projets.pavie.info/yohours/).
        """,  # noqa: E501
            title="Horaires d’accueil du public",
            examples=["Mo-Fr 08:30-12:30; PH off"],
        ),
    ] = None
    accessibilite_lieu: Annotated[
        HttpUrl | None,
        Field(
            title="Accessibilité du lieu",
            description="""
            Lien vers la page Accesslibre référençant le niveau d’accessibilité de
            la structure.

            Le format attendu est donc un lien vers [Accesslibre](https://acceslibre.beta.gouv.fr/).
            """,
            examples=[
                "https://acceslibre.beta.gouv.fr/app/17-la-greve-sur-mignon/a/mairie/erp/mairie-la-greve-sur-mignon/",  # noqa: E501
            ],
        ),
    ] = None
    reseaux_porteurs: Annotated[
        set[ReseauPorteur] | None,
        Field(
            title="Réseaux porteurs",
            description="""
                Réseaux, organisations ou administrations portant la structure.
            """,
            examples=[[ReseauPorteur.MISSION_LOCALE]],
        ),
    ] = None
