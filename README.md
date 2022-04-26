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
        "siret": "41822382200028",
        "nom": "MOBILEX",
        "commune": "Bischwiller CEDEX",
        "code_postal": "67242",
        "code_insee": "67046",
        "adresse": "16 RUE DES COUTURIERES"
    }
]
```

Données étendues

```json
[
    {
        "id": "c3d15659-8de9-4fd6-b283-04d50f6ace57",
        "siret": "41822382200028",
        "nom": "MOBILEX",
        "commune": "Bischwiller CEDEX",
        "code_postal": "67242",
        "code_insee": "67046",
        "adresse": "16 RUE DES COUTURIERES",
        "complement_adresse": "HOTEL D'ENTREPRISE TERTIAIRE",
        "longitude": 7.847133,
        "latitude": 48.7702,
        "typologie": "Autre",
        "telephone": "9976329954",
        "courriel": "geovanni@example.net",
        "site_web": "https://www.asso-mobilex.org/",
        "presentation_resume": "L’association Mobilex propose des solutions de déplacement aux personnes pour qui la non mobilité est un frein à l’insertion professionnelle : - connaissance de l'offre de transport du territoire - accès à un véhicule 2 ou 4 roues - transport solidaire - accès au permis",
        "presentation_detail": "",
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