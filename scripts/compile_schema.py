import importlib
import json
import pathlib
import pkgutil

from data_inclusion import schema

SCHEMAS_DIR = pathlib.Path() / "schemas"


def json_dump(obj, file):
    json.dump(
        obj,
        file,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )


def compile_schema(version: str):
    schema = importlib.import_module(f"data_inclusion.schema.{version}")

    ENUM_FILENAMES = {
        schema.Frais: "frais",
        schema.LabelNational: "labels_nationaux",
        schema.ModeAccueil: "modes_accueil",
        schema.Thematique: "thematiques",
        schema.TypologieStructure: "typologies_de_structures",
    }
    if version == "v0":
        ENUM_FILENAMES[schema.ModeOrientationAccompagnateur] = (
            "modes_orientation_accompagnateur"
        )
        ENUM_FILENAMES[schema.ModeOrientationBeneficiaire] = (
            "modes_orientation_beneficiaire"
        )
        ENUM_FILENAMES[schema.Profil] = "profils"
        ENUM_FILENAMES[schema.TypologieService] = "typologies_de_services"
        ENUM_FILENAMES[schema.ZoneDiffusionType] = "zones_de_diffusion_types"
    elif version == "v1":
        ENUM_FILENAMES[schema.ModeMobilisation] = "modes_mobilisation"
        ENUM_FILENAMES[schema.PersonneMobilisatrice] = "personnes_mobilisatrices"
        ENUM_FILENAMES[schema.Public] = "publics"
        ENUM_FILENAMES[schema.TypeService] = "types_de_services"

    SCHEMAS_DIR.mkdir(exist_ok=True)
    (SCHEMAS_DIR / version).mkdir(exist_ok=True, parents=True)

    for model in [schema.Structure, schema.Service]:
        with (SCHEMAS_DIR / version / f"{model.__name__.lower()}.json").open(
            "w"
        ) as file:
            json_dump(model.model_json_schema(), file)

    for enum, filename in ENUM_FILENAMES.items():
        with (
            SCHEMAS_DIR / version / "extra" / f"{filename.replace('_', '-')}.json"
        ).open("w") as file:
            json_dump(enum.as_dict_list(), file)


def list_schema_versions() -> list[str]:
    return [
        name
        for _, name, is_pkg in pkgutil.iter_modules(schema.__path__)
        if is_pkg and name.startswith("v") and name[1:].isdigit()
    ]


if __name__ == "__main__":
    for version in list_schema_versions():
        compile_schema(version)
