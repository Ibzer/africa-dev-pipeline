SELECT DISTINCT
    annee,
    CASE
        WHEN annee BETWEEN 2000 AND 2009 THEN '2000s'
        WHEN annee BETWEEN 2010 AND 2019 THEN '2010s'
        WHEN annee >= 2020 THEN '2020s'
    END AS decennie
FROM {{ ref('stg_indicators') }}
