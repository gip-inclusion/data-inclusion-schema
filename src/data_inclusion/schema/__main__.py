import json
import pathlib

from data_inclusion.schema import models


def main():
    output_dir = pathlib.Path() / "schemas"
    output_dir.mkdir(exist_ok=True)

    # schémas

    with (output_dir / "structures.json").open("w") as file:
        json.dump(models.generate_structures_json_schema(), file, indent=2)

    with (output_dir / "services.json").open("w") as file:
        json.dump(models.generate_services_json_schema(), file, indent=2)

    # fichiers supplémentaires documentant les énumérations

    (output_dir / "extra").mkdir(exist_ok=True)

    enum_x_file_tuples_list = [
        ("typologies-de-structures.json", models.Typologie),
        ("labels-nationaux.json", models.LabelNational),
        ("thematiques.json", models.Thematique),
        ("typologies-de-services.json", models.TypologieService),
        ("frais.json", models.Frais),
        ("profils.json", models.Profil),
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
