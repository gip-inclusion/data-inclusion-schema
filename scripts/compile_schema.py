import json
import pathlib

from referentiels import ENUM_FILENAMES, VERSION

from data_inclusion.schema import v1

SCHEMAS_DIR = pathlib.Path() / "schemas" / VERSION


def json_dump(obj, file):
    json.dump(
        obj,
        file,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )


def compile_schema():
    (SCHEMAS_DIR / "extra").mkdir(exist_ok=True, parents=True)

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
