from screen import screen_rectangle, change_colors
from screen import treshold_black, treshold_all
from parsing import data_extract
from read_config import screen_infos
from treatment import get_start_y
from PIL import Image
import time


def end_of_scroll():
    """
    Détecte si on atteind le bas de l'hdv
    """
    image_name = 'images/check_if_bottom.png'
    # Capture du pixel
    x_pixel = screen_infos('x_pixel')
    y_pixel = screen_infos('y_pixel')
    screen_rectangle(image_name, x_pixel, y_pixel, 1, 1)

    # Vérification de la teinte du pixel
    img_scroll = Image.open(image_name)
    pix_scroll = list(img_scroll.getdata())
    r = pix_scroll[0][0]
    is_bottom = r > 50

    return is_bottom


def is_ok_color(value, goal, tolerance):
    return value >= goal - tolerance and value <= goal + tolerance


def is_ok_pixel(x, y, r=50, g=50, b=50, tr=5, tg=5, tb=5):
    """
    Indique si un pixel est dans la bonne plage de couleur
    """
    image_name = 'images/check_pixel.png'
    # Capture du pixel
    screen_rectangle(image_name, x, y, 1, 1)

    # Véification de la teinte du pixel
    img_pixel = Image.open(image_name)
    pixel = list(img_pixel.getdata())
    mr, mg, mb = pixel[0]
    print(mr, mg, mb)
    is_ok_red = is_ok_color(mr, r, tr)
    is_ok_blue = is_ok_color(mb, b, tb)
    is_ok_green = is_ok_color(mg, g, tg)
    print(is_ok_red, is_ok_green, is_ok_blue)


def test():
    image_name = 'images/ressource_name.png'
    img_pixel = Image.open(image_name)
    pixel = list(img_pixel.getdata())
    print(pixel)


def is_text(text, start_x, start_y, width, height,
            test=treshold_all, treshold=100):
    """
    Renvoi true si le texte mis en entrée est détecté dans la zone
    ciblée, avec la formule de test spécifiée.
    """
    image_name = 'images/check_if_text.png'
    # Capture de la fenêtre
    screen_rectangle(image_name, start_x, start_y, width, height)

    # Récupération de l'info texte
    result_path = change_colors(image_name, test, treshold)
    the_text = data_extract(result_path)
    print(the_text)
    return text in the_text


def ready_to_launch():
    """
    Permet de savoir si le jeu est prêt à être lancé depuis le launcher
    """
    start_x = screen_infos('start_button_x')
    start_y = screen_infos('start_button_y')
    width = screen_infos('start_button_width')
    height = screen_infos('start_button_height')
    return is_text('JOUER', start_x, start_y, width, height,
                   treshold_black, 210)


def in_brakmar():
    """
    Permet de savoir si l'on est bien connecté à Brakmar
    """
    start_x = screen_infos('brak_pos_x')
    start_y = screen_infos('brak_pos_y')
    width = screen_infos('brak_pos_width')
    height = screen_infos('brak_pos_height')
    return is_text('Brakmar', start_x, start_y, width, height)


def in_rune_shop():
    """
    Permet de savoir si l'hotel de vente des runes a bien chargé
    """
    start_x = screen_infos('rune_pos_x')
    start_y = screen_infos('rune_pos_y')
    width = screen_infos('rune_pos_width')
    height = screen_infos('rune_pos_height')
    return is_text('Rune de forgemagie', start_x, start_y, width, height)


def is_clicked(position):
    """
    Permet de savoir si la ressource est cliquée
    """
    start_x = screen_infos('buy_button_x')
    start_y = get_start_y(position + 1)
    width = screen_infos('buy_button_width')
    height = screen_infos('parsing_height')
    return is_text('Acheter', start_x, start_y, width, height,
                   treshold_black)


if __name__ == "__main__":
    time.sleep(5)
    print(is_clicked(0))
