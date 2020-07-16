
import pytesseract
from PIL import Image
import re


def data_extract(filepath):
    """
    Fonction de récupération de texte/nombre
    d'une image en utilisant pytesseract
    /! Ne semble pas marcher pour des chiffres uniques
    """
    text = pytesseract.image_to_string(Image.open(filepath))
    return text


def price_parsing(price):
    """
    Fonction permettant de vérifier si un texte correspond à un prix et de le
    remettre en forme avant ajout dans la base de données le cas échéant.
    """
    parsed_price = price.replace(".", "").replace(" ", "")
    if parsed_price.isdigit():
        return parsed_price
    else:
        return ''


def lot_parsing(text):
    """
    Fonction permettant de vérifier si un texte correspond à un nombre de lot
    et de récupérer la taille du lot le cas échéant
    """
    parsed_text = text.replace(".", "").replace(" ", "")
    lot_number = re.sub(r'^lotde([0-9]*)', r'\1', parsed_text)

    if lot_number in ['1', '10', '100']:
        return lot_number
    else:
        return '0'


# Debug zone

# print(price_parsing('124 572.12'))
# print(text_extract('images/test_prix_done.png'))
# print(text_extract('images/test_fenetre_done.png'))
# print(ressource_parsing('lol')[0])
