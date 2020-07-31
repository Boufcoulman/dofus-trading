from read_config import db_path

db_path = db_path()


def add_ressource_line(ressource, timestamp, moyen, unite, dix, cent):
    """
    Permet d'ajouter la recupération d'une donnée dans la base
    """
    db_csv = open(db_path, "a")
    db_csv.write("{0};{1};{2};{3};{4};{5}\n".format(
        timestamp, ressource, moyen, unite, dix, cent))
    db_csv.close


if __name__ == "__main__":
    add_ressource_line('tomate', '31072020 23', 540, 520, 5400, 56000)
