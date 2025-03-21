!!! info "Les champs marqués d’une astérisque (*) sont obligatoires."



### `Id` *





Type : `string`










---

### `Siret`





Type : `string`





Regex : `^\d{14}$`




---

### `Rna`





Type : `string`





Regex : `^W\d{9}$`




---

### `Nom` *





Type : `string`










---

### `Commune`





Type : `string`










---

### `Code Postal`





Type : `string`





Regex : `^\d{5}$`




---

### `Code Insee`





Type : `string`





Regex : `^\w{5}$`




---

### `Adresse`





Type : `string`










---

### `Complement Adresse`





Type : `string`










---

### `Longitude`





Type : `number`










---

### `Latitude`





Type : `number`










---

### `typologie`





Type : `string`










Valeurs acceptées : voir le [référentiel associé](referentiels/typologies_de_structures.md)




---

### `Telephone`





Type : `string`










---

### `Courriel`

Courriel à utiliser pour obtenir des informations complémentaires sur la structure.



Type : `string`



Format : `email`






Validation :
Doit suivre le format de la RFC 5322.
Si non conforme ou destinataire inexistant, suppression de la valeur.

Exemples :

```json
"exemple@inclusion.gouv.fr"

```

---

### `Site Web`





Type : `string`



Format : `uri`






---

### `Presentation Resume`





Type : `string`










---

### `Presentation Detail`





Type : `string`










---

### `Source` *





Type : `string`










---

### `Date Maj` *





Type : ``



Format : `date | date-time`






---

### `Antenne`





Type : `boolean`










---

### `Lien Source`





Type : `string`



Format : `uri`






---

### `Horaires Ouverture`





Type : `string`










---

### `Accessibilite`





Type : `string`



Format : `uri`






---

### `Labels Nationaux`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/labels_nationaux.md)




---

### `Labels Autres`





Type : `array`










---

### `Thematiques`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/thematiques.md)




---
