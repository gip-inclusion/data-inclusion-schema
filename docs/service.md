!!! info "Les champs marqués d’une astérisque (*) sont obligatoires."



### `source` *

Identifiant du producteur original de la donnée.



Type : `string`










Exemples :

```json
"emplois-de-linclusion"
"france-travail"
"dora"

```

---

### `structure_id` *

Identifiant unique de la structure rattachée au service.



Type : `string`










Exemples :

```json
"dora--42"
"cd35--mjc-13-grandjour"

```

---

### `id` *

Identifiant unique du service, obtenu par une combinaison de l’identifiant du producteur et de l’identifiant du service (fourni par le producteur).



Type : `string`










Exemples :

```json
"emplois-de-linclusion--17"
"france-travail--ccas-provence-alpes-cote-dazur-2024-01-01"
"dora--AidantsConnect:2024-47BXY"

```

---

### `nom` *

Nom du service.

Chaîne de caractères entre 3 et 150 caractères, ne se terminant pas par un point.



Type : `string`










Exemples :

```json
"Atelier insertion et posture professionnelle"

```

---

### `description` *

Description du service.

Entre 50 et 2000 caractères.

Ce champ est pris en compte dans le calcul du score de qualité.



Type : `string`










Exemples :

```json
"Cet atelier-conseil vous permet d’identifier les compétences à développer pour atteindre vos objectifs d’évolution professionnelle et à découvrir les différentes modalités de formation.  Durée d’une journée et inscription via votre espace France Travail."

```

---

### `date_maj` *

Date de dernière modification du service chez le producteur de données.



Type : `string`



Format : `date`






Exemples :

```json
"2025-02-14"

```

---

### `type`

Type de service.



Type : `string`









Valeurs acceptées : voir le [référentiel associé](referentiels/types_de_services.md)



Exemples :

```json
"accompagnement"

```

---

### `thematiques`





Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/thematiques.md)



---

### `frais`

Indique si l’accès au service est payant ou gratuit.

Si le service comporte des frais, ceux-ci devraient être précisés dans le champ `frais_precisions`.



Type : `string`









Valeurs acceptées : voir le [référentiel associé](referentiels/frais.md)



Exemples :

```json
"gratuit"
"payant"

```

---

### `frais_precisions`

Précisions sur les éventuels frais pour accéder au service.



Type : `string`










Exemples :

```json
"10€ pour l’adhésion annuelle"
"Tarif réduit pour les bénéficiaires du RSA"

```

---

### `publics`

Publics visés par le service.

Des informations complémentaires peuvent être précisées dans le champ `publics_precisions`.



Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/publics.md)



Exemples :

```json
"femmes"
"residents-qpv-frr"

```

---

### `publics_precisions`

Précisions sur les publics visés par le service.



Type : `string`










Exemples :

```json
"Le jeune entre 15 et 18 ans."

```

---

### `conditions_acces`

Conditions d’accès au service.

Il peut s’agir de prérequis ou de justificatifs à présenter.



Type : `string`










Exemples :

```json
"Maîtrise de la langue française à l’oral et à l’écrit"

```

---

### `commune`





Type : `string`










---

### `code_postal`





Type : `string`





Regex : `^\d{5}$`




---

### `code_insee`





Type : `string`





Regex : `^\w{5}$`




---

### `adresse`





Type : `string`










---

### `complement_adresse`





Type : `string`










---

### `longitude`





Type : `number`










---

### `latitude`





Type : `number`










---

### `telephone`

Numéro de téléphone à utiliser pour obtenir des informations complémentaires sur le service. Si le mode de mobilisation est `telephoner`, peut être utilisé pour mobiliser le service.

Chaîne de caractères contenant un seul numéro de téléphone, de préférence au format E.164.



Type : `string`










Exemples :

```json
"+33123456789"

```

---

### `courriel`

Courriel à utiliser pour obtenir des informations complémentaires sur le service. Si le mode de mobilisation est `envoyer-un-email`, peut être utilisé pour mobiliser le service.

Doit suivre le format de la RFC 5322. Vérification de l’existence du destinataire (envoi d’un courrier de notification)

Si non conforme ou destinataire inexistant, suppression de la valeur.



Type : `string`



Format : `email`






Exemples :

```json
"exemple@inclusion.gouv.fr"

```

---

### `modes_accueil`





Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/modes_accueil.md)



---

### `zone_eligibilite`

Zone géographique d’éligibilité du service.

Contient une liste de codes issus du [Code Officiel Géographique](https://www.insee.fr/fr/information/2560452) maintenu par l’INSEE.

Chaque code dans cette liste peut être un code commune, un code département, un code EPCI ou un code pays.

Si le service est éligible à l’ensemble d’une région, lister les codes des departements de cette région.

Si le service est éligible sur l’ensemble du territoire national, utiliser le code `france` (France) ou le code pays `99100`.

data·inclusion vérifie la validité des codes fournis. Les codes invalides sont supprimés de la liste.

[Outil de recherche des codes](https://www.insee.fr/fr/recherche/recherche-geographique)



Type : `array`










Exemples :

```json
["75056"]
["2A", "2B"]
["200093201"]
["2A", "2B", "200093201"]
["france"]

```

---

### `contact_nom_prenom`





Type : `string`










---

### `lien_mobilisation`

Lien pour accéder ou mobiliser l’offre de service.



Type : `string`



Format : `uri`






Exemples :

```json
"https://www.actionlogement.fr/demande-cfi"

```

---

### `modes_mobilisation`

Modes de mobilisation de l’offre de service.



Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/modes_mobilisation.md)



Exemples :

```json
"envoyer-un-courriel"

```

---

### `mobilisable_par`

Indique qui peut mobiliser le service : usagers, professionnels ou les deux.



Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/personnes_mobilisatrices.md)



Exemples :

```json
["professionnels"]
["usagers"]

```

---

### `mobilisation_precisions`

Précisions sur les modes de mobilisation du service.



Type : `string`










Exemples :

```json
"La demande est à faire depuis l’espace personnel du demandeur d’emploi, rubrique « mes aides », formulaire spécifique « Aide à la mobilité »."

```

---

### `volume_horaire_hebdomadaire`

Durée du service en heures sur une semaine.

L’absence de valeur signifie que le service n’est pas concerné (exemple aide financière) ou que l’information n’est pas disponible.

Champ utilisé dans le cadre des 15h-20h d’activité hebdomadaire des BRSA.



Type : `number`










Exemples :

```json
1

```

---

### `nombre_semaines`

Nombre de semaines sur lequel dure le service.

Ne peut pas être inférieur à 1. L’absence de valeur signifie que le service n’est pas concerné (exemple aide financière) ou que l’information n’est pas disponible.

Champ utilisé dans le cadre des 15h-20h d’activité hebdomadaire des BRSA.



Type : `integer`










Exemples :

```json
3

```

---

### `horaires_accueil`

Horaires d’accueil du public pour ce service.

Si le champ n’est pas renseigné, les horaires d’accueil de la structure peuvent être utilisés.

Doit être au format [OpenStreetMap Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

[Outil d’aide à la saisie](https://projets.pavie.info/yohours/).



Type : `string`










Exemples :

```json
"Mo-Fr 08:30-12:30; PH off"

```

---
