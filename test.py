import os
from trading_functions import get_screen
import random
import mss
import mss.tools
from pynput.mouse import Button, Controller
import time
import re

mouse = Controller()
print(mouse.position)

cwd = os.getcwd()
print(cwd)

ts = time.localtime()
print(ts)

print(time.strftime("%Y%m%d_%H%M%S", ts))

for filename in os.listdir('images'):
    print(filename)

txt = "images/truc/mon_image.png"
x = re.sub(r'^(.*)([a-zA-Z_]*).png', r'\1\2_done.png', txt)
print(x)

test_dictionnaire = {1: (120, 110, 27), 2: (121, 112, 28)}
print(test_dictionnaire[1][2])
# get_screen(930, 230, 'test')

# for x in range(10):
#     print(random.random())

# with mss.mss() as sct:
#     # The screen part to capture
#     monitor = {"top": 200, "left": 615, "width": 600, "height": 190}
#     output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
#
#     # Grab the data
#     sct_img = sct.grab(monitor)
#
#     # Save to the picture file
#     mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#     print(output)


# 618 206
# 1213 206


# 619 387
# 1208 386
