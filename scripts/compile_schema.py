import json
import pathlib

from data_inclusion.schema import v1

VERSION = "v1"
SCHEMAS_DIR = pathlib.Path() / "schemas" / VERSION
ENUM_FILENAMES = {
    v1.Frais: "frais",
    v1.ModeAccueil: "modes_accueil",
    v1.Thematique: "thematiques",
    v1.ModeMobilisation: "modes_mobilisation",
    v1.PersonneMobilisatrice: "personnes_mobilisatrices",
    v1.Public: "publics",
    v1.ReseauPorteur: "reseaux_porteurs",
    v1.TypeService: "types_de_services",
}


def json_dump(obj, file):
    json.dump(
        obj,
        file,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )


def compile_schema():
    SCHEMAS_DIR.mkdir(exist_ok=True)
    (SCHEMAS_DIR).mkdir(exist_ok=True, parents=True)

    for model in [v1.Structure, v1.Service]:
        with (SCHEMAS_DIR / f"{model.__name__.lower()}.json").open("w") as file:
            json_dump(model.model_json_schema(), file)

    for enum, filename in ENUM_FILENAMES.items():
        with (SCHEMAS_DIR / "extra" / f"{filename.replace('_', '-')}.json").open(
            "w"
        ) as file:
            json_dump(enum.as_dict_list(), file)


if __name__ == "__main__":
    compile_schema()
