import json
import pathlib
import jinja2
import os

from data_inclusion.schema import (
    Frais,
    LabelNational,
    ModeAccueil,
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
    Profil,
    Service,
    Structure,
    Thematique,
    Typologie,
    TypologieService,
    ZoneDiffusionType,
)


def json_dump(obj, file):
    json.dump(
        obj,
        file,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )


def extract_type_from_any_of(field_schema: dict, model_json_schema: dict):
    field_types = {}
    for field_type in field_schema["anyOf"]:
        if "$ref" in field_type and "type" not in field_type:
            path = field_type["$ref"].split("/")
            item = model_json_schema[path[1]][path[2]]
            field_types[item["type"]] = {"enum": item["enum"], "title": item["title"]}
        elif field_type["type"] == "array" and "$ref" in field_type["items"]:
            path = field_type["items"]["$ref"].split("/")
            field_types["array"] = model_json_schema[path[1]][path[2]]
        elif field_type["type"] == "array":
            field_types["array"] = field_type["items"]["type"]
        elif field_type["type"] == "null":
            continue
        else:
            if field_type["type"] not in field_types:
                extra = {}
                if "format" in field_type:
                    extra["format"] = [field_type["format"]]
                if "pattern" in field_type:
                    extra["pattern"] = [field_type["pattern"]]
                field_types[field_type["type"]] = extra
            else:
                if (
                    "format" in field_type
                    and "format" in field_types[field_type["type"]]
                ):
                    field_types[field_type["type"]]["format"].append(
                        field_type["format"]
                    )
                if (
                    "pattern" in field_type
                    and "pattern" in field_types[field_type["type"]]
                ):
                    field_types[field_type["type"]]["pattern"].append(
                        field_type["pattern"]
                    )
                if (
                    "format" in field_type
                    and "format" not in field_types[field_type["type"]]
                ):
                    field_types[field_type["type"]]["format"] = [field_type["format"]]
                if (
                    "pattern" in field_type
                    and "pattern" not in field_types[field_type["type"]]
                ):
                    field_types[field_type["type"]]["pattern"] = [field_type["pattern"]]

    return field_types


def extract_type_from_model(model_json_schema: dict):
    fields_types = {}
    for field_name, field in model_json_schema["properties"].items():
        if "type" in field:
            fields_types[field_name] = {}
            extra = {}
            if "format" in field:
                extra["format"] = field["format"]
            if "pattern" in field:
                extra["pattern"] = field["pattern"]
            fields_types[field_name][field["type"]] = extra
        if "anyOf" in field:
            fields_types[field_name] = extract_type_from_any_of(
                field, model_json_schema
            )
    return fields_types


def main():
    output_dir = pathlib.Path() / "schemas"
    output_dir.mkdir(exist_ok=True)

    for model in [Structure, Service]:
        model_json_schema = model.model_json_schema()
        with (output_dir / f"{model.__name__.lower()}.json").open("w") as file:
            json.dump(
                model_json_schema,
                file,
                indent=2,
                ensure_ascii=False,
                sort_keys=True,
            )

    # fichiers supplémentaires documentant les énumérations

    (output_dir / "extra").mkdir(exist_ok=True)

    enum_x_file_tuples_list = [
        ("frais.json", Frais),
        ("labels-nationaux.json", LabelNational),
        ("modes-accueil.json", ModeAccueil),
        ("modes-orientation-accompagnateur.json", ModeOrientationAccompagnateur),
        ("modes-orientation-beneficiaire.json", ModeOrientationBeneficiaire),
        ("profils.json", Profil),
        ("thematiques.json", Thematique),
        ("typologies-de-services.json", TypologieService),
        ("typologies-de-structures.json", Typologie),
        ("zones-de-diffusion-types.json", ZoneDiffusionType),
    ]

    for filename, enum in enum_x_file_tuples_list:
        with (output_dir / "extra" / filename).open("w") as file:
            json_dump(enum.as_dict_list(), file)

    fields_types = extract_type_from_model(model_json_schema)

    with open("./docs/jinja_test.md", "w+") as file:
        print(fields_types)
        file.write(
            jinja2.Template(
                open("./src/data_inclusion/schema/template.md.j2").read()
            ).render(model=model_json_schema, field_types=fields_types)
        )


if __name__ == "__main__":
    """
    Usage:
        $ python -m data_inclusion.schema
    """
    main()
