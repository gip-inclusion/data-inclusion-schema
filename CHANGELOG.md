# Changements

## À venir

### Ajouts

### Changements

### Dépréciations

### Suppressions

## 1.0.0 - 2025-XX-XX

### Changements

* renommage du champ structure `horaires_ouverture` en `horaires_accueil`
* renommage du champ service `recurrence` en `horaires_accueil`
* remplacement des champs `presentation_***` en faveur d'un champ unique `description` et mise à jour du critère de qualité `description_bien_definie`
* fusion des champs service `pre_requis` et `justificatifs` dans un nouveau champ `conditions_acces`
* renommage du champ service `frais_autres` en `frais_precisions`
* refonte du référentiel des `frais`

### Suppressions

**Schéma structure**

* suppression du champ `antenne`
* suppression du champ `rna`
* suppression du champ `thematiques`
* suppression du champ `lien_source`

**Schéma service**

* suppression du champ `cumulable`
* suppression du champ `date_creation`
* suppression du champ `date_suspension`
* suppression du champ `contact_public`
* suppression du champ `lien_source`
