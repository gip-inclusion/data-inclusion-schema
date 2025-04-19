import pathlib
import re

import jinja2

from data_inclusion.schema.v1 import (
    Frais,
    LabelNational,
    ModeAccueil,
    ModeOrientationAccompagnateur,
    ModeOrientationBeneficiaire,
    Profil,
    Service,
    Structure,
    Thematique,
    TypologieService,
    TypologieStructure,
    ZoneDiffusionType,
)

DOCS_DIR = pathlib.Path() / "docs"

# les référentiels sont affichés en inline dans la documentation
# si leur taille est inférieure à cette limite
DOCS_INLINE_REFERENTIAL_SIZE_LIMIT = 5

ENUM_FILENAMES = {
    Frais: "frais",
    LabelNational: "labels_nationaux",
    ModeAccueil: "modes_accueil",
    ModeOrientationAccompagnateur: "modes_orientation_accompagnateur",
    ModeOrientationBeneficiaire: "modes_orientation_beneficiaire",
    Profil: "profils",
    Thematique: "thematiques",
    TypologieService: "typologies_de_services",
    TypologieStructure: "typologies_de_structures",
    ZoneDiffusionType: "zones_de_diffusion_types",
}


def snake_case(txt: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", txt).lower()


def get_property_type_data(property_schema: dict) -> dict | None:
    match property_schema:
        case {"type": json_type}:
            return {"type": json_type, "format": property_schema.get("format")}
        case {"anyOf": [{"type": "array", "items": {"$ref": ref}}, {"type": "null"}]}:
            return {
                "type": "array[string]",
                "referentiel": ref.split("/")[-1],
            }
        case {"anyOf": [{"$ref": ref}, {"type": "null"}]}:
            return {
                "type": "string",
                "referentiel": ref.split("/")[-1],
            }
        case {"anyOf": [*json_type_dict_list, {"type": "null"}]}:
            return {
                "type": " | ".join(
                    sorted(
                        {
                            json_type_dict["type"]
                            for json_type_dict in json_type_dict_list
                        }
                    )
                ),
                "format": " | ".join(
                    sorted(
                        {
                            json_type_dict["format"]
                            for json_type_dict in json_type_dict_list
                            if "format" in json_type_dict
                        }
                    )
                ),
                "regex": " | ".join(
                    sorted(
                        {
                            json_type_dict["pattern"]
                            for json_type_dict in json_type_dict_list
                            if "pattern" in json_type_dict
                        }
                    )
                ),
            }
        case {"anyOf": [*json_type_dict_list]}:
            return {
                "format": " | ".join(
                    sorted(
                        {
                            json_type_dict["format"]
                            for json_type_dict in json_type_dict_list
                            if "format" in json_type_dict
                        }
                    )
                )
            }


def main():
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "referentiels").mkdir(exist_ok=True)

    for model in [Structure, Service]:
        with (DOCS_DIR / f"{model.__name__.lower()}.md").open("w") as file:
            file.write(
                jinja2.Template(
                    open(DOCS_DIR / "model.md.j2").read(),
                    autoescape=True,
                    keep_trailing_newline=True,
                ).render(
                    schema=model.model_json_schema(),
                    get_property_type_data=get_property_type_data,
                    snake_case=snake_case,
                    inline_referentiel_size_limit=DOCS_INLINE_REFERENTIAL_SIZE_LIMIT,
                    enum_filenames_by_ref={
                        enum.__name__: filename
                        for enum, filename in ENUM_FILENAMES.items()
                    },
                )
            )

    referentiel_template = open(DOCS_DIR / "referentiel.md.j2").read()

    for enum, filename in ENUM_FILENAMES.items():
        with (DOCS_DIR / "referentiels" / f"{filename}.md").open("w") as file:
            file.write(
                jinja2.Template(
                    referentiel_template,
                    autoescape=True,
                    keep_trailing_newline=True,
                ).render(
                    referentiel=enum.as_dict_list(),
                )
            )


if __name__ == "__main__":
    main()
