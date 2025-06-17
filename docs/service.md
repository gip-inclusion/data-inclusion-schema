!!! info "Les champs marqués d’une astérisque (*) sont obligatoires."



### `id` *





Type : `string`










---

### `structure_id` *





Type : `string`










---

### `source` *





Type : `string`










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
"Cet atelier-conseil vous permet d\u2019identifier les comp\u00e9tences \u00e0\n                d\u00e9velopper pour atteindre vos objectifs d\u2019\u00e9volution professionnelle et \u00e0\n                d\u00e9couvrir les diff\u00e9rentes modalit\u00e9s de formation.\n\n                Dur\u00e9e d\u2019une journ\u00e9e et inscription via votre espace France Travail."

```

---

### `types`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/typologies_de_services.md)




---

### `thematiques`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/thematiques.md)




---

### `prise_rdv`





Type : `string`



Format : `uri`






---

### `frais`

Indique si l’accès au service est payant ou gratuit.

Si le service comporte des frais, ceux-ci devraient être précisés dans le champ `frais_precisions`.



Type : `string`










Valeurs acceptées : `"gratuit&#34;, &#34;payant"`




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
"10\u20ac pour l\u2019adh\u00e9sion annuelle"
"Tarif r\u00e9duit pour les b\u00e9n\u00e9ficiaires du RSA"

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
"Ma\u00eetrise de la langue fran\u00e7aise \u00e0 l\u2019oral et \u00e0 l\u2019\u00e9crit"

```

---

### `formulaire_en_ligne`





Type : `string`



Format : `uri`






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

### `date_maj` *

Date de dernière modification du service chez le producteur de données.



Type : `string`



Format : `date`






Exemples :

```json
"2025-02-14"

```

---

### `modes_accueil`





Type : `array[string]`










Valeurs acceptées : `"a-distance&#34;, &#34;en-presentiel"`




---

### `zone_eligibilite`

Zone géographique d’éligibilité du service.

Contient une liste de codes issus du Code Officiel Géographique maintenu par l’INSEE.

Chaque code dans cette liste peut être un code commune, un code département, un code EPCI ou un code pays.

Si le service est éligible à l’ensemble d’une région, lister les codes des departements de cette région.

Si le service est éligible sur l’ensemble du territoire national, utiliser le code `france` (France) ou le code pays `99100`.

data·inclusion vérifie la validité des codes fournis. Les codes invalides sont supprimés de la liste.

[Le Code Officiel Géographique de l’INSEE](https://www.insee.fr/fr/information/2560452).

[Outil de recherche des codes](https://www.insee.fr/fr/recherche/recherche-geographique).



Type : `array`










Exemples :

```json
["france"]
["2A", "2B"]
["200093201"]
["2A", "2B", "200093201"]

```

---

### `contact_nom_prenom`





Type : `string`










---

### `page_web`

Lien vers une page web dédiée au service sur le site web de la structure. Ce champ n’est pas destiné à recevoir un lien vers le site d’un producteur de donnée.



Type : `string`



Format : `uri`






Exemples :

```json
"https://insersol.fr/biclou-atelier-reparation-participatif-solidaire/"

```

---

### `modes_orientation_beneficiaire`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/modes_orientation_beneficiaire.md)




---

### `modes_orientation_beneficiaire_autres`





Type : `string`










---

### `modes_orientation_accompagnateur`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/modes_orientation_accompagnateur.md)




---

### `modes_orientation_accompagnateur_autres`





Type : `string`










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

Doit être au format OpenStreetMap Opening Hours.

[Spécification du format OSM Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

[Outil d’aide à la saisie](https://projets.pavie.info/yohours/).



Type : `string`










Exemples :

```json
"Mo-Fr 08:30-12:30; PH off"

```

---
