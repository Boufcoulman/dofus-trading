from pynput import mouse, keyboard
from scripts.stopper import escape_on_escape
from scripts.window import use_key
import time

escape_on_escape()

# Ajout du clavier
typing_device = keyboard.Controller()

time.sleep(0.8)

# Appel de windows+R
with typing_device.pressed(keyboard.Key.cmd):
    use_key(typing_device, 'r')
