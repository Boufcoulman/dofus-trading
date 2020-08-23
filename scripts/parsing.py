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
    cleaned_text = re.sub(r'[^0-9A-Za-z ]', r'', text)
    return cleaned_text


def price_parsing(price):
    """
    Fonction permettant de vérifier si un texte correspond à un prix et de le
    remettre en forme avant ajout dans la base de données le cas échéant.
    """
    parsed_price = re.sub(r'[^0-9]', r'', price)
    if parsed_price.isdigit():
        return parsed_price
    else:
        return ''


def lot_parsing(text):
    """
    Fonction permettant de vérifier si un texte correspond à un nombre de lot
    et de récupérer la taille du lot le cas échéant
    """
    parsed_text = re.sub(r'[^0-9]', r'', text)
    if parsed_text in ['100', '10', '1']:
        return parsed_text
    else:
        return '0'
    # lot_number = re.sub(r'^lotde([0-9]*).*\n?', r'\1', parsed_text)


if __name__ == "__main__":
    print(data_extract('images/ressource_name_bw.png'))
