!!! info "Les champs marqués d'une astérisque (*) sont obligatoires."



### `Id` *





Type : `string`










---

### `Structure Id` *





Type : `string`










---

### `Source` *





Type : `string`










---

### `Nom` *





Type : `string`










---

### `Presentation Resume`





Type : `string`










---

### `Presentation Detail`





Type : `string`










---

### `Types`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/typologies_de_services.md)




---

### `Thematiques`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/thematiques.md)




---

### `Prise Rdv`





Type : `string`



Format : `uri`






---

### `Frais`





Type : `array[string]`










Valeurs acceptées : `"gratuit&#34;, &#34;gratuit-sous-conditions&#34;, &#34;payant&#34;, &#34;adhesion&#34;, &#34;pass-numerique"`




---

### `Frais Autres`





Type : `string`










---

### `Profils`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/profils.md)




---

### `Profils Precisions`





Type : `string`










---

### `Pre Requis`





Type : `array`










---

### `Cumulable`





Type : `boolean`










---

### `Justificatifs`





Type : `array`










---

### `Formulaire En Ligne`





Type : `string`



Format : `uri`






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

### `Recurrence`





Type : `string`










---

### `Date Creation`





Type : `string`



Format : `date`






---

### `Date Suspension`





Type : `string`



Format : `date`






---

### `Lien Source`





Type : `string`



Format : `uri`






---

### `Telephone`





Type : `string`










---

### `Courriel`





Type : `string`



Format : `email`






---

### `Contact Public`





Type : `boolean`










---

### `Date Maj`





Type : `string`



Format : `date | date-time`






---

### `Modes Accueil`





Type : `array[string]`










Valeurs acceptées : `"a-distance&#34;, &#34;en-presentiel"`




---

### `zone_diffusion_type`





Type : `string`










Valeurs acceptées : `"commune&#34;, &#34;epci&#34;, &#34;region&#34;, &#34;departement&#34;, &#34;pays"`




---

### `Zone Diffusion Code`





Type : `string`





Regex : `^\d{2}$ | ^\d{9}$ | ^\w{2,3}$ | ^\w{5}$`




---

### `Zone Diffusion Nom`





Type : `string`










---

### `Contact Nom Prenom`





Type : `string`










---

### `Page Web`

Lien vers une page web dédiée au service sur le site web de la structure. Ce champ n&#39;est pas destiné à recevoir un lien vers le site d&#39;un producteur de donnée.



Type : `string`



Format : `uri`






Exemples :

```json
"https://insersol.fr/biclou-atelier-reparation-participatif-solidaire/"

```

---

### `Modes Orientation Beneficiaire`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/modes_orientation_beneficiaire.md)




---

### `Modes Orientation Beneficiaire Autres`





Type : `string`










---

### `Modes Orientation Accompagnateur`





Type : `array[string]`










Valeurs acceptées : voir le [référentiel associé](referentiels/modes_orientation_accompagnateur.md)




---

### `Modes Orientation Accompagnateur Autres`





Type : `string`










---
