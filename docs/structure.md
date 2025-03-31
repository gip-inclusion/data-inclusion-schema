!!! info "Les champs marqués d'une astérisque (*) sont obligatoires."



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





Type : `string`










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





Type : `string`










---

### `courriel`





Type : `string`



Format : `email`






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

### `antenne`





Type : `boolean`










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
