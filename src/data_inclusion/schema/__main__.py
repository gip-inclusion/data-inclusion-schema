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
    Typologie,
    TypologieService,
    ZoneDiffusionType,
)


def main():
    output_dir = pathlib.Path() / "schemas"
    output_dir.mkdir(exist_ok=True)

    with (output_dir / "structures.json").open("w") as file:
        json.dump(
            Structure.model_list_json_schema(
                title="Structures de l'insertion",
                id=(
                    "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
                    "/main/structures.json"
                ),
                description="",
            ),
            file,
            indent=2,
        )

    with (output_dir / "services.json").open("w") as file:
        json.dump(
            Service.model_list_json_schema(
                title="Services de l'insertion",
                id=(
                    "https://raw.githubusercontent.com/betagouv/data-inclusion-schema"
                    "/main/services.json"
                ),
                description="",
            ),
            file,
            indent=2,
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
            json.dump(
                enum.as_dict_list(),
                file,
                indent=2,
                ensure_ascii=False,
            )


if __name__ == "__main__":
    """
    Usage:
        $ python -m data_inclusion.schema
    """
    main()
