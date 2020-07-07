from image_functions import screen_rectangle, change_colors
from parsing_functions import data_extract, lot_parsing, price_parsing
from db_functions import add_ressource_line
import time


def name_treatment(ordonnee):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer son nom.
    """
    image_name = 'images/ressource_name.png'

    # Capture du nom de la ressource
    screen_rectangle(image_name, 665, ordonnee, 235, 25)

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


def mid_price_treatment(ordonnee):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer son prix
    moyen.
    """
    image_name = 'images/mid_price.png'

    # Capture du prix moyen
    screen_rectangle(image_name, 1070, ordonnee, 100, 25)

    # Récupération du prix à ajouter dans la database
    mid_price = price_treatment(image_name)

    return mid_price


def lot_number_treatment(ordonnee):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer
    son numéro de lot.
    """
    image_name = 'images/lot_number.png'

    # Capture du nombre de lot
    screen_rectangle(image_name, 830, ordonnee, 70, 25)

    # Récupération de l'information du lot
    result_path = change_colors(image_name)
    raw_lot_number = data_extract(result_path)

    # Récupère le nombre du lot et renvoi 0 si pas bon
    lot_number = lot_parsing(raw_lot_number)

    return lot_number


def lot_price_treatment(ordonnee):
    """
    Fonction à appeler quand une ressource est cliquée pour récupérer
    son prix de lot.
    """
    image_name = 'images/lot_price.png'

    # Capture du prix de lot
    screen_rectangle(image_name, 940, ordonnee, 80, 25)

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
    ordonnee = 215 + position * 46

    # Pour chaque portion utile, capture de la portion, changement de couleur,
    # extraction de la donnée, parsing et vérification de la données
    # Un traitement pour le nom, un traitement pour le prix moyen puis
    # une boucle sur les 3 lignes suivantes

    # Récupération du nom de la ressource
    ressource_name = name_treatment(ordonnee)

    # Récupération du prix moyen
    mid_price = mid_price_treatment(ordonnee)

    # Récupération des prix unitaire, dizaine et centaine
    table_lot = {'1': 0, '10': 0, '100': 0}
    for ligne in range(1, 4):
        # Pour chaque ligne, on test si on detecte lot de 1, 10 ,100 et on
        # passe au parsing du prix si c'est le cas
        ordonnee_ligne = ordonnee + ligne * 46

        # Récupération du numéro de lot (1, 10 ou 100)
        lot_number = lot_number_treatment(ordonnee_ligne)
        # Récupération du prix associé et ajout dans la table_lot
        if lot_number in ['1', '10', '100']:
            table_lot[lot_number] = lot_price_treatment(ordonnee_ligne)

    # Récupération du timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())

    # Ajout des données dans la base s'il y a un prix moyen
    if mid_price != 0:
        add_ressource_line(ressource_name, timestamp, mid_price,
                           table_lot['1'], table_lot['10'], table_lot['100'])

    # Une fois toutes les portions traitées, ajout de la données
    # à la base de données avec le timestamp actuel

    # A priori +46 en ordonnée pour passer d'une ressource à la suivante
    #
    # nom ressource :       (665, 215, 235, 25)
    # prix moyen :          (1070, 215, 100, 25)
    # premier champ lot :   (830, 261, 70, 25)
    # premier prix lot :    (940, 261, 80, 25)
    # deuxieme champ lot :  (830, 307, 70, 25)
    # deuxieme prix lot :   (940, 307, 80, 25)
    # troisieme champ lot : (830, 353, 70, 25)
    # troisieme prix lot :  (940, 353, 80, 25)

    # Sortie de debug
    return ressource_name, mid_price, table_lot

# Debug zone


table_lot = ressource_treatment(4)
print(table_lot)
