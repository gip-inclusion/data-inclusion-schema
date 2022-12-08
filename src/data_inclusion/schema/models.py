from datetime import date, datetime
from typing import Optional

import pydantic
from pydantic import BaseModel, EmailStr, Extra, HttpUrl, constr

from data_inclusion.schema.base import EnhancedEnum


class Typologie(EnhancedEnum):
    ACI = (
        "ACI",
        "Structures porteuses d’ateliers et chantiers d’insertion (ACI)",
        None,
    )
    ACIPHC = (
        "ACIPHC",
        "SIAE — Atelier chantier d’insertion premières heures en chantier",
        None,
    )
    AFPA = (
        "AFPA",
        "Agence nationale pour la formation professionnelle des adultes (AFPA)",
        None,
    )
    AI = (
        "AI",
        "Associations intermédiaires (AI)",
        None,
    )
    ASE = (
        "ASE",
        "Aide sociale à l’enfance (ASE)",
        None,
    )
    ASSO = (
        "ASSO",
        "Associations",
        None,
    )
    ASSO_CHOMEUR = (
        "ASSO_CHOMEUR",
        "Associations de chômeurs",
        None,
    )
    Autre = (
        "Autre",
        "Autre",
        None,
    )
    BIB = (
        "BIB",
        "Bibliothèque / Médiathèque",
        None,
    )
    CAARUD = (
        "CAARUD",
        (
            "CAARUD - Centre d’accueil et d’accompagnement à la réduction de risques "
            "pour usagers de drogues"
        ),
        None,
    )
    CADA = (
        "CADA",
        "Centres d’accueil de demandeurs d’asile (CADA)",
        None,
    )
    CAF = (
        "CAF",
        "Caisses d’allocation familiale (CAF)",
        None,
    )
    CAP_EMPLOI = (
        "CAP_EMPLOI",
        "Cap Emploi",
        None,
    )
    CAVA = (
        "CAVA",
        "Centres d’adaptation à la vie active (CAVA)",
        None,
    )
    CC = (
        "CC",
        "Communautés de Commune",
        None,
    )
    CCAS = (
        "CCAS",
        "Centres communaux d’action sociale (CCAS)",
        None,
    )
    CCONS = (
        "CCONS",
        "Chambres consulaires (CCI, CMA, CA)",
        None,
    )
    CD = (
        "CD",
        "Conseils Départementaux (CD)",
        None,
    )
    CHRS = (
        "CHRS",
        "Centres d’hébergement et de réinsertion sociale (CHRS)",
        None,
    )
    CHU = (
        "CHU",
        "Centres d’hébergement d’urgence (CHU)",
        None,
    )
    CIAS = (
        "CIAS",
        "Centres intercommunaux d’action sociale (CIAS)",
        None,
    )
    CIDFF = (
        "CIDFF",
        "Centres d’information sur les droits des femmes et des familles (CIDFF)",
        None,
    )
    CITMET = (
        "CITMET",
        "Cité des métiers",
        None,
    )
    CPH = (
        "CPH",
        "Centres provisoires d’hébergement (CPH)",
        None,
    )
    CS = (
        "CS",
        "Centre social",
        None,
    )
    CSAPA = (
        "CSAPA",
        "CSAPA - Centre de soins, d’accompagnement et de prévention en addictologie",
        None,
    )
    DEETS = (
        "DEETS",
        "Directions de l’Economie, de l’Emploi, du Travail et des Solidarités (DEETS)",
        None,
    )
    DEPT = (
        "DEPT",
        "Services sociaux du Conseil départemental",
        None,
    )
    DIPLP = (
        "DIPLP",
        (
            "Délégation interministérielles à la prévention et à la lutte contre la "
            "pauvreté"
        ),
        None,
    )
    E2C = (
        "E2C",
        "E2C - École de la deuxième chance",
        None,
    )
    EA = (
        "EA",
        "Entreprise adaptée (EA)",
        None,
    )
    EATT = (
        "EATT",
        "Entreprise Adaptée (EATT)",
        None,
    )
    EI = (
        "EI",
        "Entreprises d’insertion (EI)",
        None,
    )
    EITI = (
        "EITI",
        "Entreprises d’insertion par le travail indépendant (EITI)",
        None,
    )
    EPCI = (
        "EPCI",
        "Intercommunalité (EPCI)",
        None,
    )
    EPIDE = (
        "EPIDE",
        "EPIDE - Établissement pour l’insertion dans l’emploi",
        None,
    )
    ESS = (
        "ESS",
        "Entreprise de l’Économie Sociale et Solidaire",
        None,
    )
    ETTI = (
        "ETTI",
        "Entreprises de travail temporaire d’insertion (ETTI)",
        None,
    )
    FAIS = (
        "FAIS",
        "Fédérations d’acteurs de l’insertion et de la solidarité",
        None,
    )
    GEIQ = (
        "GEIQ",
        "Groupements d’employeurs pour l’insertion et la qualification (GEIQ)",
        None,
    )
    HUDA = (
        "HUDA",
        "HUDA - Hébergement d’urgence pour demandeurs d’asile",
        None,
    )
    MDE = (
        "MDE",
        "Maison de l’emploi",
        None,
    )
    MDEF = (
        "MDEF",
        "Maison de l’emploi et de la formation",
        None,
    )
    MDPH = (
        "MDPH",
        "Maison Départementale des Personnes Handicapées",
        None,
    )
    MDS = (
        "MDS",
        "Maison Départementale des Solidarités",
        None,
    )
    MJC = (
        "MJC",
        "Maison des jeunes et de la culture",
        None,
    )
    ML = (
        "ML",
        "Mission Locale",
        None,
    )
    MQ = (
        "MQ",
        "Maison de quartier",
        None,
    )
    MSA = (
        "MSA",
        "Mutualité Sociale Agricole",
        None,
    )
    MUNI = (
        "MUNI",
        "Municipalités",
        None,
    )
    OACAS = (
        "OACAS",
        (
            "Structures agréées Organisme d’accueil communautaire et d’activité "
            "solidaire (OACAS)"
        ),
        None,
    )
    ODC = (
        "ODC",
        "Organisation délégataire d’un CD",
        None,
    )
    OF = (
        "OF",
        "Organisme de formations",
        None,
    )
    OIL = (
        "OIL",
        "Opérateur d’intermédiation locative",
        None,
    )
    OPCS = (
        "OPCS",
        "Organisation porteuse de la clause sociale",
        None,
    )
    PAD = (
        "PAD",
        "Point d’Accès au Droit",
        None,
    )
    PE = (
        "PE",
        "Pôle emploi",
        None,
    )
    PENSION = (
        "PENSION",
        "Pension de famille / résidence accueil",
        None,
    )
    PIJ_BIJ = (
        "PIJ_BIJ",
        "Points et bureaux information jeunesse (PIJ/BIJ)",
        None,
    )
    PIMMS = (
        "PIMMS",
        "Point Information Médiation Multi Services (PIMMS)",
        None,
    )
    PJJ = (
        "PJJ",
        "Protection judiciaire de la jeunesse (PJJ)",
        None,
    )
    PLIE = (
        "PLIE",
        "Plans locaux pour l’insertion et l’emploi (PLIE)",
        None,
    )
    PREF = (
        "PREF",
        "Préfecture, Sous-Préfecture",
        None,
    )
    PREVENTION = (
        "PREVENTION",
        "Service ou club de prévention",
        None,
    )
    REG = (
        "REG",
        "Région",
        None,
    )
    RFS = (
        "RFS",
        "Réseau France Services",
        None,
    )
    RS_FJT = (
        "RS_FJT",
        "Résidence sociale / FJT - Foyer de Jeunes Travailleurs",
        None,
    )
    SCP = (
        "SCP",
        "Services et clubs de prévention",
        None,
    )
    SPIP = (
        "SPIP",
        "Services pénitentiaires d’insertion et de probation (SPIP)",
        None,
    )
    TIERS_LIEUX = (
        "TIERS_LIEUX",
        "Tiers lieu & coworking",
        None,
    )
    UDAF = (
        "UDAF",
        "Union Départementale d’Aide aux Familles (UDAF)",
        None,
    )


class LabelNational(EnhancedEnum):
    SOIXANTE_MILLE_REBONDS = (
        "60000-rebonds",
        "60 000 rebonds",
        None,
    )
    ACTION_LOGEMENT = (
        "action-logement",
        "Action logement",
        None,
    )
    ADIE = (
        "adie",
        "Adie",
        None,
    )
    AFPA = (
        "afpa",
        "AFPA",
        None,
    )
    AGEFIPH = (
        "agefiph",
        "AGEFIPH",
        None,
    )
    AIDANTS_CONNECT = (
        "aidants-connect",
        "Aidants Connect",
        None,
    )
    ALLIANCE_VILLES_EMPLOI = (
        "alliance-villes-emploi",
        "Alliance villes emploi",
        None,
    )
    ANLCI = (
        "anlci",
        "ANLCI",
        None,
    )
    APEC = (
        "apec",
        "APEC",
        None,
    )
    APELS = (
        "apels",
        "APELS Agence Pour l’Education par Le Sport",
        None,
    )
    APPRENTIS_DAUTEUIL = (
        "apprentis-dauteuil",
        "Apprentis d’Auteuil",
        None,
    )
    APTIC = (
        "aptic",
        "APTIC",
        None,
    )
    BANQUES_ALIMENTAIRES = (
        "banques-alimentaires",
        "Banques alimentaires",
        None,
    )
    BGE = (
        "bge",
        "BGE",
        None,
    )
    CAF = (
        "caf",
        "CAF",
        None,
    )
    CAMPUS_CONNECTE = (
        "campus-connecte",
        "Campus connecté",
        None,
    )
    CCI = (
        "cci",
        "CCI",
        None,
    )
    CHANTIER_ECOLE = (
        "chantier-ecole",
        "Chantier école",
        None,
    )
    CHEOPS = (
        "cheops",
        "Cheops",
        None,
    )
    CIDFF = (
        "cidff",
        "CIDFF",
        None,
    )
    CNAM = (
        "cnam",
        "CNAM",
        None,
    )
    CONSEILLER_NUMERIQUE = (
        "conseiller-numerique",
        "Conseiller numérique",
        None,
    )
    COORACE = (
        "coorace",
        "Coorace",
        None,
    )
    CREPI = (
        "crepi",
        "CREPI",
        None,
    )
    CRESUS = (
        "cresus",
        "Crésus",
        None,
    )
    CROIX_ROUGE = (
        "croix-rouge",
        "Croix rouge",
        None,
    )
    DIHAL = (
        "dihal",
        "DIHAL",
        None,
    )
    DUO_FOR_A_JOB = (
        "duo-for-a-job",
        "Duo for a job",
        None,
    )
    ECOLES_DE_LA_DEUXIEME_CHANCE = (
        "ecoles-de-la-deuxieme-chance",
        "Ecoles de la deuxième chance",
        None,
    )
    EGEE = (
        "egee",
        "EGEE",
        None,
    )
    EMMAUS = (
        "emmaus",
        "Emmaus",
        None,
    )
    ENVIE = (
        "envie",
        "Envie",
        None,
    )
    EPIDE = (
        "epide",
        "EPIDE",
        None,
    )
    ESPACE_EMPLOI_AGRIC_ARRCO = (
        "espace-emploi-agric-arrco",
        "Espace Emploi Agirc Arrco",
        None,
    )
    FABRIQUE_DE_TERRITOIRE = (
        "fabrique-de-territoire",
        "Fabrique de Territoire",
        None,
    )
    FACE = (
        "face",
        "Fondation FACE",
        None,
    )
    FEDE_PRO_FEM = (
        "fede-pro-fem",
        "Federation Professionnelle Pour les Femmes",
        None,
    )
    FEDERATION_DES_ACTEURS_DE_LA_SOLIDARITE = (
        "federation-des-acteurs-de-la-solidarite",
        "Fédération des acteurs de la solidarité",
        None,
    )
    FEDERATION_DES_ENTREPRISES_DINSERTION = (
        "federation-des-entreprises-dinsertion",
        "Fédération des entreprises d’insertion",
        None,
    )
    FORCE_FEMMES = (
        "force-femmes",
        "Force Femmes",
        None,
    )
    FRANCE_ACTIVE = (
        "france-active",
        "France Active",
        None,
    )
    FRANCE_SERVICE = (
        "france-service",
        "France service",
        None,
    )
    FRENCH_TECH = (
        "french-tech",
        "French Tech",
        None,
    )
    GEIQ = (
        "geiq",
        "GEIQ",
        None,
    )
    GRANDES_ECOLES_DU_NUMERIQUE = (
        "grandes-ecoles-du-numerique",
        "Grand Test Couveuse d’entreprise",
        None,
    )
    GRAND_TEST_COUVEUSE_DENTREPRISE = (
        "grand-test-couveuse-dentreprise",
        "Grandes écoles du numérique",
        None,
    )
    HUP = (
        "hup",
        "H’UP",
        None,
    )
    INAE = (
        "inae",
        "INAE",
        None,
    )
    INITIATIVE_FRANCE = (
        "initiative-france",
        "Initiative France",
        None,
    )
    KONEXIO = (
        "konexio",
        "Konexio",
        None,
    )
    LA_CRAVATE_SOLIDAIRE = (
        "la-cravate-solidaire",
        "La Cravate Solidaire",
        None,
    )
    LA_RESSOURCERIE = (
        "la-ressourcerie",
        "La ressourcerie",
        None,
    )
    LES_PREMIERES = (
        "les-premieres",
        "Les Premières",
        None,
    )
    LINKLUSION = (
        "linklusion",
        "Linklusion",
        None,
    )
    MAISONS_DE_LEMPLOI = (
        "maisons-de-lemploi",
        "Maisons de l’Emploi",
        None,
    )
    MDPH = (
        "mdph",
        "MDPH",
        None,
    )
    MISSION_LOCALE = (
        "mission-locale",
        "Mission Locale",
        None,
    )
    MOBIN = (
        "mobin",
        "Mobin",
        None,
    )
    NQT = (
        "nqt",
        "NQT",
        None,
    )
    POINT_CONSEIL_BUDGET = (
        "point-conseil-budget",
        "Point conseil budget",
        None,
    )
    POINT_JUSTICE = (
        "point-justice",
        "Points Justice",
        None,
    )
    POLE_EMPLOI = (
        "pole-emploi",
        "Pôle emploi",
        None,
    )
    POSITIVE_PLANET = (
        "positive-planet",
        "Positive Planet",
        None,
    )
    PROXITE = (
        "proxite",
        "Proxité",
        None,
    )
    RESEAU_ENTREPRENDRE = (
        "reseau-entreprendre",
        "Réseau Entreprendre",
        None,
    )
    RESSOURCERIES = (
        "ressourceries",
        "Ressourceries",
        None,
    )
    RESTOS_DU_COEUR = (
        "restos-du-coeur",
        "Restos du coeur",
        None,
    )
    SCCONSEIL = (
        "scconseil",
        "SC Conseil",
        None,
    )
    SECOURS_POPULAIRE = (
        "secours-populaire",
        "Secours populaire",
        None,
    )
    SIAO = (
        "siao",
        "SIAO",
        None,
    )
    SIMPLON = (
        "simplon",
        "Simplon",
        None,
    )
    SINCA = (
        "sinca",
        "SINGA",
        None,
    )
    SNC = (
        "snc",
        "SNC - Solidarité Nouvelle Face au Chômage",
        None,
    )
    SPORT_DANS_LA_VILLE = (
        "sport-dans-la-ville",
        "Sport Dans La Ville",
        None,
    )
    TOUS_TES_POSSIBLE = (
        "tous-tes-possible",
        "Tous Tes Possibles",
        None,
    )
    TZCLD = (
        "tzcld",
        "TZCLD - Territoire Zero Chomeur Longue Durée",
        None,
    )
    UNAF = (
        "unaf",
        "Union nationale de l’aide aux familles",
        None,
    )
    UNAI = (
        "unai",
        "UNAI",
        None,
    )
    UNCCAS = (
        "unccas",
        "Union nationale des centres communaux d’action sociale",
        None,
    )
    UNEA = (
        "unea",
        "UNEA",
        None,
    )
    UNIS_CITE = (
        "unis-cite",
        "Unis-Cité",
        None,
    )


class Thematique(EnhancedEnum):
    ACCES_AUX_DROITS_ET_CITOYENNETE = (
        "acces-aux-droits-et-citoyennete",
        "Accès aux droits & citoyenneté",
        None,
    )
    ACCES_AUX_DROITS_ET_CITOYENNETE__ACCOMPAGNEMENT_DEMARCHES_ADMINISTRATIVES = (
        (
            "acces-aux-droits-et-citoyennete"
            "--accompagnement-dans-les-demarches-administratives"
        ),
        "Accompagnement dans les démarches administratives",
        None,
    )
    ACCES_AUX_DROITS_ET_CITOYENNETE__ACCOMPAGNEMENT_JURIDIQUE = (
        "acces-aux-droits-et-citoyennete--accompagnement-juridique",
        "Accompagnement juridique",
        None,
    )
    ACCES_AUX_DROITS_ET_CITOYENNETE__CONNAITRE_SES_DROITS = (
        "acces-aux-droits-et-citoyennete--connaitre-ses-droits",
        "Connaitre ses droits",
        None,
    )
    ACCES_AUX_DROITS_ET_CITOYENNETE__DEMANDEURS_DASILE_ET_NATURALISATION = (
        "acces-aux-droits-et-citoyennete--demandeurs-dasile-et-naturalisation",
        "Demandeurs d’asile et naturalisation",
        None,
    )
    ACCES_AUX_DROITS_ET_CITOYENNETE__FACILITER_LACTION_CITOYENNE = (
        "acces-aux-droits-et-citoyennete--faciliter-laction-citoyenne",
        "Faciliter l’action citoyenne",
        None,
    )
    ACCES_AUX_DROITS_ET_CITOYENNETE__DEVELOPPEMENT_DURABLE = (
        "acces-aux-droits-et-citoyennete--developpement-durable",
        "Développement durable",
        None,
    )

    ACCOMPAGNEMENT_SOCIO_PRO_PERSONNALISE = (
        "accompagnement-social-et-professionnel-personnalise",
        "Accompagnement social et professionnel personnalisé",
        None,
    )
    ACCOMPAGNEMENT_SOCIO_PRO_PERSONNALISE__DECROCHAGE_SCOLAIRE = (
        "accompagnement-social-et-professionnel-personnalise--decrochage-scolaire",
        "Décrochage scolaire",
        None,
    )
    ACCOMPAGNEMENT_SOCIO_PRO_PERSONNALISE__DEFINITION_DU_PROJET_PROFESSIONNEL = (
        (
            "accompagnement-social-et-professionnel-personnalise--"
            "definition-du-projet-professionnel"
        ),
        "Définition du projet professionnel",
        None,
    )
    ACCOMPAGNEMENT_SOCIO_PRO_PERSONNALISE__PARCOURS_D_INSERTION_SOCIOPROFESSIONNEL = (
        (
            "accompagnement-social-et-professionnel-personnalise--"
            "parcours-d-insertion-socioprofessionnel"
        ),
        "Parcours d’insertion socio-professionnel",
        None,
    )

    CHOISIR_UN_METIER = (
        "choisir-un-metier",
        "Choisir un métier",
        None,
    )
    CHOISIR_UN_METIER__IDENTIFIER_SES_POINTS_FORTS_ET_SES_COMPETENCES = (
        "choisir-un-metier--identifier-ses-points-forts-et-ses-competences",
        "Identifier ses points forts et ses compétences",
        None,
    )
    CHOISIR_UN_METIER__CONNAITRE_LES_OPPORTUNITES_DEMPLOI = (
        "choisir-un-metier--connaitre-les-opportunites-demploi",
        "Connaître les opportunités d’emploi",
        None,
    )
    CHOISIR_UN_METIER__DECOUVRIR_UN_METIER_OU_UN_SECTEUR_DACTIVITE = (
        "choisir-un-metier--decouvrir-un-metier-ou-un-secteur-dactivite",
        "Découvrir un métier ou un secteur d’activité",
        None,
    )
    CHOISIR_UN_METIER__CONFIRMER_SON_CHOIX_DE_METIER = (
        "choisir-un-metier--confirmer-son-choix-de-metier",
        "Confirmer son choix de métier",
        None,
    )

    CREATION_ACTIVITE = (
        "creation-activite",
        "Création d’activité",
        None,
    )
    CREATION_ACTIVITE__DEFINIR_SON_PROJET_DE_CREATION_DENTREPRISE = (
        "creation-activite--definir-son-projet-de-creation-dentreprise",
        "Définir son projet de création d’entreprise",
        None,
    )
    CREATION_ACTIVITE__DEVELOPPER_SON_ENTREPRISE = (
        "creation-activite--developper-son-entreprise",
        "Développer son entreprise",
        None,
    )
    CREATION_ACTIVITE__STRUCTURER_SON_PROJET_DE_CREATION_DENTREPRISE = (
        "creation-activite--structurer-son-projet-de-creation-dentreprise",
        "Structurer son projet de création d’entreprise",
        None,
    )
    CREATION_ACTIVITE__RESEAUTAGE_POUR_CREATEURS_DENTREPRISE = (
        "creation-activite--reseautage-pour-createurs-dentreprise",
        "Réseautage pour créateurs d’entreprise",
        None,
    )
    CREATION_ACTIVITE__FINANCER_SON_PROJET = (
        "creation-activite--financer-son-projet",
        "Financer son projet",
        None,
    )

    EQUIPEMENT_ET_ALIMENTATION = (
        "equipement-et-alimentation",
        "Equipement et alimentation",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__ACCES_A_DU_MATERIEL_INFORMATIQUE = (
        "equipement-et-alimentation--acces-a-du-materiel-informatique",
        "Accès à du matériel informatique",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__ACCES_A_UN_TELEPHONE_ET_UN_ABONNEMENT = (
        "equipement-et-alimentation--acces-a-un-telephone-et-un-abonnement",
        "Accès à un téléphone et un abonnement",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__ALIMENTATION = (
        "equipement-et-alimentation--alimentation",
        "Alimentation",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__ELECTROMENAGER = (
        "equipement-et-alimentation--electromenager",
        "Electroménager",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__HABILLEMENT = (
        "equipement-et-alimentation--habillement",
        "Habillement",
        None,
    )

    FAMILLE = (
        "famille",
        "Famille",
        None,
    )
    FAMILLE__INFORMATION_ET_ACCOMPAGNEMENT_DES_PARENTS = (
        "famille--information-et-accompagnement-des-parents",
        "Information et accompagnement des parents",
        None,
    )
    FAMILLE__GARDE_DENFANTS = (
        "famille--garde-denfants",
        "Garde d’enfants",
        None,
    )
    FAMILLE__JEUNES_SANS_SOUTIEN_FAMILIAL = (
        "famille--jeunes-sans-soutien-familial",
        "Jeunes sans soutien familial",
        None,
    )
    FAMILLE__SOUTIEN_AUX_FAMILLES = (
        "famille--soutien-aux-familles",
        "Soutien aux familles",
        None,
    )
    FAMILLE__VIOLENCES_INTRAFAMILIALES = (
        "famille--violences-intrafamiliales",
        "Violences intrafamiliales",
        None,
    )
    FAMILLE__ACCOMPAGNEMENT_FEMME_ENCEINTE_BEBE_JEUNE_ENFANT = (
        "famille--accompagnement-femme-enceinte-bebe-jeune-enfant",
        "Accompagnement femme enceinte, bébé, jeune enfant",
        None,
    )
    FAMILLE__SOUTIEN_A_LA_PARENTALITE = (
        "famille--soutien-a-la-parentalite",
        "Soutien à la parentalité",
        None,
    )

    GESTION_FINANCIERE = (
        "gestion-financiere",
        "Gestion financière",
        None,
    )
    GESTION_FINANCIERE__ACCOMPAGNEMENT_AUX_PERSONNES_EN_DIFFICULTES_FINANCIERES = (
        "gestion-financiere--accompagnement-aux-personnes-en-difficultes-financieres",
        "Accompagnement aux personnes en difficultés financières",
        None,
    )
    GESTION_FINANCIERE__APPRENDRE_A_GERER_SON_BUDGET = (
        "gestion-financiere--apprendre-a-gerer-son-budget",
        "Apprendre à gérer son budget",
        None,
    )
    GESTION_FINANCIERE__PREVENTION_ET_GESTION_DU_SURENDETTEMENT = (
        "gestion-financiere--prevention-et-gestion-du-surendettement",
        "Prévention et gestion du surendettement",
        None,
    )
    GESTION_FINANCIERE__CREATION_ET_UTILISATION_DUN_COMPTE_BANCAIRE = (
        "gestion-financiere--creation-et-utilisation-dun-compte-bancaire",
        "Création et utilisation d’un compte bancaire",
        None,
    )
    GESTION_FINANCIERE__ACCES_AU_MICRO_CREDIT = (
        "gestion-financiere--acces-au-micro-credit",
        "Accès au micro-crédit",
        None,
    )
    GESTION_FINANCIERE__OBTENIR_UNE_AIDE_ALIMENTAIRE = (
        "gestion-financiere--obtenir-une-aide-alimentaire",
        "Obtenir une aide alimentaire",
        None,
    )
    GESTION_FINANCIERE__BENEFICIER_DAIDES_FINANCIERES = (
        "gestion-financiere--beneficier-daides-financieres",
        "Bénéficier d’aides financières",
        None,
    )

    HANDICAP = (
        "handicap",
        "Handicap",
        None,
    )
    HANDICAP__ACCOMPAGNEMENT_PAR_UNE_STRUCTURE_SPECIALISEE = (
        "handicap--accompagnement-par-une-structure-specialisee",
        "Accompagnement par une structure spécialisée",
        None,
    )
    HANDICAP__ADAPTATION_AU_POSTE_DE_TRAVAIL = (
        "handicap--adaptation-au-poste-de-travail",
        "Adaptation au poste de travail",
        None,
    )
    HANDICAP__ADAPTER_SON_LOGEMENT = (
        "handicap--adapter-son-logement",
        "Adapter son logement",
        None,
    )
    HANDICAP__CONNAISSANCE_DES_DROITS_DES_TRAVAILLEURS = (
        "handicap--connaissance-des-droits-des-travailleurs",
        "Connaissance des droits des travailleurs",
        None,
    )
    HANDICAP__FAIRE_RECONNAITRE_UN_HANDICAP = (
        "handicap--faire-reconnaitre-un-handicap",
        "Faire reconnaitre un handicap",
        None,
    )
    HANDICAP__FAVORISER_LE_RETOUR_ET_LE_MAINTIEN_DANS_LEMPLOI = (
        "handicap--favoriser-le-retour-et-le-maintien-dans-lemploi",
        "Favoriser le retour et le maintien dans l’emploi",
        None,
    )
    HANDICAP__MOBILITE_DES_PERSONNES_EN_SITUATION_DE_HANDICAP = (
        "handicap--mobilite-des-personnes-en-situation-de-handicap",
        "Mobilité des personnes en situation de handicap",
        None,
    )
    HANDICAP__GERER_LE_DEPART_A_LA_RETRAITE_DES_PERSONNES_EN_SITUATION_DE_HANDICAP = (
        (
            "handicap--"
            "gerer-le-depart-a-la-retraite-des-personnes-en-situation-de-handicap"
        ),
        "Gérer le départ à la retraite des personnes en situation de handicap",
        None,
    )

    LOGEMENT_HEBERGEMENT = (
        "logement-hebergement",
        "Logement et hébergement",
        None,
    )
    LOGEMENT_HEBERGEMENT__ETRE_ACCOMPAGNE_POUR_SE_LOGER = (
        "logement-hebergement--etre-accompagne-pour-se-loger",
        "Etre accompagné(e) pour se loger",
        None,
    )
    LOGEMENT_HEBERGEMENT__BESOIN_DADAPTER_MON_LOGEMENT = (
        "logement-hebergement--besoin-dadapter-mon-logement",
        "Besoin d’adapter mon logement",
        None,
    )
    LOGEMENT_HEBERGEMENT__DEMENAGEMENT = (
        "logement-hebergement--demenagement",
        "Déménagement",
        None,
    )
    LOGEMENT_HEBERGEMENT__MAL_LOGES_SANS_LOGIS = (
        "logement-hebergement--mal-loges-sans-logis",
        "Mal logé/sans logis",
        None,
    )
    LOGEMENT_HEBERGEMENT__PROBLEME_AVEC_SON_LOGEMENT = (
        "logement-hebergement--probleme-avec-son-logement",
        "Problème avec son logement",
        None,
    )
    LOGEMENT_HEBERGEMENT__REPRENDRE_UN_EMPLOI_OU_UNE_FORMATION = (
        "logement-hebergement--reprendre-un-emploi-ou-une-formation",
        "Reprendre un emploi ou une formation",
        None,
    )
    LOGEMENT_HEBERGEMENT__CONNAISSANCE_DE_SES_DROITS_ET_INTERLOCUTEURS = (
        "logement-hebergement--connaissance-de-ses-droits-et-interlocuteurs",
        "Connaissance de ses droits et interlocuteurs",
        None,
    )
    LOGEMENT_HEBERGEMENT__GERER_SON_BUDGET = (
        "logement-hebergement--gerer-son-budget",
        "Gérer son budget",
        None,
    )

    MOBILITE = (
        "mobilite",
        "Mobilité",
        None,
    )
    MOBILITE__ETRE_ACCOMPAGNE_DANS_SON_PARCOURS_MOBILITE = (
        "mobilite--etre-accompagne-dans-son-parcours-mobilite",
        "Etre accompagné(e) dans son parcours mobilité",
        None,
    )
    MOBILITE__ENTRETENIR_REPARER_SON_VEHICULE = (
        "mobilite--entretenir-reparer-son-vehicule",
        "Entretenir ou réparer son véhicule",
        None,
    )
    MOBILITE__LOUER_UN_VEHICULE = (
        "mobilite--louer-un-vehicule",
        "Louer un véhicule (voiture, vélo, scooter..)",
        None,
    )
    MOBILITE__ACHETER_UN_VEHICULE_MOTORISE = (
        "mobilite--acheter-un-vehicule-motorise",
        "Acheter un véhicule motorisé",
        None,
    )
    MOBILITE__PREPARER_SON_PERMIS_DE_CONDUIRE_SE_REENTRAINER_A_LA_CONDUITE = (
        "mobilite--preparer-son-permis-de-conduire-se-reentrainer-a-la-conduite",
        "Préparer son permis de conduire, se réentrainer à la conduite",
        None,
    )
    MOBILITE__AIDES_A_LA_REPRISE_DEMPLOI_OU_A_LA_FORMATION = (
        "mobilite--aides-a-la-reprise-demploi-ou-a-la-formation",
        "Aides à la reprise d’emploi ou à la formation",
        None,
    )
    MOBILITE__COMPRENDRE_ET_UTILISER_LES_TRANSPORTS_EN_COMMUN = (
        "mobilite--comprendre-et-utiliser-les-transports-en-commun",
        "Comprendre et utiliser les transports en commun",
        None,
    )
    MOBILITE__APPRENDRE_A_UTILISER_UN_DEUX_ROUES = (
        "mobilite--apprendre-a-utiliser-un-deux-roues",
        "Apprendre à utiliser un deux roues",
        None,
    )
    MOBILITE__FINANCER_MON_PROJET_MOBILITE = (
        "mobilite--financer-mon-projet-mobilite",
        "Financer mon projet mobilité",
        None,
    )
    MOBILITE__ACHETER_UN_VELO = (
        "mobilite--acheter-un-velo",
        "Acheter un vélo",
        None,
    )

    NUMERIQUE = (
        "numerique",
        "Numérique",
        None,
    )
    NUMERIQUE__DEVENIR_AUTONOME_DANS_LES_DEMARCHES_ADMINISTRATIVES = (
        "numerique--devenir-autonome-dans-les-demarches-administratives",
        "Devenir autonome dans les démarches administratives",
        None,
    )
    NUMERIQUE__REALISER_DES_DEMARCHES_ADMINISTRATIVES_AVEC_UN_ACCOMPAGNEMENT = (
        "numerique--realiser-des-demarches-administratives-avec-un-accompagnement",
        "Réaliser des démarches administratives avec un accompagnement",
        None,
    )
    NUMERIQUE__PRENDRE_EN_MAIN_UN_SMARTPHONE_OU_UNE_TABLETTE = (
        "numerique--prendre-en-main-un-smartphone-ou-une-tablette",
        "Prendre en main un smartphone ou une tablette",
        None,
    )
    NUMERIQUE__PRENDRE_EN_MAIN_UN_ORDINATEUR = (
        "numerique--prendre-en-main-un-ordinateur",
        "Prendre en main un ordinateur",
        None,
    )
    NUMERIQUE__UTILISER_LE_NUMERIQUE_AU_QUOTIDIEN = (
        "numerique--utiliser-le-numerique-au-quotidien",
        "Utiliser le numérique au quotidien",
        None,
    )
    NUMERIQUE__APPROFONDIR_MA_CULTURE_NUMERIQUE = (
        "numerique--approfondir-ma-culture-numerique",
        "Approfondir ma culture numérique",
        None,
    )
    NUMERIQUE__FAVORISER_MON_INSERTION_PROFESSIONNELLE = (
        "numerique--favoriser-mon-insertion-professionnelle",
        "Favoriser mon insertion professionnelle",
        None,
    )
    NUMERIQUE__ACCEDER_A_UNE_CONNEXION_INTERNET = (
        "numerique--acceder-a-une-connexion-internet",
        "Accéder à une connexion internet",
        None,
    )
    NUMERIQUE__ACCEDER_A_DU_MATERIEL = (
        "numerique--acceder-a-du-materiel",
        "Accéder à du matériel",
        None,
    )
    NUMERIQUE__S_EQUIPER_EN_MATERIEL_INFORMATIQUE = (
        "numerique--s-equiper-en-materiel-informatique",
        "S’équiper en matériel informatique",
        None,
    )
    NUMERIQUE__CREER_ET_DEVELOPPER_MON_ENTREPRISE = (
        "numerique--creer-et-developper-mon-entreprise",
        "Créer et développer mon entreprise",
        None,
    )
    NUMERIQUE__CREER_AVEC_LE_NUMERIQUE = (
        "numerique--creer-avec-le-numerique",
        "Créer avec le numérique",
        None,
    )
    NUMERIQUE__ACCOMPAGNER_LES_DEMARCHES_DE_SANTE = (
        "numerique--accompagner-les-demarches-de-sante",
        "Accompagner les démarches de santé",
        None,
    )
    NUMERIQUE__PROMOUVOIR_LA_CITOYENNETE_NUMERIQUE = (
        "numerique--promouvoir-la-citoyennete-numerique",
        "Promouvoir la citoyenneté numérique",
        None,
    )
    NUMERIQUE__SOUTENIR_LA_PARENTALITE_ET_L_EDUCATION_AVEC_LE_NUMERIQUE = (
        "numerique--soutenir-la-parentalite-et-l-education-avec-le-numerique",
        "Soutenir la parentalité et l’éducation avec le numérique",
        None,
    )

    PREPARER_SA_CANDIDATURE = (
        "preparer-sa-candidature",
        "Préparer sa candidature",
        None,
    )
    PREPARER_SA_CANDIDATURE__VALORISER_SES_COMPETENCES = (
        "preparer-sa-candidature--valoriser-ses-competences",
        "Valoriser ses compétences",
        None,
    )
    PREPARER_SA_CANDIDATURE__REALISER_UN_CV_ET_OU_UNE_LETTRE_DE_MOTIVATION = (
        "preparer-sa-candidature--realiser-un-cv-et-ou-une-lettre-de-motivation",
        "Réaliser un CV et/ou une lettre de motivation",
        None,
    )
    PREPARER_SA_CANDIDATURE__DEVELOPPER_SON_RESEAU = (
        "preparer-sa-candidature--developper-son-reseau",
        "Développer son réseau",
        None,
    )
    PREPARER_SA_CANDIDATURE__ORGANISER_SES_DEMARCHES_DE_RECHERCHE_DEMPLOI = (
        "preparer-sa-candidature--organiser-ses-demarches-de-recherche-demploi",
        "Organiser ses démarches de recherche d’emploi",
        None,
    )

    REMOBILISATION = (
        "remobilisation",
        "Remobilisation",
        None,
    )
    REMOBILISATION__BIEN_ETRE = (
        "remobilisation--bien-etre",
        "Bien être",
        None,
    )
    REMOBILISATION__IDENTIFIER_SES_COMPETENCES_ET_APTITUDES = (
        "remobilisation--identifier-ses-competences-et-aptitudes",
        "Identifier ses compétences et aptitudes",
        None,
    )
    REMOBILISATION__LIEN_SOCIAL = (
        "remobilisation--lien-social",
        "Lien social",
        None,
    )
    REMOBILISATION__RESTAURER_SA_CONFIANCE_SON_IMAGE_DE_SOI = (
        "remobilisation--restaurer-sa-confiance-son-image-de-soi",
        "Restaurer sa confiance, son image de soi",
        None,
    )
    REMOBILISATION__PRESSION_SOCIALE = (
        "remobilisation--pression-sociale",
        "Pression sociale",
        None,
    )
    REMOBILISATION__DISCRIMINATION = (
        "remobilisation--discrimination",
        "Discrimination",
        None,
    )
    REMOBILISATION__DECOUVRIR_SON_POTENTIEL_VIA_LE_SPORT_ET_LA_CULTURE = (
        "remobilisation--decouvrir-son-potentiel-via-le-sport-et-la-culture",
        "Découvrir son potentiel via le sport et la culture",
        None,
    )
    REMOBILISATION__PARTICIPER_A_DES_ACTIONS_SOLIDAIRES_OU_DE_BÉNÉVOLAT = (
        "remobilisation--participer-a-des-actions-solidaires-ou-de-benevolat",
        "Participer à des actions solidaires ou de bénévolat",
        None,
    )

    SANTE = (
        "sante",
        "Santé",
        None,
    )
    SANTE__FAIRE_FACE_A_UNE_SITUATION_DADDICTION = (
        "sante--faire-face-a-une-situation-daddiction",
        "Faire face à une situation d’addiction",
        None,
    )
    SANTE__BIEN_ETRE_PSYCHOLOGIQUE = (
        "sante--bien-etre-psychologique",
        "Bien être psychologique",
        None,
    )
    SANTE__OBTENIR_LA_PRISE_EN_CHARGE_DE_FRAIS_MEDICAUX = (
        "sante--obtenir-la-prise-en-charge-de-frais-medicaux",
        "Obtenir la prise en charge de frais médicaux",
        None,
    )
    SANTE__SE_SOIGNER_ET_PRÉVENIR_LA_MALADIE = (
        "sante--se-soigner-et-prevenir-la-maladie",
        "Se soigner et prévenir la maladie",
        None,
    )
    SANTE__ACCOMPAGNEMENT_DE_LA_FEMME_ENCEINTE_DU_BEBE_ET_DU_JEUNE_ENFANT = (
        "sante--accompagnement-de-la-femme-enceinte-du-bebe-et-du-jeune-enfant",
        "Accompagnement de la femme enceinte, du bébé et du jeune enfant",
        None,
    )
    SANTE__PREVENTION_ET_ACCES_AUX_SOINS = (
        "sante--prevention-et-acces-aux-soins",
        (
            "Prévention et accès aux soins "
            "(vaccination, éducation à la santé, lutte contre la tuberculose…)."
        ),
        None,
    )
    SANTE__VIE_RELATIONNELLE_ET_AFFECTIVE = (
        "sante--vie-relationnelle-et-affective",
        "Vie relationnelle et affective, dépistage et prévention des IST/VIH…",
        None,
    )
    SANTE__ACCOMPAGNER_LES_TRAUMATISMES = (
        "sante--accompagner-les-traumatismes",
        "Accompagner les traumatismes",
        None,
    )
    SANTE__ACCES_AUX_SOINS = (
        "sante--acces-aux-soins",
        "Accès aux soins",
        None,
    )
    SANTE__DIAGNOSTIC_ET_ACCOMPAGNEMENT_A_LEMPLOYABILITE = (
        "sante--diagnostic-et-accompagnement-a-lemployabilite",
        "Diagnostic et accompagnement à l’employabailité",
        None,
    )

    SE_FORMER = (
        "se-former",
        "Se former",
        None,
    )
    SE_FORMER__TROUVER_SA_FORMATION = (
        "se-former--trouver-sa-formation",
        "Trouver sa formation",
        None,
    )
    SE_FORMER__MONTER_SON_DOSSIER_DE_FORMATION = (
        "se-former--monter-son-dossier-de-formation",
        "Monter son dossier de formation",
        None,
    )
    SE_FORMER__UTILISER_LE_NUMÉRIQUE = (
        "se-former--utiliser-le-numerique",
        "Utiliser le numérique",
        None,
    )

    SOUVRIR_A_L_INTERNATIONAL = (
        "souvrir-a-linternational",
        "S’ouvrir à l’international",
        None,
    )
    SOUVRIR_A_L_INTERNATIONAL__CONNAITRE_LES_OPPORTUNITES_DEMPLOI_A_LETRANGER = (
        "souvrir-a-linternational--connaitre-les-opportunites-demploi-a-letranger",
        "Connaître les opportunités d’emploi à l’étranger",
        None,
    )
    SOUVRIR_A_L_INTERNATIONAL__SINFORMER_SUR_LES_AIDES_POUR_TRAVAILLER_A_LETRANGER = (
        "souvrir-a-linternational--sinformer-sur-les-aides-pour-travailler-a-letranger",
        "S’informer sur les aides pour travailler à l’étranger",
        None,
    )
    SOUVRIR_A_L_INTERNATIONAL__SORGANISER_SUITE_A_SON_RETOUR_EN_FRANCE = (
        "souvrir-a-linternational--sorganiser-suite-a-son-retour-en-france",
        "S’organiser suite à son retour en France",
        None,
    )

    TROUVER_UN_EMPLOI = (
        "trouver-un-emploi",
        "Trouver un emploi",
        None,
    )
    TROUVER_UN_EMPLOI__REPONDRE_A_DES_OFFRES_DEMPLOI = (
        "trouver-un-emploi--repondre-a-des-offres-demploi",
        "Répondre à des offres d’emploi",
        None,
    )
    TROUVER_UN_EMPLOI__FAIRE_DES_CANDIDATURES_SPONTANEES = (
        "trouver-un-emploi--faire-des-candidatures-spontanees",
        "Faire des candidatures spontanées",
        None,
    )
    TROUVER_UN_EMPLOI__SUIVRE_SES_CANDIDATURES_ET_RELANCER_LES_EMPLOYEURS = (
        "trouver-un-emploi--suivre-ses-candidatures-et-relancer-les-employeurs",
        "Suivre ses candidatures et relancer les employeurs",
        None,
    )
    TROUVER_UN_EMPLOI__CONVAINCRE_UN_RECRUTEUR_EN_ENTRETIEN = (
        "trouver-un-emploi--convaincre-un-recruteur-en-entretien",
        "Convaincre un recruteur en entretien",
        None,
    )


class TypologieService(EnhancedEnum):
    ACCOMPAGNEMENT = (
        "accompagnement",
        "Accompagnement",
        "Etre accompagné·e dans ses démarches ou son retour à l’emploi durable",
    )
    ACCUEIL = (
        "accueil",
        "Accueil",
        """
            Lieux d’écoute et d’évaluation des besoins de la personne qui se présente
            afin de la guider vers le ou les organismes les plus susceptibles de
            répondre à ses besoins
        """,
    )
    AIDE_FINANCIERE = (
        "aide-financiere",
        "Aide financière",
        """
            Prise en charge financière, aide ou rémunération visant à aider une
            personne à accéder à un service
        """,
    )
    AIDE_MATERIELLE = (
        "aide-materielle",
        "Aide materielle",
        "Accéder à du matériel, voiture, vélo, ordinateur, alimentation",
    )
    ATELIER = (
        "atelier",
        "Atelier",
        "Etre accompagné·e dans sa montée en compétence sur un sujet spécifique",
    )
    FORMATION = (
        "formation",
        "Formation",
        "Formation dispensée par des professionnels pour les bénéficiaires",
    )
    INFORMATION = (
        "information",
        "Information",
        "Premier niveau d’information apporté par des professionnels du secteur",
    )
    NUMÉRIQUE = (
        "numerique",
        "Service numérique",
        "Service en ligne qui renvoi vers un site dédié",
    )
    AUTONOMIE = (
        "autonomie",
        "En autonomie",
        "Réaliser des démarches en toute autonomie",
    )
    DELEGATION = (
        "delegation",
        "Délégation",
        "Une personne fait les démarches à ma place.",
    )
    FINANCEMENT = (
        "financement",
        "Financement ",
        "Crédit solidaire, prêts à taux zéro pour le financement d’un projet",
    )


class Frais(EnhancedEnum):
    GRATUIT = (
        "gratuit",
        "Gratuit",
        "Je peux accéder gratuitement au lieu et à ses services",
    )
    GRATUIT_SOUS_CONDITIONS = (
        "gratuit-sous-conditions",
        "Gratuit sous conditions",
        """
            La gratuité est conditionnée à des critères (situation familiale,
            convention avec un organisme social…)
        """,
    )
    PAYANT = (
        "payant",
        "Payant",
        "L’accès au lieu et/ou à ses services est payant",
    )
    ADHESION = (
        "adhesion",
        "Adhésion",
        "L’accès au lieu et/ou à ses services nécessite d’y adhérer",
    )
    PASS_NUMERIQUE = (
        "pass-numerique",
        "Accepte le pass numérique",
        "Il est possible d’utiliser un Pass numérique pour accéder au lieu",
    )


class Profil(EnhancedEnum):
    SENIORS_65 = (
        "seniors-65",
        "Seniors (+ 65 ans)",
        None,
    )
    FAMILLES_ENFANTS = (
        "familles-enfants",
        "Familles/enfants",
        None,
    )
    ADULTES = (
        "adultes",
        "Adultes",
        None,
    )
    JEUNES_16_26 = (
        "jeunes-16-26",
        "Jeunes (16-26 ans)",
        None,
    )
    PUBLIC_LANGUES_ETRANGERES = (
        "public-langues-etrangeres",
        "Public langues étrangères",
        None,
    )
    DEFICIENCE_VISUELLE = (
        "deficience-visuelle",
        "Déficience visuelle",
        None,
    )
    SURDITE = (
        "surdite",
        "Surdité",
        None,
    )
    HANDICAPS_PSYCHIQUES = (
        "handicaps-psychiques",
        (
            "Handicaps psychiques : troubles psychiatriques donnant lieu à des"
            " atteintes comportementales"
        ),
        None,
    )
    HANDICAPS_MENTAUX = (
        "handicaps-mentaux",
        "Handicaps mentaux : déficiences limitant les activités d’une personne",
        None,
    )
    FEMMES = (
        "femmes",
        "Femmes",
        "Le lieu propose des accompagnements réservés aux femmes.",
    )
    PERSONNES_EN_SITUATION_ILLETTRISME = (
        "personnes-en-situation-illettrisme",
        "Personnes en situation d’illettrisme",
        None,
    )


class Service(BaseModel):
    id: str
    structure_id: Optional[str]
    source: str
    nom: str
    presentation_resume: Optional[constr(max_length=280)]
    types: Optional[list[TypologieService]]
    thematiques: Optional[list[Thematique]]
    prise_rdv: Optional[HttpUrl]
    frais: Optional[list[Frais]]
    frais_autres: Optional[str]
    profils: Optional[list[Profil]]

    class Config:
        extra = Extra.forbid


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
    antenne: bool = False
    lien_source: Optional[HttpUrl]
    horaires_ouverture: Optional[str]
    accessibilite: Optional[HttpUrl]
    labels_nationaux: Optional[list[LabelNational]]
    labels_autres: Optional[list[str]]
    thematiques: Optional[list[Thematique]]

    class Config:
        extra = Extra.forbid


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


def generate_services_json_schema():
    """Generate the services file json schema from the `Service` model."""

    # json schema for a file containing a **list** of services
    return {
        "title": "Services de l'insertion",
        "$schema": "http://json-schema.org/draft-07/schema",
        "$id": (
            "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
            "/main/services.json"
        ),
        "description": "",
        "type": "array",
        "items": {
            "$ref": "#/definitions/Service",
        },
        # Pydantic generates the json schema of a **single** service from the
        # `Service` model. Only the definitions are extracted.
        "definitions": pydantic.schema_of(Service)["definitions"],
    }
