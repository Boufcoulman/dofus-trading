import time
import random
from pynput.mouse import Button, Controller
from stopper import escape_on_escape
from read_config import screen_infos, tempo_infos
from pixelisation import change_pixelisation

# Nécessaire pour rendre les cliques souris adéquats
change_pixelisation()


def random_click(min_x, max_x, min_y, max_y):
    """
    Réalise un clique gauche souris aléatoirement dans la zone indiquée
    """
    random_x = min_x + random.random() * (max_x - min_x)
    random_y = min_y + random.random() * (max_y - min_y)
    # On définit la souris, on la place et on clique
    mouse = Controller()
    mouse.position = (random_x, random_y)
    time.sleep(tempo_infos('mouse_tempo')
               + random.random() * tempo_infos('mouse_tempo'))
    mouse.click(Button.left)


def ressource_click(position):
    """
    Envoi un clic aléatoirement sur la fênetre de la ressource à la position
    indiquée
    """
    min_x = screen_infos('rc_min_x')
    max_x = screen_infos('rc_max_x')
    min_y = screen_infos('rc_min_y') + position * screen_infos('line_height')
    max_y = screen_infos('rc_max_y') + position * screen_infos('line_height')

    random_click(min_x, max_x, min_y, max_y)


def null_click():
    """
    Envoi un clic aléatoirement sur la fenêtre hors interface de sorte à ce
    que ça n'entraine aucune action
    """
    min_x = screen_infos('nc_min_x')
    max_x = screen_infos('nc_max_x')
    min_y = screen_infos('nc_min_y')
    max_y = screen_infos('nc_max_y')

    random_click(min_x, max_x, min_y, max_y)


def scroll_down():
    """
    Scroll une fois vers le bas
    """
    mouse = Controller()
    mouse.scroll(0, -1)


def random_walk(time_step):
    """
    Fait bouger aléatoirement la souris
    """
    mouse = Controller()
    escape_on_escape()
    step = 100
    while True:
        randx = random.randint(-step, step)
        randy = random.randint(-step, step)
        mouse.position = (mouse.position[0] + randx, mouse.position[1] + randy)
        time.sleep(time_step)


if __name__ == "__main__":
    random_walk(0.05)
