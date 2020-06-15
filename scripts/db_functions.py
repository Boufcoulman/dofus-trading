import sqlite3

dbpath = 'E:/Donnees/Programmation/dofus-trading-database/dofus-trading.db'
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()


def add_ressource_line(ressource, timestamp, moyen, unite, dix, cent):
    # Création de la table ressource si non existante
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS """+ressource+"""(
         timestamp TEXT,
         prix_moyen INTERGER,
         prix_unitaire INTERGER,
         prix_dizaine INTERGER,
         prix_centaine INTERGER
    )
    """)

    # Ajout de la récupération de données
    cursor.execute("""
    INSERT INTO """+ressource+"""(
        timestamp,
        prix_moyen,
        prix_unitaire,
        prix_dizaine,
        prix_centaine
        ) VALUES(?, ?, ?, ?, ?)""",
                   (timestamp, moyen, unite, dix, cent)
                   )
    conn.commit()
    conn.close()


# Debug zone

# add_ressource_line('tomate', '20200613_075146', 1200, 950, 11000, 122000)
