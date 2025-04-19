!!! info "Les champs marqués d’une astérisque (*) sont obligatoires."



### `id` *





Type : `string`










---

### `siret`





Type : `string`





Regex : `^\d{14}$`




---

### `rna`





Type : `string`





Regex : `^W\d{9}$`




---

### `nom` *

Nom de la structure.

Chaîne de caractères entre 3 et 150 caractères, ne se terminant pas par un point.



Type : `string`










Exemples :

```json
"Centre social Le Tournesol"

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

### `typologie`





Type : `string`










Valeurs acceptées : voir le [référentiel associé](referentiels/typologies_de_structures.md)




---

### `telephone`

Numéro de téléphone à utiliser pour obtenir des informations complémentaires sur la structure.

Chaîne de caractères contenant un seul numéro de téléphone, de préfèrence au format E.164.



Type : `string`










Exemples :

```json
"+33123456789"

```

---

### `courriel`

Courriel à utiliser pour obtenir des informations complémentaires sur la structure.

Doit suivre le format de la RFC 5322.



Type : `string`



Format : `email`






Exemples :

```json
"exemple@inclusion.gouv.fr"

```

---

### `site_web`





Type : `string`



Format : `uri`






---

### `presentation_resume`





Type : `string`










---

### `presentation_detail`





Type : `string`










---

### `source` *





Type : `string`










---

### `date_maj` *

Date de dernière modification de la structure chez le producteur de données.



Type : `string`



Format : `date`






Exemples :

```json
"2025-02-14"

```

---

### `lien_source`





Type : `string`



Format : `uri`






---

### `horaires_ouverture`





Type : `string`










---

### `accessibilite`





Type : `string`



Format : `uri`






---

### `labels_nationaux`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/labels_nationaux.md)




---

### `labels_autres`





Type : `array`










---

### `thematiques`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/thematiques.md)




---
