import time
from pynput.mouse import Controller
from pynput import keyboard
import os

"""
L'appel du fichier permet de relever la position du curseur pendant un temps
avec des appuis sur shiftl
Termine sur un appui sur escape
"""

# On définit la souris
mouse = Controller()


def on_release(key):
    if key == keyboard.Key.shift:
        file = open('setup/mouse_positions.txt', 'a')
        # Affiche la position de la souris
        pos = mouse.position
        print(str(pos))
        file.write(str(pos) + '\n')

    if key == keyboard.Key.esc:
        # Arrêt du programme
        os._exit(1)


def get_mouse_pos():
    listener = keyboard.Listener(
        on_release=on_release)
    listener.start()


if __name__ == "__main__":
    file = open('setup/mouse_positions.txt', 'a')
    timestamp = str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
    file.write('\n' + timestamp + '\n')
    file.close()

    time.sleep(0.5)
    get_mouse_pos()
    time.sleep(1000)
