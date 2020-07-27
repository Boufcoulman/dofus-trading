import time
import random
from pynput.mouse import Button, Controller
from stopper import escape_on_escape
from read_config import screen_infos


def random_click(min_x, max_x, min_y, max_y):
    """
    Réalise un clique gauche souris aléatoirement dans la zone indiquée
    """
    random_x = min_x + random.random() * (max_x - min_x)
    random_y = min_y + random.random() * (max_y - min_y)
    # On définit la souris, on la place et on clique
    mouse = Controller()
    mouse.position = (random_x, random_y)
    time.sleep(0.05 + random.random() * 0.1)
    mouse.click(Button.left)


def ressource_click(position):
    """
    Envoi un clic aléatoirement sur la fênetre de la ressource à la position
    indiquée
    """
    min_x = 665
    max_x = 890
    min_y = 210 + position * 46
    max_y = 245 + position * 46
    random_click(min_x, max_x, min_y, max_y)


def null_click():
    """
    Envoi un clic aléatoirement sur la fenêtre hors interface de sorte à ce
    que ça n'entraine aucune action
    """
    min_x = 350
    max_x = 1180
    min_y = 30
    max_y = 95
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
    while True:
        randx = random.randint(-10, 10)
        randy = random.randint(-10, 10)
        mouse.position = (mouse.position[0] + randx, mouse.position[1] + randy)
        time.sleep(time_step)


if __name__ == "__main__":
    # random_walk(0.1)
    print(screen_infos('ressource_click_min_x'))
