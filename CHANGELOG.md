# Changements

## À venir

### Ajouts

Ajout des champs volume_horaire_hebdomadaire et nombre_semaines

### Changements

### Dépréciations

### Suppressions

## 1.0.0 - 2025-XX-XX

### Ajouts

* ajout du champ `mobilisable_par` et du référentiel associé

### Changements

* remplacement des champs `presentation_***` en faveur d'un champ unique `description` et mise à jour du critère de qualité `description_bien_definie`
* remplacement des champs `prise_rdv`, `formulaire_en_ligne` et `page_web` en faveur d'un champ unique `lien_mobilisation`
* remplacement des champs `modes_orientation_***` en faveur d'un champ unique `modes_mobilisation`
* remplacement des champs `modes_orientation_***_autres` en faveur d'un champ unique `modes_mobilisation_precisions`
* remplacement du critère score de qualité `au_moins_un_mode_orientation` par `modes_mobilisation_bien_definis`

### Suppressions

**Schéma structure**

* suppression du champ `antenne`
* suppression du champ `rna`
* suppression du champ `thematiques`
* suppression du champ `lien_source`

**Schéma service**

* suppression du champ `cumulable`
* suppression du champ `recurrence`
* suppression du champ `date_creation`
* suppression du champ `date_suspension`
* suppression du champ `contact_public`
* suppression du champ `lien_source`
