import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from trading_functions import get_screen

# ATTENTION ça marche que sur un hdv sur le bon ecran, ça ne parcours pas
# partout, il faut paufiner le bousin et savoir à quoi ça sert. gl hf.

# On définit la souris
mouse = Controller()

# Placement préalable dans la fenêtre dofus
mouse.position = (930, 230)
mouse.click(Button.left, 1)
time.sleep(1)

# Fonction pour clic screen

# On créé un thread pour éxécuter en boucle la commande


class ScrollHdv(threading.Thread):
    def __init__(self):
        super(ScrollHdv, self).__init__()
        self.running = False
        self.program_running = True

    def start_doing_your_stuff(self):
        self.running = True

    def stop_doing_your_stuff(self):
        self.running = False

    def exit(self):
        self.stop_doing_your_stuff()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                # On clique la première ressource
                mouse.position = (930, 230)
                mouse.click(Button.left)
                time.sleep(0.1)

                # On screen
                # insert screen instruction here

                # On scroll

                time.sleep(0.8)
            time.sleep(0.1)
