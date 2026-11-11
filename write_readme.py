import pathlib

readme = pathlib.Path('README.md')
readme.write_text('''# Africa Dev Pipeline

Pipeline de donnees sur les indicateurs de developpement humain en Afrique de l Ouest (Guinee, Senegal, Cote d Ivoire, Mali) entre 2000 et 2023.

Source des donnees : API Banque mondiale (wbdata)

## Indicateurs suivis

- Mortalite infantile (pour 1000 naissances)
- Taux de scolarisation primaire (%)
- Acces a l eau potable (% population)
- PIB par habitant (USD)

## Stack

- Python 3.11
- PostgreSQL 15
- dbt-core + dbt-postgres (modele en etoile + tests qualite)
- Docker + Docker Compose
- wbdata (API Banque mondiale)

## Architecture

API Banque mondiale -> fetch_indicators.py -> PostgreSQL (indicators_raw)
                                                      |
                                         dbt stg_indicators (vue)
                                                      |
                      dim_pays + dim_annee + fact_indicators (modele en etoile)

## Modele en etoile

- fact_indicators : table centrale avec les mesures (104 lignes)
- dim_pays : 4 pays (Guinee, Senegal, Cote d Ivoire, Mali)
- dim_annee : 26 annees (2000-2023) avec decennie

## Lancer le projet

1. Installer Docker Desktop et Python 3.11
2. Creer le venv : py -3.11 -m venv venv && venv\\Scripts\\activate
3. Installer les dependances : pip install pandas psycopg2-binary wbdata dbt-core dbt-postgres
4. Lancer les conteneurs : docker compose up -d
5. Ingerer les donnees : python ingestion\\fetch_indicators.py
6. Lancer dbt : cd dbt_project && dbt run && dbt test

## Acces

- PostgreSQL : localhost:5434 (africa / africa)

## Choix techniques

Le modele en etoile separe les dimensions (pays, annee) des faits (mesures) pour faciliter les requetes analytiques. wbdata permet de recuperer les donnees directement depuis l API Banque mondiale sans telechargement manuel. Les 12 tests dbt garantissent la qualite des donnees a chaque execution.
''', encoding='utf-8')
print('README.md cree')
