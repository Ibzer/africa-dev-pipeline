SELECT
    id,
    pays,
    annee,
    mortalite_infantile,
    scolarisation,
    eau_potable,
    pib_par_habitant,
    inserted_at
FROM {{ source('public', 'indicators_raw') }}
WHERE annee IS NOT NULL
  AND pays IS NOT NULL
