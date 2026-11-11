SELECT
    id,
    pays,
    annee,
    mortalite_infantile,
    scolarisation,
    eau_potable,
    pib_par_habitant
FROM {{ ref('stg_indicators') }}
