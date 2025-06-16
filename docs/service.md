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
"10\u20ac pour l\u2019adh\u00e9sion annuelle"
"Tarif r\u00e9duit pour les b\u00e9n\u00e9ficiaires du RSA"

```

---

### `profils`





Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/profils.md)



---

### `profils_precisions`





Type : `string`










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









Valeurs acceptées : voir le [référentiel associé](referentiels/modes_accueil.md)



---

### `zone_diffusion_type`





Type : `string`









Valeurs acceptées : voir le [référentiel associé](referentiels/zones_de_diffusion_types.md)



---

### `zone_diffusion_code`





Type : `string`





Regex : `^\d{2}$ | ^\d{9}$ | ^\w{2,3}$ | ^\w{5}$`




---

### `zone_diffusion_nom`





Type : `string`










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

Modes de mobilisation de l’offre de service. Les valeurs proviennent d’un référentiel disponible sur notre documentation.



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
"La demande est \u00e0 faire depuis l\u2019espace personnel\n                du demandeur d\u2019emploi, rubrique \u00ab mes aides \u00bb,\n                formulaire sp\u00e9cifique \u00ab Aide \u00e0 la mobilit\u00e9 \u00bb."

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
