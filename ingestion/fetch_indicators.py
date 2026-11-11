import wbdata
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import datetime

PAYS = ["GN", "SN", "CI", "ML"]
INDICATEURS = {
    "SH.DYN.MORT": "Mortalite infantile (pour 1000 naissances)",
    "SE.PRM.ENRR": "Taux de scolarisation primaire (%)",
    "SH.H2O.BASW.ZS": "Acces eau potable (% population)",
    "NY.GDP.PCAP.CD": "PIB par habitant (USD)"
}

def fetch_data():
    print("Recuperation des donnees Banque mondiale...")
    df = wbdata.get_dataframe(INDICATEURS, country=PAYS)
    df = df.reset_index()
    df.columns = ["pays", "annee", "mortalite_infantile", "scolarisation", "eau_potable", "pib_par_habitant"]
    df["annee"] = df["annee"].astype(str).str[:4].astype(int)
    df = df[df["annee"] >= 2000]
    df = df.dropna(subset=["mortalite_infantile", "scolarisation", "eau_potable", "pib_par_habitant"], how="all")
    print(f"{len(df)} lignes recuperees")
    return df

def load_to_postgres(df):
    conn = psycopg2.connect(host="127.0.0.1", port=5434, dbname="africa", user="africa", password="africa")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS indicators_raw (
            id SERIAL PRIMARY KEY,
            pays VARCHAR(100),
            annee INTEGER,
            mortalite_infantile FLOAT,
            scolarisation FLOAT,
            eau_potable FLOAT,
            pib_par_habitant FLOAT,
            inserted_at TIMESTAMP DEFAULT NOW()
        )
    """)

    cur.execute("TRUNCATE TABLE indicators_raw")

    rows = [tuple(row) for row in df[["pays","annee","mortalite_infantile","scolarisation","eau_potable","pib_par_habitant"]].values]
    execute_values(cur, """
        INSERT INTO indicators_raw (pays, annee, mortalite_infantile, scolarisation, eau_potable, pib_par_habitant)
        VALUES %s
    """, rows)

    conn.commit()
    cur.close()
    conn.close()
    print("Donnees chargees dans PostgreSQL")

if __name__ == "__main__":
    df = fetch_data()
    load_to_postgres(df)
