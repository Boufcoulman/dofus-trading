import time
from pynput.mouse import Button, Controller
import random
import mss

# On définit la souris
mouse = Controller()


# Fait un click, prend un screen, refait un click
def get_screen(x, y, item):
    mouse.position = (x, y)
    mouse.click(Button.left)
    time.sleep(0.2 + random.random()/5)
    # prend un screenshot avec le bon nom
    mouse.position = (x, y)
    mouse.click(Button.left)
    time.sleep(0.5)


def capture_reduced_window(ressource):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
        output = "{}.png".format(ressource)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
