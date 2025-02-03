import json
import pathlib

from data_inclusion.schema import (
    Frais,
    LabelNational,
    MobilisablePar,
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


def main():
    output_dir = pathlib.Path() / "schemas"
    output_dir.mkdir(exist_ok=True)

    for model in [Structure, Service]:
        with (output_dir / f"{model.__name__.lower()}.json").open("w") as file:
            json.dump(
                model.model_json_schema(),
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
        ("mobilisable-par.json", MobilisablePar),
        ("profils.json", Profil),
        ("thematiques.json", Thematique),
        ("typologies-de-services.json", TypologieService),
        ("typologies-de-structures.json", Typologie),
        ("zones-de-diffusion-types.json", ZoneDiffusionType),
    ]

    for filename, enum in enum_x_file_tuples_list:
        with (output_dir / "extra" / filename).open("w") as file:
            json_dump(enum.as_dict_list(), file)


if __name__ == "__main__":
    """
    Usage:
        $ python -m data_inclusion.schema
    """
    main()
