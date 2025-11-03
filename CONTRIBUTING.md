# Contribuer

## Prérequis

* `uv` : pour la gestion de l’environnement python, les dépendances, le build. Voir [les instructions d’installation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

## Installation

```bash
# Cloner le dépôt
git clone git@github.com:gip-inclusion/data-inclusion-schema.git

# Initialiser l’environnement
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
        ├── v0/  # version dépréciée
        └── v1/  # version actuelle
```

### 2. Compiler le json schéma

Lancer la commande suivante à la racine du repo :

```bash
uv run scripts/compile_schema.py
```

### 3. Compiler la documentation

```bash
uv run --extra docs scripts/compile_docs.py
```

### 3. Ouvrir une PR avec les changements

Ajouter ses modifications au [CHANGELOG](CHANGELOG.md) dans la section "à venir".

## Faire une release

💡 Les tags (git) utilisent le format `vX.Y.Z`. Le package (python, `pyproject.toml`) utilise le format `X.Y.Z`.

Marche à suivre :

1. Uniquement sur les branches `v0` et `main`
    * `v0` pour toutes les versions `v0`
    * `main` pour toutes les versions `v1`
2. Créer un commit spécifique sur la branche :
    * actualiser la version du package avec `uv version X.Y.Z` (⚠️ pas de `v` ici)
    * actualiser le `CHANGELOG.md`, avec une nouvelle section dédiée pour cette version (⚠️ pas pour les prereleases)
    * `git commit -m "chore: version v$(uv version --short)"`
4. Taguer ce commit : `git tag v$(uv version --short)`
5. Envoyer commit et tag : `git push && git push --tags`
