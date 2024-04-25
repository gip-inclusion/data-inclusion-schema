# Contribuer

## Prérequis

### `python`

Le projet utilise `python3.10`.

[`pyenv`](https://github.com/pyenv/pyenv-installer) est un bon moyen d'installer python localement.

## Installation

```bash
# Cloner le dépôt
git clone git@github.com:gip-inclusion/data-inclusion-schema.git

# Initialiser un virtual env à la racine du repo
python3.10 -m venv .venv && source .venv/bin/activate && pip install -U pip setuptools wheel && pip install -e .[dev]

# Installer les outils de qualité de codes
pre-commit install
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

Lancer la commande suivante à la racine du repo.

```bash
data-inclusion-schema
```

### 3. Ouvrir une PR avec les changements
