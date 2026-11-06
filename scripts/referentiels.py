from data_inclusion.schema import v1

VERSION = "v1"

# snake_case basename of the generated docs and json files, for each referentiel
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
