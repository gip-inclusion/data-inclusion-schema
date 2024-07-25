import json

import pandas as pd
import pydantic
import pydantic_core
import streamlit as st

from data_inclusion import schema
from data_inclusion.schema import score_qualite

CUSTOM_ERROR_MESSAGES_BY_ERROR_TYPE = {
    "enum": (
        "Contient une valeur non autorisée. "
        "Se référer aux valeurs possibles pour ce champ."
    ),
    "set_type": "Doit contenir une liste.",
    "url_scheme": "N'est pas une URL valide.",
    "value_error": "Contient une valeur invalide.",
    "missing": "Est manquant.",
}
structures_label = "🏬 Structures"
services_label = "🤝 Services"
default_structures = [
    {"nom": "structure_1", "id": "1", "source": "dora"},
    {"nom": "structure_2", "id": "2", "courriel": "tata@toto"},
]
default_services = [
    {
        "nom": "service_1",
        "structure_id": "foo",
        "id": "1",
        "source": "dora",
        "frais": ["aucun"],
    },
    {
        "nom": "service_2",
        "id": "2",
        "source": "dora",
        "courriel": "tata@toto",
        "frais": ["gratuit"],
    },
]


def get_error_message(error_detail: pydantic_core.ErrorDetails):
    return CUSTOM_ERROR_MESSAGES_BY_ERROR_TYPE.get(error_detail["type"], "")


def format_error(error_detail: pydantic_core.ErrorDetails):
    champ = error_detail["loc"][0]
    detail = CUSTOM_ERROR_MESSAGES_BY_ERROR_TYPE.get(error_detail["type"], "")

    match error_detail:
        case {"type": "missing"}:
            return {
                "champ": champ,
                "valeur": None,
                "detail": detail,
            }
        case _:
            return {
                "champ": champ,
                "valeur": error_detail["input"],
                "detail": detail,
            }


def list_errors(model_schema, data):
    try:
        model_schema(**data)
    except pydantic.ValidationError as exc:
        return [
            {
                "id": data["id"],
                **format_error(error_detail),
            }
            for error_detail in exc.errors()
        ]

    return []


def highlight_invalid(errors_df, data_df):
    sr1 = pd.Series(
        index=data_df.stack(future_stack=True).index.rename(["id", "champ"]),
        data="",
    )
    sr2 = pd.Series(
        index=errors_df.reset_index().set_index(["id", "champ"]).index,
        data="background-color:hsl(0 100% 80%)",
    )
    sr = sr1.copy()
    sr.update(sr2)
    return sr.unstack()


def get_score(data):
    try:
        service = schema.Service(**data)
    except pydantic.ValidationError:
        return None

    score, criteres = score_qualite.score(service)
    return {"score": score, "criteres": criteres}


st.set_page_config(
    page_title="data·inclusion",
    page_icon="📊",
    layout="wide",
)

progress_bar = st.progress(0)
col1, col2 = st.columns(2)
tab1, tab2 = st.tabs([structures_label, services_label])

col1.markdown("#### 1. Vos structures")
structures_file = col1.file_uploader(
    label="Importer un fichier JSON",
    type=["json"],
    key="structures_file",
)
structures_raw = col1.text_area(
    label=structures_label,
    height=500,
    value=json.dumps(
        json.load(structures_file) if structures_file else default_services, indent=4
    ),
)
if structures_raw is None or len(structures_raw) == 0:
    st.stop()

try:
    structures_data_list = json.loads(structures_raw)
except json.JSONDecodeError as exc:
    col1.error(
        icon="🚨",
        body=f"Erreur de syntaxe JSON :\n```\n{exc.lineno:<5} | {exc.doc.splitlines()[exc.lineno - 1]}\n{'-' * (7 + exc.colno) + '^'}\n```",  # noqa: E501
    )
    st.stop()

progress_bar.progress(0.5)

structures_errors_list = [
    {"ressource": structures_label, **error_detail}
    for structures_dict in structures_data_list
    for error_detail in list_errors(schema.Structure, structures_dict)
]

if len(structures_data_list) > 0:
    tab1.dataframe(
        pd.DataFrame(structures_data_list).set_index("id")
        if len(structures_errors_list) == 0
        else pd.DataFrame(structures_data_list)
        .set_index("id")
        .style.apply(
            lambda df: highlight_invalid(
                pd.DataFrame(structures_errors_list).set_index("id"), df
            ),
            axis=None,
        ),
        use_container_width=True,
    )


col2.markdown("#### 2. Vos services")
services_file = col2.file_uploader(
    label="Importer un fichier JSON",
    type=["json"],
    key="services_file",
)
services_raw = col2.text_area(
    label=services_label,
    height=500,
    value=json.dumps(
        json.load(services_file) if services_file else default_services, indent=4
    ),
)
if services_raw is None or len(services_raw) == 0:
    st.stop()

try:
    services_data_list = json.loads(services_raw)
except json.JSONDecodeError as exc:
    col2.error(
        icon="🚨",
        body=f"Erreur de syntaxe JSON :\n```\n{exc.lineno:<5} | {exc.doc.splitlines()[exc.lineno - 1]}\n{'-' * (7 + exc.colno) + '^'}\n```",  # noqa: E501
    )
    st.stop()

progress_bar.progress(1.0)

services_data_list = json.loads(services_raw)
services_errors_list = [
    {"ressource": services_label, **error_detail}
    for services_dict in services_data_list
    for error_detail in list_errors(schema.Service, services_dict)
]
if len(services_data_list) > 0:
    tab2.dataframe(
        pd.DataFrame(services_data_list).set_index("id")
        if len(services_errors_list) == 0
        else pd.DataFrame(services_data_list)
        .set_index("id")
        .style.apply(
            lambda df: highlight_invalid(
                pd.DataFrame(services_errors_list).set_index("id"), df
            ),
            axis=None,
        ),
        use_container_width=True,
        column_config={
            field_name: st.column_config.Column(help=field_info.description)
            for field_name, field_info in schema.Service.model_fields.items()
        },
    )


all_errors = structures_errors_list + services_errors_list

if len(all_errors) > 0:
    st.error(
        icon="🚨",
        body=f"{len(all_errors)} erreurs détectées",
    )
    st.dataframe(
        pd.DataFrame(all_errors).set_index(["ressource", "id"]),
        column_order=["champ", "detail", "valeur"],
        use_container_width=True,
    )
else:
    st.success("Aucune erreur 🥳", icon="✅")
    st.balloons()

criteres = [
    {
        "ressource": services_label,
        "id": service_data["id"],
        "critere": critere_name,
    }
    for service_data in services_data_list
    if (score := get_score(service_data))
    for critere_name, critere_value in score["criteres"].items()
    if critere_value != 1
]

if len(criteres) > 0:
    st.warning(
        icon="⚠️",
        body=f"{len(criteres)} critères de qualité non respectés",
    )
    st.dataframe(
        pd.DataFrame(criteres).set_index(["ressource", "id"]),
        use_container_width=True,
    )
