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

### `id` *

Identifiant unique de la structure, obtenu par une combinaison de l’identifiant producteur et de l’identifiant de la structure (fourni par le producteur).



Type : `string`










Exemples :

```json
"emplois-de-linclusion--17"
"france-travail--ccas-provence-alpes-cote-dazur-2024-01-01"
"dora--AidantsConnect:2024-47BXY"

```

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

### `date_maj` *

Date de dernière modification de la structure chez le producteur de données.



Type : `string`



Format : `date`






Exemples :

```json
"2025-02-14"

```

---

### `description`

Description de la structure.



Type : `string | null`










Exemples :

```json
"L’association 3027 offre un accès gratuit aux arts, à la culture et au sport pour toutes et tous sans distinction et en priorité aux personnes en situation de précarité et d’isolement."

```

---

### `lien_source`

Lien pour accéder à la structure sur le site web du producteur.



Type : `string | null`



Format : `uri`






Exemples :

```json
"https://dora.inclusion.beta.gouv.fr/structures/ass-pour-droit-a-l-i-nhes"

```

---

### `siret`

Un numéro SIRET associé à la structure.

Lorsque la structure correspond à un établissement dans la base sirene, le numéro SIRET doit être celui de cet établissement.

Si la structure ne correspond pas strictement à un établissement de la base sirene, le numéro SIRET du siège social peut être utilisé.

data·inclusion vérifie régulièrement la validité des numéros SIRET fournis. Les SIRETs inconnus sont retirés. Lorsque l’établissement associé à un SIRET a fait l’objet d’une succession (d’après la base sirene), data·inclusion remplace ce SIRET par celui de l’établissement successeur. Lorsque l’établissement associé est déclaré fermé et sans successeur, data·inclusion retire la structure.



Type : `string | null`





Regex : `^\d{14}$`




Exemples :

```json
"13003013300016"

```

---

### `commune`





Type : `string | null`










---

### `code_postal`





Type : `string | null`





Regex : `^\d{5}$`




---

### `code_insee`





Type : `string | null`





Regex : `^\w{5}$`




---

### `adresse`





Type : `string | null`










---

### `complement_adresse`





Type : `string | null`










---

### `longitude`





Type : `number | null`










---

### `latitude`





Type : `number | null`










---

### `telephone`

Numéro de téléphone à utiliser pour obtenir des informations complémentaires sur la structure.

Chaîne de caractères contenant un seul numéro de téléphone, de préfèrence au format E.164.



Type : `string | null`










Exemples :

```json
"+33123456789"

```

---

### `courriel`

Courriel à utiliser pour obtenir des informations complémentaires sur la structure.

Doit suivre le format de la RFC 5322.



Type : `string | null`



Format : `email`






Exemples :

```json
"exemple@inclusion.gouv.fr"

```

---

### `site_web`





Type : `string | null`



Format : `uri`






---

### `horaires_accueil`

Horaires d’accueil du public par la structure.

Un service peut avoir un horaire d’accueil différent. Se référer aux horaires des services.

Doit être au format [OpenStreetMap Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

[Outil d’aide à la saisie](https://projets.pavie.info/yohours/).



Type : `string | null`










Exemples :

```json
"Mo-Fr 08:30-12:30; PH off"

```

---

### `accessibilite_lieu`

Lien vers la page Accesslibre référençant le niveau d’accessibilité de la structure.

Le format attendu est donc un lien vers [Accesslibre](https://acceslibre.beta.gouv.fr/).



Type : `string | null`



Format : `uri`






Exemples :

```json
"https://acceslibre.beta.gouv.fr/app/17-la-greve-sur-mignon/a/mairie/erp/mairie-la-greve-sur-mignon/"

```

---

### `reseaux_porteurs`

Réseaux, organisations ou administrations portant la structure.



Type : `array[string] | null`









Valeurs acceptées : voir le [référentiel associé](referentiels/reseaux_porteurs.md)



Exemples :

```json
["mission-locale"]

```

---
