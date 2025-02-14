import json
import pathlib

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
    TypologieService,
    TypologieStructure,
    ZoneDiffusionType,
)

SCHEMAS_DIR = pathlib.Path() / "schemas"

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


def json_dump(obj, file):
    json.dump(
        obj,
        file,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )


def main():
    SCHEMAS_DIR.mkdir(exist_ok=True)
    (SCHEMAS_DIR / "extra").mkdir(exist_ok=True)

    for model in [Structure, Service]:
        with (SCHEMAS_DIR / f"{model.__name__.lower()}.json").open("w") as file:
            json_dump(model.model_json_schema(), file)

    for enum, filename in ENUM_FILENAMES.items():
        with (SCHEMAS_DIR / "extra" / f"{filename.replace('_', '-')}.json").open(
            "w"
        ) as file:
            json_dump(enum.as_dict_list(), file)


if __name__ == "__main__":
    main()
