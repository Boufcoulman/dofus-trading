import sqlite3

dbpath = 'E:/Donnees/Programmation/dofus-trading-database/dofus-trading.db'


def add_ressource_line(ressource, timestamp, moyen, unite, dix, cent):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    # Création de la table ressource si non existante
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dofus_trading_table(
         timestamp TEXT,
         ressource TEXT,
         prix_moyen INTEGER,
         prix_unitaire INTEGER,
         prix_dizaine INTEGER,
         prix_centaine INTEGER
    )
    """)

    # Ajout de la récupération de données
    cursor.execute("""
    INSERT INTO dofus_trading_table(
        timestamp,
        ressource,
        prix_moyen,
        prix_unitaire,
        prix_dizaine,
        prix_centaine
        ) VALUES(?, ?, ?, ?, ?, ?)""",
                   (timestamp, ressource, moyen, unite, dix, cent)
                   )
    conn.commit()
    conn.close()


# Debug zone

# add_ressource_line('tomate', '20200613_075146', 1200, 950, 11000, 122000)
