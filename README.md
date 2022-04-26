# Schéma de l'offre d'insertion

Ce dépôt contient le schéma de l'offre d'insertion. Il est issu de la collaboration d'acteurs de l'insertion.

## Le schéma

Le format actuellement supporté est le JSON schema.

Le schéma comprend actuellement les structures de l'insertion et devraient à terme inclure les services proposés par ces structures.

### Exemple de données au format du schéma de l'offre d'insertion.

Données minimales

```json
[
    {
        "id": "c3d15659-8de9-4fd6-b283-04d50f6ace57",
        "siret": "10000001700010",
        "nom": "état français",
        "commune": "Paris",
        "code_postal": "75800",
        "code_insee": "75108",
        "adresse": "55 RUE DU FAUBOURG SAINT HONORE"
    }
]
```

Données étendues

```json
[
    {
        "id": "c3d15659-8de9-4fd6-b283-04d50f6ace57",
        "siret": "10000001700010",
        "nom": "état français",
        "commune": "Paris",
        "code_postal": "75800",
        "code_insee": "75108",
        "adresse": "55 RUE DU FAUBOURG SAINT HONORE",
        "complement_adresse": "",
        "longitude": 2.316934,
        "latitude": 48.87063,
        "typologie": "Autre",
        "telephone": "0142928100",
        "courriel": "contact@en-marche.fr",
        "site_web": "https://comment-contacter.fr/",
        "presentation_resume": "La présidence",
        "presentation_detail": "La présidence de la République",
        "source": "bob"
    }
]
```

## Contribuer

Créer un [nouveau ticket](https://github.com/betagouv/data-inclusion-schema/issues/new) ici.

Participer aux [ateliers](https://app.gitbook.com/o/-LumF4j8whrJ3iKwLJ6f/s/8F5IpX18jjDR1Iawzsnj/schemas-de-donnees-de-loffre/les-schemas-and-ateliers).

## Changements

### Version 0.1.0 - 2022-04-26

Publication initiale.