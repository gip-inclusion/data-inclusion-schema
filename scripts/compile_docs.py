import importlib
import pathlib
import pkgutil
import re
from dataclasses import dataclass

import jinja2

from data_inclusion import schema

DOCS_DIR = pathlib.Path() / "docs"


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


def main(version: str) -> None:
    schema = importlib.import_module(f"data_inclusion.schema.{version}")

    ENUM_FILENAMES = {
        schema.Frais: "frais",
        schema.ModeAccueil: "modes_accueil",
        schema.Thematique: "thematiques",
    }
    if version == "v0":
        ENUM_FILENAMES[schema.LabelNational] = "labels_nationaux"
        ENUM_FILENAMES[schema.ModeOrientationAccompagnateur] = (
            "modes_orientation_accompagnateur"
        )
        ENUM_FILENAMES[schema.ModeOrientationBeneficiaire] = (
            "modes_orientation_beneficiaire"
        )
        ENUM_FILENAMES[schema.Profil] = "profils"
        ENUM_FILENAMES[schema.TypologieService] = "typologies_de_services"
        ENUM_FILENAMES[schema.TypologieStructure] = "typologies_de_structures"
        ENUM_FILENAMES[schema.ZoneDiffusionType] = "zones_de_diffusion_types"
    elif version == "v1":
        ENUM_FILENAMES[schema.ModeMobilisation] = "modes_mobilisation"
        ENUM_FILENAMES[schema.PersonneMobilisatrice] = "personnes_mobilisatrices"
        ENUM_FILENAMES[schema.Public] = "publics"
        ENUM_FILENAMES[schema.ReseauPorteur] = "reseaux_porteurs"
        ENUM_FILENAMES[schema.TypeService] = "types_de_services"

    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "referentiels").mkdir(exist_ok=True)

    for model in [schema.Structure, schema.Service]:
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


def list_schema_versions():
    return sorted(
        [
            name
            for _, name, is_pkg in pkgutil.iter_modules(schema.__path__)
            if is_pkg and name.startswith("v") and name[1:].isdigit()
        ]
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        type=str,
        required=False,
        choices=list_schema_versions(),
        default=list_schema_versions()[-1],
        help="Version cible du schéma à compiler. Par défaut, la dernière version.",
    )
    args = parser.parse_args()

    main(args.version)
