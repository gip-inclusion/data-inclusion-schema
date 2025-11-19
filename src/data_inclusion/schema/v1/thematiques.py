from data_inclusion.schema.base import EnhancedEnum


class Categorie(EnhancedEnum):
    """Catégories de thématiques"""

    CHOISIR_UN_METIER = (
        "choisir-un-metier",
        "Choisir un métier",
        None,
    )
    CREER_UNE_ENTREPRISE = (
        "creer-une-entreprise",
        "Créer une entreprise",
        None,
    )
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES = (
        "difficultes-administratives-ou-juridiques",
        "Difficultés administratives ou juridiques",
        None,
    )
    DIFFICULTES_FINANCIERES = (
        "difficultes-financieres",
        "Difficultés financières",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION = (
        "equipement-et-alimentation",
        "Équipement et alimentation",
        None,
    )
    FAMILLE = (
        "famille",
        "Famille",
        None,
    )
    LECTURE_ECRITURE_CALCUL = (
        "lecture-ecriture-calcul",
        "Lecture, écriture et calcul",
        None,
    )
    LOGEMENT_HEBERGEMENT = (
        "logement-hebergement",
        "Logement et hébergement",
        None,
    )
    MOBILITE = (
        "mobilite",
        "Mobilité",
        None,
    )
    NUMERIQUE = (
        "numerique",
        "Numérique",
        None,
    )
    PREPARER_SA_CANDIDATURE = (
        "preparer-sa-candidature",
        "Préparer sa candidature",
        None,
    )
    REMOBILISATION = (
        "remobilisation",
        "Remobilisation",
        None,
    )
    SANTE = (
        "sante",
        "Santé",
        None,
    )
    SE_FORMER = (
        "se-former",
        "Se former",
        None,
    )
    SOUVRIR_A_LINTERNATIONAL = (
        "souvrir-a-linternational",
        "S’ouvrir à l’international",
        None,
    )
    TROUVER_UN_EMPLOI = (
        "trouver-un-emploi",
        "Trouver un emploi",
        None,
    )


class Thematique(EnhancedEnum):
    """Thématiques"""

    #########################
    ### Choisir un métier ###
    #########################
    CHOISIR_UN_METIER__CONFIRMER_SON_CHOIX_DE_METIER = (
        "choisir-un-metier--confirmer-son-choix-de-metier",
        "Confirmer son choix de métier",
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
    CHOISIR_UN_METIER__IDENTIFIER_SES_POINTS_FORTS_ET_SES_COMPETENCES = (
        "choisir-un-metier--identifier-ses-points-forts-et-ses-competences",
        "Identifier ses points forts et ses compétences",
        None,
    )

    ############################
    ### Créer une entreprise ###
    ############################
    CREER_UNE_ENTREPRISE__DEFINIR_SON_PROJET_DE_CREATION_DENTREPRISE = (
        "creer-une-entreprise--definir-son-projet-de-creation-dentreprise",
        "Définir son projet de création d’entreprise",
        None,
    )
    CREER_UNE_ENTREPRISE__DEVELOPPER_SON_ENTREPRISE = (
        "creer-une-entreprise--developper-son-entreprise",
        "Développer son entreprise",
        None,
    )
    CREER_UNE_ENTREPRISE__STRUCTURER_SON_PROJET_DE_CREATION_DENTREPRISE = (
        "creer-une-entreprise--structurer-son-projet-de-creation-dentreprise",
        "Structurer son projet de création d’entreprise",
        None,
    )

    #################################################
    ### Difficultés administratives ou juridiques ###
    #################################################
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES__ACCOMPAGNEMENT_AUX_DEMARCHES_ADMINISTRATIVES = (  # noqa: E501
        "difficultes-administratives-ou-juridiques--accompagnement-aux-demarches-administratives",
        "Accompagnement aux démarches administratives",
        None,
    )
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES__ACCOMPAGNEMENT_POUR_LACCES_A_LA_CITOYENNETE = (  # noqa: E501
        "difficultes-administratives-ou-juridiques--accompagnement-pour-lacces-a-la-citoyennete",
        "Accompagnement pour l’accès à la citoyenneté",
        None,
    )
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES__ACCOMPAGNEMENT_POUR_LACCES_AUX_DROITS = (
        "difficultes-administratives-ou-juridiques--accompagnement-pour-lacces-aux-droits",
        "Accompagnement pour l’accès aux droits",
        None,
    )
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES__BENEFICIER_DUNE_MESURE_DACCOMPAGNEMENT_ADAPTE = (  # noqa: E501
        "difficultes-administratives-ou-juridiques--beneficier-dune-mesure-daccompagnement-adapte",
        "Bénéficier d’une mesure d’accompagnement adapté",
        None,
    )
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES__CONNAITRE_SES_DROITS_FACE_A_UNE_DISCRIMINATION = (  # noqa: E501
        "difficultes-administratives-ou-juridiques--connaitre-ses-droits-face-a-une-discrimination",
        "Connaître ses droits face à une discrimination",
        None,
    )
    DIFFICULTES_ADMINISTRATIVES_OU_JURIDIQUES__PRENDRE_EN_COMPTE_UNE_PROBLEMATIQUE_JUDICIAIRE = (  # noqa: E501
        "difficultes-administratives-ou-juridiques--prendre-en-compte-une-problematique-judiciaire",
        "Prendre en compte une problématique judiciaire",
        None,
    )

    ###############################
    ### Difficultés financières ###
    ###############################
    DIFFICULTES_FINANCIERES__ACQUERIR_UNE_AUTONOMIE_BUDGETAIRE = (
        "difficultes-financieres--acquerir-une-autonomie-budgetaire",
        "Acquérir une autonomie budgétaire",
        None,
    )
    DIFFICULTES_FINANCIERES__AMELIORER_SA_GESTION_BUDGETAIRE = (
        "difficultes-financieres--ameliorer-sa-gestion-budgetaire",
        "Améliorer sa gestion budgétaire",
        None,
    )
    DIFFICULTES_FINANCIERES__METTRE_EN_PLACE_UNE_MESURE_DE_PROTECTION_FINANCIERE = (
        "difficultes-financieres--mettre-en-place-une-mesure-de-protection-financiere",
        "Mettre en place une mesure de protection financière",
        None,
    )
    DIFFICULTES_FINANCIERES__PREVENIR_UNE_DEGRADATION_DE_LA_SITUATION_FINANCIERE = (
        "difficultes-financieres--prevenir-une-degradation-de-la-situation-financiere",
        "Prévenir une dégradation de la situation financière",
        None,
    )
    DIFFICULTES_FINANCIERES__SITUATION_DENDETTEMENT_SURENDETTEMENT = (
        "difficultes-financieres--situation-dendettement-surendettement",
        "Situation d’endettement ou de surendettement",
        None,
    )

    ##################################
    ### Équipement et alimentation ###
    ##################################
    EQUIPEMENT_ET_ALIMENTATION__AIDE_MENAGERE = (
        "equipement-et-alimentation--aide-menagere",
        "Aide ménagère",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__ALIMENTATION = (
        "equipement-et-alimentation--alimentation",
        "Alimentation",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__ELECTROMENAGER = (
        "equipement-et-alimentation--electromenager",
        "Électroménager",
        None,
    )
    EQUIPEMENT_ET_ALIMENTATION__HABILLEMENT = (
        "equipement-et-alimentation--habillement",
        "Habillement",
        None,
    )

    ###############
    ### Famille ###
    ###############
    FAMILLE__GARDE_DENFANTS = (
        "famille--garde-denfants",
        "Garde d’enfants",
        None,
    )
    FAMILLE__PRISE_EN_CHARGE_PERSONNE_DEPENDANTE = (
        "famille--prise-en-charge-personne-dependante",
        "Prise en charge d’une personne dépendante",
        None,
    )
    FAMILLE__SOUTIEN_A_LA_PARENTALITE_ET_A_LEDUCATION = (
        "famille--soutien-a-la-parentalite-et-a-leducation",
        "Soutien à la parentalité et à l’éducation",
        None,
    )
    FAMILLE__SOUTIEN_AIDANTS = (
        "famille--soutien-aidants",
        "Soutien aux aidants",
        None,
    )
    FAMILLE__SURMONTER_CONFLITS_SEPARATION_VIOLENCE = (
        "famille--surmonter-conflits-separation-violence",
        "Surmonter les conflits liés à la séparation ou à la violence",
        None,
    )

    ###################################
    ### Lecture, écriture et calcul ###
    ###################################
    LECTURE_ECRITURE_CALCUL__MAITRISER_LE_CALCUL = (
        "lecture-ecriture-calcul--maitriser-le-calcul",
        "Maîtriser le calcul",
        None,
    )
    LECTURE_ECRITURE_CALCUL__MAITRISER_LE_FRANCAIS = (
        "lecture-ecriture-calcul--maitriser-le-francais",
        "Maîtriser le français",
        None,
    )

    ###############################
    ### Logement et hébergement ###
    ###############################
    LOGEMENT_HEBERGEMENT__ACHETER_UN_LOGEMENT = (
        "logement-hebergement--acheter-un-logement",
        "Acheter un logement",
        None,
    )
    LOGEMENT_HEBERGEMENT__CHANGER_DE_LOGEMENT = (
        "logement-hebergement--changer-de-logement",
        "Changer de logement",
        None,
    )
    LOGEMENT_HEBERGEMENT__LOUER_UN_LOGEMENT = (
        "logement-hebergement--louer-un-logement",
        "Louer un logement",
        None,
    )
    LOGEMENT_HEBERGEMENT__RECHERCHER_UNE_SOLUTION_DHEBERGEMENT_TEMPORAIRE = (
        "logement-hebergement--rechercher-une-solution-dhebergement-temporaire",
        "Rechercher une solution d’hébergement temporaire",
        None,
    )
    LOGEMENT_HEBERGEMENT__REDUIRE_LES_IMPAYES_DE_LOYER = (
        "logement-hebergement--reduire-les-impayes-de-loyer",
        "Réduire les impayés de loyer",
        None,
    )
    LOGEMENT_HEBERGEMENT__SE_MAINTENIR_DANS_LE_LOGEMENT = (
        "logement-hebergement--se-maintenir-dans-le-logement",
        "Se maintenir dans le logement",
        None,
    )
    LOGEMENT_HEBERGEMENT__SINFORMER_SUR_LES_DEMARCHES_LIEES_A_LACCES_AU_LOGEMENT = (
        "logement-hebergement--sinformer-sur-les-demarches-liees-a-lacces-au-logement",
        "S’informer sur les démarches liées à l’accès au logement",
        None,
    )

    ################
    ### Mobilité ###
    ################
    MOBILITE__ACCEDER_A_UN_VEHICULE = (
        "mobilite--acceder-a-un-vehicule",
        "Accéder à un véhicule",
        None,
    )
    MOBILITE__ENTRETENIR_REPARER_SON_VEHICULE = (
        "mobilite--entretenir-reparer-son-vehicule",
        "Entretenir et réparer son véhicule",
        None,
    )
    MOBILITE__ETRE_ACCOMPAGNE_DANS_SON_PARCOURS_MOBILITE = (
        "mobilite--etre-accompagne-dans-son-parcours-mobilite",
        "Être accompagné dans son parcours mobilité",
        None,
    )
    MOBILITE__FINANCER_MA_MOBILITE = (
        "mobilite--financer-ma-mobilite",
        "Financer ma mobilité",
        None,
    )
    MOBILITE__PREPARER_UN_PERMIS = (
        "mobilite--preparer-un-permis",
        "Préparer un permis",
        None,
    )
    MOBILITE__UTILISER_DES_SERVICES_DE_MOBILITE_DOUCE_PARTAGEE_COLLECTIVE = (
        "mobilite--mobilite-douce-partagee-collective",
        "Utiliser des services de mobilité douce, partagée ou collective",
        None,
    )

    #################
    ### Numérique ###
    #################
    NUMERIQUE__ACCEDER_A_DES_SERVICES_EN_LIGNE = (
        "numerique--acceder-a-des-services-en-ligne",
        "Accéder à des services en ligne",
        None,
    )
    NUMERIQUE__ACCEDER_A_UNE_CONNEXION_INTERNET = (
        "numerique--acceder-a-une-connexion-internet",
        "Accéder à une connexion Internet",
        None,
    )
    NUMERIQUE__ACQUERIR_UN_EQUIPEMENT = (
        "numerique--acquerir-un-equipement",
        "Acquérir un équipement",
        None,
    )
    NUMERIQUE__MAITRISER_LES_FONDAMENTAUX_DU_NUMERIQUE = (
        "numerique--maitriser-les-fondamentaux-du-numerique",
        "Maîtriser les fondamentaux du numérique",
        None,
    )

    ###############################
    ### Préparer sa candidature ###
    ###############################
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
    PREPARER_SA_CANDIDATURE__REALISER_UN_CV_ET_OU_UNE_LETTRE_DE_MOTIVATION = (
        "preparer-sa-candidature--realiser-un-cv-et-ou-une-lettre-de-motivation",
        "Réaliser un CV et/ou une lettre de motivation",
        None,
    )
    PREPARER_SA_CANDIDATURE__VALORISER_SES_COMPETENCES = (
        "preparer-sa-candidature--valoriser-ses-competences",
        "Valoriser ses compétences",
        None,
    )

    ######################
    ### Remobilisation ###
    ######################
    REMOBILISATION__ACTIVITES_SPORTIVES_ET_CULTURELLES = (
        "remobilisation--activites-sportives-et-culturelles",
        "Activités sportives et culturelles",
        None,
    )
    REMOBILISATION__BENEVOLAT_ACTION_CITOYENNE = (
        "remobilisation--benevolat-action-citoyenne",
        "Bénévolat et action citoyenne",
        None,
    )
    REMOBILISATION__BIEN_ETRE_CONFIANCE_EN_SOI = (
        "remobilisation--bien-etre-confiance-en-soi",
        "Bien-être et confiance en soi",
        None,
    )
    REMOBILISATION__LIEN_SOCIAL = (
        "remobilisation--lien-social",
        "Lien social",
        None,
    )

    #############
    ### Santé ###
    #############
    SANTE__ACCES_AUX_SOINS = (
        "sante--acces-aux-soins",
        "Accès aux soins",
        None,
    )
    SANTE__ADDICTIONS = (
        "sante--addictions",
        "Addictions",
        None,
    )
    SANTE__CONSTITUER_UN_DOSSIER_MDPH_INVALIDITE = (
        "sante--constituer-un-dossier-mdph-invalidite",
        "Constituer un dossier MDPH pour invalidité",
        None,
    )
    SANTE__SANTE_MENTALE = (
        "sante--sante-mentale",
        "Santé mentale",
        None,
    )
    SANTE__SANTE_SEXUELLE = (
        "sante--sante-sexuelle",
        "Santé sexuelle",
        None,
    )

    #################
    ### Se former ###
    #################
    SE_FORMER__MONTER_SON_DOSSIER_DE_FORMATION = (
        "se-former--monter-son-dossier-de-formation",
        "Monter son dossier de formation",
        None,
    )
    SE_FORMER__TROUVER_SA_FORMATION = (
        "se-former--trouver-sa-formation",
        "Trouver sa formation",
        None,
    )

    ##################################
    ### S’ouvrir à l’international ###
    ##################################
    SOUVRIR_A_LINTERNATIONAL__CONNAITRE_LES_OPPORTUNITES_DEMPLOI_A_LETRANGER = (
        "souvrir-a-linternational--connaitre-les-opportunites-demploi-a-letranger",
        "Connaître les opportunités d’emploi à l’étranger",
        None,
    )
    SOUVRIR_A_LINTERNATIONAL__SINFORMER_SUR_LES_AIDES_POUR_TRAVAILLER_A_LETRANGER = (
        "souvrir-a-linternational--sinformer-sur-les-aides-pour-travailler-a-letranger",
        "S’informer sur les aides pour travailler à l’étranger",
        None,
    )
    SOUVRIR_A_LINTERNATIONAL__SORGANISER_SUITE_A_SON_RETOUR_EN_FRANCE = (
        "souvrir-a-linternational--sorganiser-suite-a-son-retour-en-france",
        "S’organiser suite à son retour en France",
        None,
    )

    #########################
    ### Trouver un emploi ###
    #########################
    TROUVER_UN_EMPLOI__CONVAINCRE_UN_RECRUTEUR_EN_ENTRETIEN = (
        "trouver-un-emploi--convaincre-un-recruteur-en-entretien",
        "Convaincre un recruteur en entretien",
        None,
    )
    TROUVER_UN_EMPLOI__FAIRE_DES_CANDIDATURES_SPONTANEES = (
        "trouver-un-emploi--faire-des-candidatures-spontanees",
        "Faire des candidatures spontanées",
        None,
    )
    TROUVER_UN_EMPLOI__MAINTIEN_DANS_LEMPLOI = (
        "trouver-un-emploi--maintien-dans-lemploi",
        "Maintien dans l’emploi",
        None,
    )
    TROUVER_UN_EMPLOI__REPONDRE_A_DES_OFFRES_DEMPLOI = (
        "trouver-un-emploi--repondre-a-des-offres-demploi",
        "Répondre à des offres d’emploi",
        None,
    )
    TROUVER_UN_EMPLOI__SUIVRE_SES_CANDIDATURES_ET_RELANCER_LES_EMPLOYEURS = (
        "trouver-un-emploi--suivre-ses-candidatures-et-relancer-les-employeurs",
        "Suivre ses candidatures et relancer les employeurs",
        None,
    )
