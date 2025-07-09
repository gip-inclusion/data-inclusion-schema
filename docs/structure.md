!!! info "Les champs marqués d’une astérisque (*) sont obligatoires."



### `source` *





Type : `string`










---

### `id` *





Type : `string`










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

### `description` *

Description de la structure.

Entre 50 et 2000 caractères.



Type : `string`










Exemples :

```json
"L’association 3027 offre un accès gratuit aux arts, à la culture et au sport pour toutes et tous sans distinction et en priorité aux personnes en situation de précarité et d’isolement."

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

### `siret`





Type : `string`





Regex : `^\d{14}$`




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

### `horaires_accueil`

Horaires d’accueil du public par la structure.

Un service peut avoir un horaire d’accueil différent. Se référer aux horaires des services.

Doit être au format [OpenStreetMap Opening Hours](https://wiki.openstreetmap.org/wiki/FR:Key:opening_hours).

[Outil d’aide à la saisie](https://projets.pavie.info/yohours/).



Type : `string`










Exemples :

```json
"Mo-Fr 08:30-12:30; PH off"

```

---

### `accessibilite_lieu`

Lien vers la page Accesslibre référençant le niveau d’accessibilité de la structure.

Le format attendu est donc un lien vers [Accesslibre](https://acceslibre.beta.gouv.fr/).



Type : `string`



Format : `uri`






Exemples :

```json
"https://acceslibre.beta.gouv.fr/app/17-la-greve-sur-mignon/a/mairie/erp/mairie-la-greve-sur-mignon/"

```

---

### `reseaux_porteurs`

Réseaux, organisations ou administrations portant la structure.



Type : `array[string]`









Valeurs acceptées : voir le [référentiel associé](referentiels/reseaux_porteurs.md)



Exemples :

```json
["mission-locale"]

```

---
