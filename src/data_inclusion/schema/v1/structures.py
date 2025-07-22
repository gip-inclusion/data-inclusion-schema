from datetime import date
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl

from data_inclusion.schema import common
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
    description: Annotated[
        str,
        Field(
            description="""
                Description de la structure.

                Entre 50 et 2000 caractères.
            """,
            examples=[
                """
                    L’association 3027 offre un accès gratuit aux arts, à la culture et
                    au sport pour toutes et tous sans distinction et en priorité aux
                    personnes en situation de précarité et d’isolement.
                """
            ],
            min_length=50,
            max_length=2000,
        ),
    ]
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

    #########################
    ### Champs optionnels ###
    #########################
    siret: Annotated[
        Optional[common.CodeSiret],
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
                complémentaires sur la structure.

                Chaîne de caractères contenant un seul numéro de téléphone,
                de préfèrence au format E.164.
            """,
            examples=["+33123456789"],
            title="Téléphone",
        ),
    ] = None
    courriel: Annotated[
        Optional[EmailStr],
        Field(
            description="""
                Courriel à utiliser pour obtenir des informations complémentaires sur
                la structure.

                Doit suivre le format de la RFC 5322.
            """,
            examples=["exemple@inclusion.gouv.fr"],
        ),
    ] = None
    site_web: Optional[HttpUrl] = None
    horaires_accueil: Annotated[
        Optional[str],
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
        Optional[HttpUrl],
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
        Optional[set[ReseauPorteur]],
        Field(
            title="Réseaux porteurs",
            description="""
                Réseaux, organisations ou administrations portant la structure.
            """,
            examples=[[ReseauPorteur.MISSION_LOCALE]],
        ),
    ] = None
