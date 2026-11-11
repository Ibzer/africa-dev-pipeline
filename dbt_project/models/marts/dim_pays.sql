SELECT
    DISTINCT pays AS pays_code,
    CASE pays
        WHEN 'Cote d''Ivoire' THEN 'Cote d''Ivoire'
        WHEN 'Guinea' THEN 'Guinee'
        WHEN 'Mali' THEN 'Mali'
        WHEN 'Senegal' THEN 'Senegal'
        ELSE pays
    END AS pays_nom,
    'Afrique de l''Ouest' AS region
FROM {{ ref('stg_indicators') }}
