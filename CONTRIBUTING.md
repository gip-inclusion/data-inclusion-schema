# Contribuer

## Prérequis

* `uv` : pour la gestion de l'environnement python, les dépendances, le build. Voir [les instructions d'installation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

## Installation

```bash
# Cloner le dépôt
git clone git@github.com:gip-inclusion/data-inclusion-schema.git

# Initialiser l'environnement
uv sync

# Installer les outils de qualité de codes
uv run pre-commit install
```

## Proposer une modification

Les fichiers du dossier `./schemas/` ne doivent pas être édités directement.

Ces fichiers sont générés à partir des modèles python définis dans le dossier `./src/`.


### 1. Éditer les modèles de définition du schéma


```bash
src/
└── data_inclusion
    └── schema
        ├── __init__.py
        ├── __main__.py
        ├── base.py
        ├── common.py
        ├── frais.py
        ├── labels_nationaux.py
        ├── modes_accueil.py
        ├── modes_orientation.py
        ├── profils.py
        ├── services.py
        ├── structures.py
        ├── thematiques.py
        ├── typologies_de_services.py
        ├── typologies_de_structures.py
        └── zones_de_diffusion.py
```

### 2. Regénérer le json schéma

Lancer la commande suivante à la racine du repo :

```bash
uv run data-inclusion-schema
```

### 3. Ouvrir une PR avec les changements

Ajouter ses modifications au [CHANGELOG](CHANGELOG.md) dans la section "à venir".


## Faire une release

1. Sur une PR:
    - modif du numéro de version du package sur [pyproject.toml](pyproject.toml)
    - Passer les changements de ## À venir dans la section de la nouvelle release
2. `git tag {my-tag} & git tag -f latest & git push --tags`
3. release sur git hub en pointant sur le tag
