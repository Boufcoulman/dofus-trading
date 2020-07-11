import time
import random
from pynput.mouse import Button, Controller


def random_click(min_x, max_x, min_y, max_y):
    """
    Réalise un clique gauche souris aléatoirement dans la zone indiquée
    """
    random_x = min_x + random.random() * (max_x - min_x)
    random_y = min_y + random.random() * (max_y - min_y)
    # On définit la souris, on la place et on clique
    mouse = Controller()
    mouse.position = (random_x, random_y)
    time.sleep(0.1 + random.random() * 0.2)
    mouse.click(Button.left)
    # Fênetre de clic ressource :
    # (667, 245), (665, 208), (892, 210), (893,245)

    # Fênetre de clic hors hdv :
    # (356, 92), (347, 29), (1183, 32), (1181, 94)²


def ressource_click(position):
    """
    Envoi un clic aléatoirement sur la fênetre de la ressource à la position
    indiquée
    """
    min_x = 665 + position * 46
    max_x = 890 + position * 46
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


# Debug zone
# random_click(665, 890, 210, 245)
null_click()