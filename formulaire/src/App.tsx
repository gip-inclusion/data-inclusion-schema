import _ from "lodash";

import { useForm, useFieldArray, useFormContext, FormProvider } from "react-hook-form";
import { ajvResolver } from "@hookform/resolvers/ajv";
import { fullFormats } from "ajv-formats/dist/formats";

import serviceSchema from "../../schemas/services.json";

import { fr } from "@codegouvfr/react-dsfr";

const propertiesGroups = {
    "🪪 Identification": [
        "source",
        "structure_id",
        "id",
        "lien_source",
        "date_maj",
        "page_web",
        "date_creation",
        "date_suspension"
    ],
    "📝 Descriptif": ["nom", "presentation_resume", "presentation_detail", "thematiques", "types"],
    "✅ Conditions d'accès": [
        "frais",
        "frais_autres",
        "cumulable",
        "pre_requis",
        "justificatifs",
        "profils",
        "zone_diffusion_code",
        "zone_diffusion_nom",
        "zone_diffusion_type",
        "recurrence",
        "modes_accueil"
    ],
    "📍 Localisation": [
        "adresse",
        "complement_adresse",
        "code_postal",
        "code_insee",
        "commune",
        "longitude",
        "latitude"
    ],
    "📞 Contact": [
        "contact_public",
        "contact_nom_prenom",
        "telephone",
        "courriel",
        "prise_rdv",
        "formulaire_en_ligne"
    ]
};

const Field = ({ name, path, schema }: any) => {
    const { title, description } = schema;
    const { register, getFieldState, formState } = useFormContext();
    const fieldState = getFieldState(path, formState);
    const propertyType = schema.anyOf?.[0].type || schema.type;
    const propertyFormat = schema.anyOf?.[0].format || schema.format;

    const labelElement = (
        <label className="fr-label" htmlFor={path}>
            {title}
            {description && <span className="fr-hint-text">{description}</span>}
        </label>
    );

    if (propertyType === "boolean") {
        return (
            <fieldset className="fr-fieldset">
                <div className="fr-fieldset__element">
                    <div
                        className={
                            "fr-checkbox-group " + (fieldState.invalid ? "fr-checkbox-group--error" : "")
                        }
                    >
                        <input type="checkbox" id={path} {...register(path)} />
                        {labelElement}
                    </div>
                </div>
            </fieldset>
        );
    }

    return (
        <div className={"fr-input-group " + (fieldState.invalid ? "fr-input-group--error" : "")}>
            {labelElement}
            {name === "presentation_detail" ? (
                <textarea
                    style={{ resize: "vertical" }}
                    rows={10}
                    className={"fr-input " + (fieldState.invalid ? "fr-input--error" : "")}
                    {...register(path, { setValueAs: v => (v === "" ? undefined : v) })}
                />
            ) : schema?.anyOf?.[0]?.items?.$ref ? (
                <select
                    multiple
                    size={Math.min(
                        (serviceSchema.$defs[schema.anyOf[0].items.$ref.replace("#/$defs/", "") as keyof typeof serviceSchema.$defs] as any).enum.length,
                        20
                    )}
                    className={"fr-select " + (fieldState.invalid ? "fr-select--error" : "")}
                    {...register(path)}
                >
                    {(serviceSchema.$defs[schema.anyOf[0].items.$ref.replace("#/$defs/", "") as keyof typeof serviceSchema.$defs] as any).enum.map(
                        (value: any) => (
                            <option key={value} value={value}>
                                {value}
                            </option>
                        )
                    )}
                </select>
            ) : (
                <input
                    className={"fr-input " + (fieldState.invalid ? "fr-input--error" : "")}
                    type={
                        propertyFormat === "date"
                            ? "date"
                            : propertyType === "number"
                              ? "number"
                              : "text"
                    }
                    step={propertyType === "number" ? "any" : undefined}
                    placeholder={propertyFormat === "uri" ? "https://" : ""}
                    {...register(path, {
                        setValueAs: v =>
                            v === "" ? undefined : propertyType === "number" ? parseFloat(v) : v
                    })}
                />
            )}
            {fieldState.invalid && <div className="fr-error-text">{fieldState.error?.message}</div>}
        </div>
    );
};

function Form() {
    const methods = useForm({
        resolver: async (data, context, options) => {
            const result = await ajvResolver(serviceSchema as any, { formats: fullFormats })(
                data.services,
                context,
                options
            );
            console.log(result.values);
            if (_.isEmpty(result.errors)) {
                return { errors: {}, values: { services: result.values } };
            } else {
                return { errors: { services: result.errors }, values: {} };
            }
        },
        mode: "onChange"
    });
    const { control, handleSubmit } = methods;
    const { fields, append, remove } = useFieldArray({
        control,
        name: "services"
    });

    const onSubmit = (data: any) => {
        const blob = new Blob([JSON.stringify(data.services, null, 2)], { type: "application/json" });
        const url = URL.createObjectURL(blob);
        const tempAnchorElement = document.createElement("a");
        tempAnchorElement.href = url;
        tempAnchorElement.target = "_blank";
        tempAnchorElement.download;
        tempAnchorElement.click();
        document.removeChild(tempAnchorElement);
        URL.revokeObjectURL(url);
    };

    return (
        <FormProvider {...methods}>
            <form onSubmit={handleSubmit(onSubmit)}>
                {fields.map((field, index) => (
                    <>
                        <div key={field.id}>
                            <fieldset className="fr-fieldset fr-background-alt--grey">
                                <legend className="fr-fieldset__legend">
                                    <h4>Service {index + 1}</h4>
                                    <button
                                        className={fr.cx(
                                            "fr-btn--tertiary-no-outline",
                                            "fr-icon-delete-line"
                                        )}
                                        onClick={() => remove(index)}
                                    >
                                        Supprimer
                                    </button>
                                </legend>
                                <div className="fr-fieldset__element">
                                    {Object.entries(propertiesGroups).map(([groupName, groupFields]) => (
                                        <fieldset className="fr-fieldset">
                                            <legend className="fr-fieldset__legend">{groupName}</legend>
                                            <div className="fr-fieldset__element">
                                                {Object.entries(serviceSchema.$defs.Service.properties)
                                                    .filter(([fieldName,]) =>
                                                        groupFields.includes(fieldName)
                                                    )
                                                    .map(([fieldName, fieldSchema]) => (
                                                        <Field
                                                            key={fieldName}
                                                            name={fieldName}
                                                            path={`services.${index}.${fieldName}`}
                                                            schema={fieldSchema}
                                                        />
                                                    ))}
                                            </div>
                                        </fieldset>
                                    ))}
                                    <fieldset className="fr-fieldset">
                                        <legend className="fr-fieldset__legend">Autres</legend>
                                        <div className="fr-fieldset__element">
                                            {Object.entries(serviceSchema.$defs.Service.properties)
                                                .filter(
                                                    ([fieldName,]) =>
                                                        !Object.values(propertiesGroups).some(g =>
                                                            g.includes(fieldName)
                                                        )
                                                )
                                                .map(([fieldName, fieldSchema]) => (
                                                    <Field
                                                        key={fieldName}
                                                        name={fieldName}
                                                        path={`services.${index}.${fieldName}`}
                                                        schema={fieldSchema}
                                                    />
                                                ))}
                                        </div>
                                    </fieldset>
                                </div>
                            </fieldset>
                        </div>
                        <p className={fr.cx("fr-hr")} />
                    </>
                ))}
                <div className="fr-grid-row">
                    <div className="fr-col">
                        <div className="fr-btns-group">
                            <button
                                className="fr-btn"
                                onClick={() =>
                                    append({
                                        id: crypto.randomUUID(),
                                        date_maj: new Date().toISOString().substring(0, 10)
                                    })
                                }
                            >
                                Ajouter un service
                            </button>
                            <button className="fr-btn" type="submit">
                                Télécharger
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </FormProvider>
    );
}

function App() {
    return (
        <div className="fr-container">
            <div className="fr-grid-row fr-grid-row--center">
                <div className="fr-col-8">
                    <Form />
                </div>
            </div>
        </div>
    );
}

export default App;
