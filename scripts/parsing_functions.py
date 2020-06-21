
import pytesseract
from PIL import Image


def text_extract(filepath):
    """
    Fonction de récupération de texte d'une image en utilisant pytesseract
    """
    text = pytesseract.image_to_string(Image.open(filepath))
    return text


def price_parsing(text):
    """
    Fonction permettant de vérifier si un texte correspond à un prix et de le
    remettre en forme avant ajout dans la base de données le cas échéant
    """
    parsed_text = text
    parsed_status = 1
    return parsed_status, parsed_text


def ressource_parsing(text):
    """
    Fonction permettant de vérifier si un texte correspond à un prix et de le
    remettre en forme avant ajout dans la base de données le cas échéant
    """
    parsed_text = text
    parsed_status = 1
    return parsed_status, parsed_text


# Debug zone


# print(text_extract('images/test_prix_done.png'))
# print(text_extract('images/test_fenetre_done.png'))
# print(ressource_parsing('lol')[0])
