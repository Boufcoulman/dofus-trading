from screen import screen_rectangle, change_colors
from parsing import data_extract, lot_parsing, price_parsing
from database import add_ressource_line
import time
from read_config import screen_infos


def get_start_y(position):
    """
    Renvoi l'ordonnee de la position voulue dans l'hdv
    """
    return screen_infos('start_y') + position * screen_infos('s_line_height')


def name_treatment(start_y):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer son nom.
    """
    image_name = 'images/ressource_name.png'

    # Capture du nom de la ressource
    start_x = screen_infos('name_start_x')
    width = screen_infos('name_width')
    height = screen_infos('parsing_height')
    screen_rectangle(image_name, start_x, start_y, width, height)

    # Extraction du nom de la ressource
    result_path = change_colors(image_name)
    ressource_name = data_extract(result_path)

    return ressource_name


def price_treatment(image_name):
    """
    Fonction à appeler pour récupérer un prix depuis une image.
    """
    # Extraction du prix moyen
    result_path = change_colors(image_name)
    raw_price = data_extract(result_path)

    # Récupère le prix et indique si ça correspond effectivement à un prix
    price = price_parsing(raw_price)

    return price


def mid_price_treatment(start_y):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer son prix
    moyen.
    """
    image_name = 'images/mid_price.png'

    # Capture du prix moyen
    start_x = screen_infos('mid_price_start_x')
    width = screen_infos('mid_price_width')
    height = screen_infos('parsing_height')
    screen_rectangle(image_name, start_x, start_y, width, height)

    # Récupération du prix à ajouter dans la database
    mid_price = price_treatment(image_name)

    return mid_price


def lot_number_treatment(start_y):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer
    son numéro de lot.
    """
    image_name = 'images/lot_number.png'

    # Capture du nombre de lot
    start_x = screen_infos('lot_number_start_x')
    width = screen_infos('lot_number_width')
    height = screen_infos('parsing_height')
    screen_rectangle(image_name, start_x, start_y, width, height)

    # Récupération de l'information du lot
    result_path = change_colors(image_name)
    raw_lot_number = data_extract(result_path)

    # Récupère le nombre du lot et renvoi 0 si pas bon
    lot_number = lot_parsing(raw_lot_number)

    return lot_number


def lot_price_treatment(start_y):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer
    son prix de lot.
    """
    image_name = 'images/lot_price.png'

    # Capture du prix de lot
    start_x = screen_infos('lot_price_start_x')
    width = screen_infos('lot_price_width')
    height = screen_infos('parsing_height')
    screen_rectangle(image_name, start_x, start_y, width, height)

    # Récupération du prix à ajouter dans la base de données
    lot_price = price_treatment(image_name)

    return lot_price


def ressource_treatment(position):
    """
    Fonction à appeler quand une ressource est cliquée pour enregistrer
    ses données dans la base.
    En argument la position dans l'hdv : 0 tout en haut, 13 tout en bas.
    La fonction n'est exploitable que de 0 à 10 inclus.
    """
    # Calcul de l'ordonnée initiale de la ressource
    start_y = get_start_y(position)

    # Pour chaque portion utile, capture de la portion, changement de couleur,
    # extraction de la donnée, parsing et vérification de la données
    # Un traitement pour le nom, un traitement pour le prix moyen puis
    # une boucle sur les 3 lignes suivantes

    # Récupération du nom de la ressource
    ressource_name = name_treatment(start_y)

    # Récupération du prix moyen
    mid_price = mid_price_treatment(start_y)

    # Récupération des prix unitaire, dizaine et centaine
    table_lot = {'1': '', '10': '', '100': ''}
    for line in range(1, 4):
        # Pour chaque ligne, on test si on detecte lot de 1, 10 ,100 et on
        # passe au parsing du prix si c'est le cas
        start_y_line = get_start_y(position + line)

        # Récupération du numéro de lot (1, 10 ou 100)
        lot_number = lot_number_treatment(start_y_line)
        # Récupération du prix associé et ajout dans la table_lot
        if lot_number in ['1', '10', '100']:
            table_lot[lot_number] = lot_price_treatment(start_y_line)

    # Récupération du timestamp
    timestamp = time.strftime("%d%m%Y %H", time.localtime())

    # Ajout des données dans la base s'il y a un prix moyen
    if mid_price.isdigit():
        add_ressource_line(ressource_name, timestamp, mid_price,
                           table_lot['1'], table_lot['10'], table_lot['100'])
    # Sortie de debug
    return ressource_name, mid_price, table_lot


def nbr_lots(position):
    """
    Récupère le nombre de ligne indiquant un lot pour la position donnée
    """
    compte_lots = 0
    # Récupération du nombre de ligne contenant "lot de"
    for line in range(1, 4):
        # Pour chaque ligne, on test si on detecte lot de 1, 10 ,100 et on
        # passe au parsing du prix si c'est le cas
        start_y_line = get_start_y(position + line)

        # Récupération du numéro de lot (1, 10 ou 100)
        lot_number = lot_number_treatment(start_y_line)

        # Si c'est bien un nombre valide on incrémente le compte
        if lot_number in ['1', '10', '100']:
            compte_lots += 1

    return compte_lots


if __name__ == "__main__":
    print(mid_price_treatment(215))
    print(mid_price_treatment(215).isdigit())
