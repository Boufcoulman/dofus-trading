import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from scripts.stopper import escape_on_escape
import random
from setup.setup_tools import get_mouse_pos
import mss
from PIL import Image
import numpy as np
import re

# On définit la souris
mouse = Controller()

escape_on_escape()

file = open('setup/mouse_positions.txt', 'a')
timestamp = str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
file.write('\n' + timestamp + '\n')
file.close()

time.sleep(0.5)
get_mouse_pos()

# On récupère la position actuelle
mouse.position = (600, 280)
print(mouse.position)
time.sleep(5)

screen_name = 'images/test3.png'
left = 940
top = 263
width = 80
height = 25

with mss.mss() as sct:
    # La partie de l'ecran à capturer
    monitor = {"top": top, "left": left, "width": width, "height": height}

    # Capture l'écran
    sct_img = sct.grab(monitor)

    # Sauvegarde l'image
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=screen_name)


mouse.position = (600, 280)
print(mouse.position)


time.sleep(100)

# mouse.position = (1213, 845)
# mouse.scroll(0, -1)
# screen_rectangle('images/test.png', mouse.position[0], mouse.position[1], 335, 45)
# screen_rectangle('images/test_fenetre.png', 1070, 215, 100, 25)

# On déplace la souris ((400,200) la position de la fenêtre recherche dofus sur mon grand ecran)
# mouse.position = (400, 200)

# Cliquez bandes de s****** (2 clics car on est dans dans la fenetre dofus au moment de l'exec)
# mouse.click(Button.left, 2)

# Première ressource de l'hdv
# mouse.position = (930, 230)

# Random placement
# min_x = 665
# max_x = 890
# min_y = 210
# max_y = 245
# random_x = min_x + random.random() * (max_x - min_x)
# random_y = min_y + random.random() * (max_y - min_y)
# print(random.random())
# print(random_x, random_y)
# mouse.position = (random_x, random_y)

# Faire un drag and drop

# mouse.press(Button.left)
# mouse.position=(600,550)
# time.sleep(0.1)
# mouse.release(Button.left)


# Se balader sur les ressources affichées

# mouse.position=(930,230)
# time.sleep(0.1)
# mouse.click(Button.left,1)
# insert screenshot here
# time.sleep(1)
# mouse.click(Button.left,1)
##
# mouse.scroll(0,-1)
##
# time.sleep(15)
# print(mouse.position)
