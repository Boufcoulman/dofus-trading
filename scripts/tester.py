from screen import screen_rectangle, change_colors
from screen import treshold_black, treshold_all
from parsing import data_extract
from read_config import screen_infos, tempo_infos
from treatment import get_start_y, name_treatment
from PIL import Image
import psutil
import time


def wait_test(function):
    """
    Permet de bloquer le programme tant que
    la fonction en argument ne renvoi pas true
    """
    while not function():
        time.sleep(tempo_infos('test_tempo'))


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
    return text in the_text


def process_running(process_name):
    """
    Permet de savoir si un processus est lancé
    """
    return (process_name in
            [p.info['name'] for
             p in psutil.process_iter(attrs=['name'])])


def launcher_launched():
    """
    Permet de savoir si le launcher Ankama est lancé
    """
    return process_running('Ankama Launcher.exe')


def dofus_launched():
    """
    Permet de savoir si dofus est lancé
    """
    return process_running('Dofus.exe')


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


def runes_showed():
    """
    Permet de savoir si les runes sont bien visibles
    """
    return bool(name_treatment(get_start_y(0)).strip())


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
    process_running('Ankama Launcher.exe')
    wait_test(launcher_launched)
