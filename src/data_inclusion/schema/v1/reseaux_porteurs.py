from data_inclusion.schema.base import EnhancedEnum


class ReseauPorteur(EnhancedEnum):
    """Réseaux porteurs"""

    # règles :
    #
    # valeurs :
    # - utiliser l'acronyme ou le nom officiel du réseau, en minuscule : "CAF" -> "caf"
    # - slugifier la valeur : "Action Logement" -> "action-logement"
    #
    # labels :
    # - utiliser le nom officiel du réseau
    # - ne pas utiliser d'acronymes, sauf si la forme développée est beaucoup moins
    #   courante que l'acronyme :
    #   - "Caisse d’Allocations Familiales" ok
    #   - "GEIQ" ok
    # - s'il n'y a pas de nom officiel, utiliser le pluriel : "Chambres Consulaires"
    # - respecter la "title case". Majuscule pour chaque mot, sauf les prépositions et
    #   conjonctions de coordination : "Maisons de l’Emploi"
    # - ne pas terminer les labels par un point
    # - préciser le type de réseaux pour les moins connus : "Association SINGA"
    #
    # descriptions :
    # - ne pas reprendre le label
    # - terminer par un point
    # - si le réseau est composé de plusieurs types de structures bien identifiées,
    #   préciser les principales

    SOIXANTE_MILLE_REBONDS = (
        "60000-rebonds",
        "60 000 Rebonds",
        None,
    )
    ACTION_LOGEMENT = (
        "action-logement",
        "Action Logement",
        None,
    )
    ADIE = (
        "adie",
        "Association pour le Droit à l’Initiative Économique",
        None,
    )
    AFPA = (
        "afpa",
        "Agence Nationale pour la Formation Professionnelle des Adultes",
        None,
    )
    AGEFIPH = (
        "agefiph",
        "Agefiph",
        None,
    )
    AIDANTS_CONNECT = (
        "aidants-connect",
        "Aidants Connect",
        None,
    )
    ALLIANCE_VILLES_EMPLOI = (
        "alliance-villes-emploi",
        "Alliance Villes Emploi",
        None,
    )
    ANLCI = (
        "anlci",
        "Agence Nationale de Lutte Contre l’Illettrisme",
        None,
    )
    APPRENTIS_DAUTEUIL = (
        "apprentis-dauteuil",
        "Apprentis d’Auteuil",
        None,
    )
    ASE = (
        "ase",
        "Aide Sociale à l’Enfance",
        None,
    )
    BANQUES_ALIMENTAIRES = (
        "banques-alimentaires",
        "Banques Alimentaires",
        None,
    )
    CAARUD = (
        "caarud",
        (
            "Centres d’Accueil et d’Accompagnement à la Réduction de Risques "
            "pour Usagers de Drogues"
        ),
        None,
    )
    CADA = (
        "cada",
        "Centres d’Accueil de Demandeurs d’Asile",
        None,
    )
    CAF = (
        "caf",
        "Caisse d’Allocations Familiales",
        None,
    )
    CAMPUS_CONNECTE = (
        "campus-connecte",
        "Campus Connecté",
        None,
    )
    CAP_EMPLOI_RESEAU_CHEOPS = (
        "cap-emploi-reseau-cheops",
        "CAP Emploi - Réseau CHEOPS",
        None,
    )
    CAVA = (
        "cava",
        "Centres d’Adaptation à la Vie Active",
        None,
    )
    CHAMBRES_CONSULAIRES = (
        "chambres-consulaires",
        "Chambres Consulaires",
        (
            "Les Chambres de Commerce et d’Industrie (CCI), "
            "les Chambres des Métiers et de l’Artisanat (CMA) "
            "et les Chambres d’Agriculture (CA)."
        ),
    )
    CHANTIER_ECOLE = (
        "chantier-ecole",
        "Réseau Chantier École",
        None,
    )
    CHRS = (
        "chrs",
        "Centres d’Hébergement et de Réinsertion Sociale",
        None,
    )
    CHU = (
        "chu",
        "Centres d’Hébergement d’Urgence",
        None,
    )
    CIDFF = (
        "cidff",
        "Centres d’Information sur les Droits des Femmes et des Familles",
        None,
    )
    CMP = (
        "cmp",
        "Centres Médico-Psychologiques",
        None,
    )
    CMS = (
        "cms",
        "Centres Médico-Sociaux",
        None,
    )
    CNAM = (
        "cnam",
        "Conservatoire National des Arts et Métiers",
        None,
    )
    COLLECTIF_EMPLOI = (
        "collectif-emploi",
        "Collectif Emploi",
        None,
    )
    COMMUNES = (
        "communes",
        "Communes, mairies, communautés de communes, etc.",
        None,
    )
    COORACE = (
        "coorace",
        "Fédération COORACE",
        None,
    )
    CONSEILLERS_NUMERIQUES = (
        "conseillers-numeriques",
        "Conseillers Numériques",
        None,
    )
    CPAM = (
        "cpam",
        "Caisses Primaires d’Assurance Maladie",
        None,
    )
    CPH = (
        "cph",
        "Centres Provisoires d’Hébergement",
        None,
    )
    CRECHES_AVIP = (
        "creches-avip",
        "Crèches à Vocation d’Insertion Professionnelle",
        None,
    )
    CREPI = (
        "crepi",
        "CREPI",
        None,
    )
    CRESUS = (
        "cresus",
        "Fédération Française des Associations CRÉSUS",
        None,
    )
    CROIX_ROUGE = (
        "croix-rouge",
        "Croix-Rouge",
        None,
    )
    CSAPA = (
        "csapa",
        "Centres de Soins, d’Accompagnement et de Prévention en Addictologie",
        None,
    )
    DEPARTEMENTS = (
        "departements",
        "Départements et Services Départementaux",
        (
            "Les Conseils Départementaux (CD), "
            "les Maisons Départementales pour les Personnes Handicapées (MDPH), "
            "les Unions Départementales des Associations Familiales (UDAF), "
            "les Centres Départementaux d’Action Sociale (CDAS), "
            "etc."
        ),
    )
    DUO_FOR_A_JOB = (
        "duo-for-a-job",
        "DUO for a JOB",
        None,
    )
    ECOLES_DE_LA_DEUXIEME_CHANCE = (
        "ecoles-de-la-deuxieme-chance",
        "Écoles de la 2ᵉ Chance",
        None,
    )
    EGEE = (
        "egee",
        "Association EGEE",
        None,
    )
    EMMAUS = (
        "emmaus",
        "Emmaüs",
        None,
    )
    EPIDE = (
        "epide",
        "EPIDE",
        None,
    )
    ESPACES_PUBLICS_NUMERIQUES = (
        "espaces-publics-numeriques",
        "Espaces Publics Numériques",
        None,
    )
    ETCLD = (
        "etcld",
        "Expérimentation Territoriale contre le Chômage de Longue Durée",
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
    FCSF = (
        "fcsf",
        "Fédération des Centres Sociaux et Socioculturels de France",
        None,
    )
    FEDERATION_PROFESSIONNELLE_FEMMES = (
        "federation-professionnelle-femmes",
        "Fédération Professionnelle pour les Femmes",
        None,
    )
    FEDERATION_DES_ACTEURS_DE_LA_SOLIDARITE = (
        "federation-des-acteurs-de-la-solidarite",
        "Fédération des Acteurs de la Solidarité",
        None,
    )
    FRANCE_ACTIVE = (
        "france-active",
        "France Active",
        None,
    )
    FRANCE_SERVICE = (
        "france-service",
        "France Service",
        None,
    )
    FRANCE_TRAVAIL = (
        "france-travail",
        "France Travail",
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
        "Grandes Écoles du Numérique",
        None,
    )
    HUDA = (
        "huda",
        "Hébergement d’Urgence pour Demandeurs d’Asile",
        None,
    )
    HUP = (
        "hup",
        "Association H’UP",
        None,
    )
    INAE = (
        "inae",
        "INAÉ Nouvelle Aquitaine",
        None,
    )
    INITIATIVE_FRANCE = (
        "initiative-france",
        "Initiative France",
        None,
    )
    KONEXIO = (
        "konexio",
        "Association Konexio",
        None,
    )
    LA_CRAVATE_SOLIDAIRE = (
        "la-cravate-solidaire",
        "La Cravate Solidaire",
        None,
    )
    LA_POSTE = (
        "la-poste",
        "La Poste",
        None,
    )
    LES_PREMIERES = (
        "les-premieres",
        "Les Premières",
        None,
    )
    MAISONS_DE_L_EMPLOI = (
        "maisons-de-l-emploi",
        "Maisons de l’Emploi",
        None,
    )
    MAISONS_DES_SOLIDARITES = (
        "maisons-des-solidarites",
        "Maisons Départementales des Solidarités (MDS)",
        (
            "Les Maisons Départementales des Solidarités sont des services "
            "départementaux. Par conséquent, le réseau `departements` devrait être "
            "également défini pour ces structures."
        ),
    )
    MISSION_LOCALE = (
        "mission-locale",
        "Mission Locale",
        None,
    )
    MJC = (
        "mjc",
        "Maisons des Jeunes et de la Culture",
        None,
    )
    MOBIN = (
        "mobin",
        "Mob’In",
        None,
    )
    MSAP = (
        "msap",
        "Maisons de Services Au Public",
        None,
    )
    MUTUALITE_SOCIALE_AGRICOLE = (
        "mutualite-sociale-agricole",
        "Mutualité Sociale Agricole",
        None,
    )
    NQT = (
        "nqt",
        "Association NQT",
        None,
    )
    PIMMS_MEDIATION = (
        "pimms-mediation",
        "Point Information Médiation Multi Services",
        None,
    )
    PJJ = (
        "pjj",
        "Protection Judiciaire de la Jeunesse",
        None,
    )
    PLIE = (
        "plie",
        "Plans Locaux pour l’Insertion et l’Emploi",
        None,
    )
    POINTS_CONSEIL_BUDGET = (
        "points-conseil-budget",
        "Points Conseil Budget",
        None,
    )
    POINTS_JUSTICE = (
        "points-justice",
        "Points Justice",
        None,
    )
    POSITIVE_PLANET = (
        "positive-planet",
        "Positive Planet",
        None,
    )
    REGIONS = (
        "regions",
        "Régions, Préfectures et services régionaux",
        (
            "Les Conseils Régionaux (CR), "
            "les préfectures, "
            "les Directions Régionales de l’Économie, de l’Emploi, du Travail et des"
            "Solidarités (DREETS), "
            "etc."
        ),
    )
    RESEAU_APP = (
        "reseau-app",
        "Réseau APP",
        None,
    )
    RESEAU_BGE = (
        "reseau-bge",
        "Réseau BGE",
        None,
    )
    RESEAU_ENTREPRENDRE = (
        "reseau-entreprendre",
        "Réseau Entreprendre",
        None,
    )
    RESEAU_INFORMATION_JEUNESSE = (
        "reseau-information-jeunesse",
        "Réseau Information Jeunesse",
        None,
    )
    RESIDENCES_FJT = (
        "residences-fjt",
        "Résidences - Foyers Jeunes Travailleurs",
        None,
    )
    RESSOURCERIES = (
        "ressourceries",
        "Ressourceries",
        None,
    )
    RESTOS_DU_COEUR = (
        "restos-du-coeur",
        "Restos du Coeur",
        None,
    )
    SECOURS_POPULAIRE = (
        "secours-populaire",
        "Secours Populaire",
        None,
    )
    SIAE = (
        "siae",
        "Structures d’Insertion par l’Activité Économique",
        None,
    )
    SIAO = (
        "siao",
        "Services Intégrés d’Accueil et d’Orientation",
        None,
    )
    SIMPLON = (
        "simplon",
        "Simplon",
        None,
    )
    SINGA = (
        "singa",
        "Association SINGA",
        None,
    )
    SNC = (
        "snc",
        "Solidarité Nouvelle Face au Chômage",
        None,
    )
    SPIP = (
        "spip",
        "Services Pénitentiaires d’Insertion et de Probation",
        None,
    )
    TOUS_TES_POSSIBLES = (
        "tous-tes-possibles",
        "Tous Tes Possibles",
        None,
    )
    UNAF = (
        "unaf",
        "Union Nationale de l’Aide aux Familles",
        None,
    )
    UNCCAS = (
        "unccas",
        "Union Nationale des Centres Communaux d’Action Sociale",
        (
            "Les Centres Communaux d’Action Sociale (CCAS) "
            "et les Centres Intercommunaux d’Action Sociale (CIAS)."
        ),
    )
    UNEA = (
        "unea",
        "Union Nationale des Entreprises Adaptées",
        None,
    )
    UNIS_CITE = (
        "unis-cite",
        "UnisCité",
        None,
    )
    WIMOOV = (
        "wimoov",
        "Wimoov",
        None,
    )
