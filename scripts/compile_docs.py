import pathlib
import re
from dataclasses import dataclass

import jinja2

from data_inclusion.schema import v1

DOCS_DIR = pathlib.Path() / "docs"
VERSION = "v1"


def snake_case(txt: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", txt).lower()


@dataclass
class PropertyTypeData:
    """Utility class holding property type metadata used during template rendering."""

    type: str
    referentiel: str | None = None
    format: str | None = None
    regex: str | None = None


def get_property_type_data(property_schema: dict) -> PropertyTypeData:
    """Extract metadata from a JSON property schema.

    It uses a recursive approach to parse the given property schema and its
    subschemas (`anyOf`, etc.) and extract the relevant data.
    """

    def _get_property_type_data(d: dict) -> PropertyTypeData:
        if "anyOf" in d:
            any_of_schemas = [_get_property_type_data(schema) for schema in d["anyOf"]]

            return PropertyTypeData(
                type=" | ".join(item.type for item in any_of_schemas),
                referentiel=next(
                    (item.referentiel for item in any_of_schemas if item.referentiel),
                    None,
                ),
                format=next(
                    (item.format for item in any_of_schemas if item.format), None
                ),
                regex=next((item.regex for item in any_of_schemas if item.regex), None),
            )
        if "$ref" in d:
            return PropertyTypeData(
                type="string",
                referentiel=d["$ref"].split("/")[-1],
            )
        if "items" in d:
            return PropertyTypeData(
                type="array[string]",
                referentiel=d["items"]["$ref"].split("/")[-1]
                if "$ref" in d["items"]
                else None,
            )
        if "type" in d:
            return PropertyTypeData(
                type=f'"{d["const"]}"' if "const" in d else d["type"],
                format=d.get("format"),
                regex=d.get("pattern"),
            )

        raise ValueError(f"Cannot parse property schema: {d}")

    return _get_property_type_data(property_schema)


def template_factory(template_name: str) -> jinja2.Template:
    env = jinja2.Environment(
        autoescape=True,
        keep_trailing_newline=True,
        loader=jinja2.FileSystemLoader(searchpath=DOCS_DIR / "templates"),
    )
    env.policies["json.dumps_kwargs"]["ensure_ascii"] = False
    return env.get_template(template_name)


def main() -> None:
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

    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "referentiels").mkdir(exist_ok=True)

    for model in [v1.Structure, v1.Service]:
        with (DOCS_DIR / f"{model.__name__.lower()}.md").open("w") as file:
            file.write(
                template_factory("model.md.j2").render(
                    schema=model.model_json_schema(),
                    get_property_type_data=get_property_type_data,
                    snake_case=snake_case,
                    enum_filenames_by_ref={
                        enum.__name__: filename
                        for enum, filename in ENUM_FILENAMES.items()
                    },
                )
            )

    for enum, filename in ENUM_FILENAMES.items():
        with (DOCS_DIR / "referentiels" / f"{filename}.md").open("w") as file:
            file.write(
                template_factory("referentiel.md.j2").render(
                    referentiel=enum.as_dict_list(),
                )
            )

    with (DOCS_DIR / "summary.md").open("w") as file:
        file.write(
            template_factory("summary.md.j2").render(
                enums=ENUM_FILENAMES,
            )
        )


if __name__ == "__main__":
    main()
