from datetime import date, datetime
from typing import Annotated, Optional

from pydantic import EmailStr, HttpUrl, StringConstraints

from data_inclusion.schema import common
from data_inclusion.schema.base import BaseModel, Field
from data_inclusion.schema.frais import Frais
from data_inclusion.schema.modes_accueil import ModeAccueil
from data_inclusion.schema.modes_orientation import (
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
)
from data_inclusion.schema.profils import Profil
from data_inclusion.schema.thematiques import Thematique
from data_inclusion.schema.typologies_de_services import TypologieService
from data_inclusion.schema.zones_de_diffusion import ZoneDiffusionType


class Service(BaseModel):
    # fields
    id: Annotated[
        str,
        Field(
            description="""
                Identifiant unique de l'offre de service. Doit être stable et immuable.
            """,
            examples=[
                "04d50659-0000-0000-0000-04d50f6ace57"
            ],
        ),
    ]
    structure_id: Annotated[
        str,
        Field(
            description="""
                Identifiant unique de la structure délivrant l'offre de service. L'id doit exister dans notre table structures.
            """,
            examples=[
                "c3d15659-0000-0000-0000-04d50f6ace57"
            ],
        ),
    ]
    source: Annotated[
        str,
        Field(
            description="""
                Nom du producteur de données dont provient l'offre de service.
            """,
            examples=[
                "action-logement"
            ],
        ),
    ]
    nom: Annotated[
        str,
        Field(
            description="""
                Intitulé de l'offre de service.
            """,
            examples=[
                "Conseil et accompagnement à la création ou la reprise d'entreprise"
            ],
        ),
    ]
    presentation_resume: Annoted[
        Optional[str],
        StringConstraints(max_length=280),
        Field(
            description="""
                Présentation succincte de l'offre de service.
            """,
            examples=[
                "BGE est un réseau associatif présent partout en France. BGE accueille les futurs créateurs d'entreprise et les entrepreneurs en activité pour leur apporter tout l'appui nécessaire à la création ou au développement de leur activité."
            ],
        ),
    ] = None
    presentation_detail: Annoted[
        Optional[str],
        Field(
            description="""
                Présentation détaillée de l'offre de service.
            """
        ),    
    ] = None
    types: Annoted[
        Optional[set[TypologieService]],
        Field(
            description="""
                Typologie de l'offre de service.
            """,
            examples=[
                "Accompagnement"
            ],
        ),
    ] = None
    thematiques: Annoted[
        Optional[set[Thematique]],
        Field(
            description="""
                Thématique abordée par l'offre de service.
            """,
            examples=[
                "Création d'activité"
            ],
        ),
    ] = None
    prise_rdv: Annoted[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers une page web permettant la prise de rendez-vous pour l'offre de service.
            """,
            examples=[
                "https://centresocialduroussillonnais.fr/services-aux-habitants/prendre-rendez-vous-avec-un-cnfs/"
            ],
        ),
    ] = None
    frais: Annoted[
        Optional[set[Frais]],
        Field(
            description="""
                Frais afférents à la mobilisation de l'offre de service.
            """,
            examples=[
                "Gratuit",
                "payant"
            ],
        ),
    ] = None
    frais_autres: Annoted[
        Optional[str],
        Field(
            description="""
                Précisions sur les frais afférents à l'offre de service.
            """,
            examples=[
                "10 euros pour les frais d'inscription"
            ],
        ),
    ] = None
    profils: Annoted[
        Optional[set[Profil]],
        Field(
            description="""
                Publics auxquels s'adresse l'offre de service.
            """,
            examples=[
                "Jeunes",
                "retraités", 
                "femmes",
                "personnes en situation de handicap..."
            ],
        ),
    ] = None
    pre_requis: Annoted[
        Optional[set[str]],
        Field(
            description="""
                Conditions d'accès à l'offre de service.
            """,
            examples=[
                "Maîtriser la lecture et l'écriture",
                "Être entrepreneur",
                "Être agé de 16 à 26 ans"
            ],
        ),
    ] = None
    cumulable: Annoted[
        Optional[bool],
        Field(
            description="""
                Indique si l'offre de service est cumulable avec d'autres services.
            """,
        ),
    ] = None
    justificatifs: Annoted[
        Optional[set[str]],
        Field(
            description="""
                Documents à présenter pour accéder à l'offre de service.
            """,
            examples=[
                "Pièce d'identité en cours de validité",
                "RIB",
                "CV"
            ],
        ),
    ] = None
    formulaire_en_ligne: Annoted[
        Optional[HttpUrl],
        Field(
           description="""
                Lien vers une page web permettant de mobiliser l'offre de service.
            """,
            examples=[
                "https://www.tarn.fr/au-quotidien/senior/demander-lallocation-personnalisee-dautonomie-apa?tx_solr%5Bq%5D=APA"
            ], 
        ),
    ] = None
    commune: Annoted[
        Optional[str],
        Field(
            description="""
                Nom de la ville où est délivrée l'offre de service.
            """,
            examples=[
                "Paris"
            ],
        ),
    ] = None
    code_postal: Annoted[
        Optional[common.CodePostal],
        Field(
            description="""
                Code postal de la commune où est délivrée l'offre de service.
            """,
            examples=[
                "75001"
            ],
        ),
    ] = None
    code_insee: Annoted[
        Optional[common.CodeCommune],
        Field(
            description="""
                Code INSEE de la commune où est délivrée l'offre de service.
            """,
            examples=[
                "75101"
            ],
        ),
    ] = None
    adresse: Annoted[
        Optional[str],
        Field(
            description="""
                Numéro et voie de l'adresse où est délivrée l'offre de service.
            """,
            examples=[
                "35 rue Paradis"
            ],
        ),
    ] = None
    complement_adresse: Annoted[
        Optional[str],
        Field(
            description="""
                Informations postales supplémentaires.
            """,
            examples=[
                "Centre d'activités Le Folgoët"
            ],
        ),
    ] = None
    longitude: Annoted[
        Optional[float],
        Field(
            description="""
                Longitude de l'adresse où est délivrée l'offre de service.
            """
        ),
    ] = None
    latitude: Annoted[
        Optional[float],
        Field(
            description="""
                Latitude de l'adresse où est délivrée l'offre de service.
            """
        ),
    ] = None
    recurrence: Annoted[
        Optional[str],
        Field(
            description="""
                Indique si l'offre de service est récurrente, c'est-à-dire proposée en continu.
            """
        ),
    ] = None
    date_creation: Annoted[
        Optional[date],
        Field(
            description="""
                Date de création de l'offre de service chez le producteur de données.
            """
        ),
    ] = None
    date_suspension: Annoted[
        Optional[date],
        Field(
            description="""
                Date à laquelle l'offre de service n'est plus délivrée ou est inactive. 
            """
        ),
    ] = None
    lien_source: Annoted[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers la page web de l'offre de service sur le site web du producteur de données. Différent du champ page_web qui renvoie sur le site web de la structure.
            """,
            examples=[
                "https://dora.inclusion.beta.gouv.fr/services/departement-de-la-sa-mtgb-accompagnement-dans--bbns"
            ],
        ),
    ] = None
    telephone: Annoted[
        Optional[str],
        Field(
            description="""
                 Numéro de téléphone de la personne référente de l'offre de service.
            """
        ),
    ] = None
    courriel: Annoted[
        Optional[EmailStr],
        Field(
            description="""
                 Adresse email de la personne référente de l'offre de service.
            """
        ),
    ] = None
    contact_public: Annoted[
        Optional[bool],
        Field(
            description="""
                 Indique si les coordonnées de la personne référente de l'offre de service sont publiques.
            """
        ),
    ] = None
    date_maj: Annoted[
        Optional[date | datetime],
        Field(
            description="""
                 Date à laquelle l'offre de service a été mise à jour.
            """
        ),
    ] = None
    modes_accueil: Annoted[
        Optional[set[ModeAccueil]],
        Field(
            description="""
                Modalités du déroulement de l'offre de service.
            """,
            examples=[
                "à distance",
                "présentiel"
            ],
        ),
    ] = None
    zone_diffusion_type: Annoted[
        Optional[ZoneDiffusionType],
        Field(
            description="""
                Périmètre de mobilisation de l'offre de service.
            """,
            examples=[
                "commune : le service n'est mobilisable que dans sa commune",
                "département : le service est mobilisable dans tout le département."
            ],
        ),
    ] = None
    zone_diffusion_code: Optional[
        common.CodeCommune
        | common.CodeEPCI
        | common.CodeDepartement
        | common.CodeRegion
    ] = None
    zone_diffusion_nom: Optional[str] = None
    contact_nom_prenom: Annoted[
        Optional[str],
        Field(
            description="""
                Nom et prénom de la personne référente de l'offre de service.
            """,
            examples=[
                "John Doe"
            ],
        ),
    ] = None
    page_web: Annotated[
        Optional[HttpUrl],
        Field(
            description="""
                Lien vers la page web de l'offre de service sur le site web de la
                structure. Ce champ n'est pas destiné à recevoir un lien vers le site
                d'un producteur de donnée.
            """,
            examples=[
                "https://insersol.fr/biclou-atelier-reparation-participatif-solidaire/"
            ],
        ),
    ] = None
    modes_orientation_beneficiaire: Annoted[
        Optional[set[ModeOrientationBeneficiaire]],
        Field(
            description="""
                Modalités pour qu'un bénéficiaire mobilise directement une offre service.
            """,
            examples=[
                "se présenter",
                "envoyer un mail"
            ],
        ),
    ] = None
    modes_orientation_beneficiaire_autres: Annoted[
        Optional[str],
        Field(
           description="""
                Précisions sur la mobilisation d'une offre de service par un bénéficaire.
            """,
            examples=[
                "sur rendez-vous uniquement"
            ], 
        ),
    ] = None
    modes_orientation_accompagnateur: Annoted[
        Optional[set[ModeOrientationAccompagnateur]],
        Field(
            description="""
                Modalités pour qu'un professionnel oriente un bénéficiaire vers une offre de service.
            """,
            examples=[
                "compléter le formulaire d'adhésion",
                "envoyer un mail"
            ],
        ),
    ] = None
    modes_orientation_accompagnateur_autres: Annoted[
        Optional[str],
        Field(
           description="""
                Précisions sur les modalités d'orientation vers une offre de service par un professionnel.
            """,
            examples=[
                "sur inscription uniquement"
            ], 
        ),
    ] = None
