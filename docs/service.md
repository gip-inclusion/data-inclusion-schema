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





Type : `array[string]`










Valeurs acceptées : `"gratuit&#34;, &#34;gratuit-sous-conditions&#34;, &#34;payant&#34;, &#34;adhesion&#34;, &#34;pass-numerique"`




---

### `frais_autres`





Type : `string`










---

### `profils`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/profils.md)




---

### `profils_precisions`





Type : `string`










---

### `pre_requis`





Type : `array`










---

### `justificatifs`





Type : `array`










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

### `zone_diffusion_type`





Type : `string`










Valeurs acceptées : `"commune&#34;, &#34;epci&#34;, &#34;region&#34;, &#34;departement&#34;, &#34;pays"`




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










Valeurs acceptées : `"envoyer-un-courriel&#34;, &#34;se-presenter&#34;, &#34;telephoner&#34;, &#34;utiliser-lien-mobilisation"`




Exemples :

```json
"envoyer-un-courriel"

```

---

### `mobilisable_par`

Indique qui peut mobiliser le service : usagers, professionnels ou les deux.



Type : `array[string]`










Valeurs acceptées : `"usagers&#34;, &#34;professionnels"`




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
