import mss
from PIL import Image
import numpy as np
import re
import time


def screen_rectangle(screen_name, left, top, width, height):
    """
    Fonction de capture d'un rectangle voulu
    avec nom du screen et zone à capturer en input
    """
    with mss.mss() as sct:
        # La partie de l'ecran à capturer
        monitor = {"top": top, "left": left, "width": width, "height": height}

        # Capture l'écran
        sct_img = sct.grab(monitor)

        # Sauvegarde l'image
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=screen_name)


def treshold_red(r, g, b, treshold=100):
    return r > treshold


def treshold_all(r, g, b, treshold=100):
    return r > treshold and g > treshold and b > treshold


def treshold_black(r, g, b, treshold=210):
    return r < treshold and g < treshold and b < treshold


def change_colors(path_image, test=treshold_red, treshold=100):
    """
    Fonction de changement de couleurs des pixels pour convertir
    en images avec polices noir sur blanc
    """
    imgpil = Image.open(path_image)
    # Transformation de l'image en tableau numpys
    img = np.array(imgpil)

    img = img[:, :, :3].copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r, g, b = img[i, j]
            if test(r, g, b, treshold):
                r = 0
                g = 0
                b = 0
            else:
                r = 255
                g = 255
                b = 255
            img[i, j] = (r, g, b)

    imgdone = Image.fromarray(img)
    path_done = re.sub(r'^(.*)([a-zA-Z_]*).png', r'\1\2_bw.png', path_image)
    imgdone.save(path_done)

    return path_done


if __name__ == "__main__":
    # print(end_of_scroll())
    time.sleep(5)
    screen_rectangle('images/test3.png', 1090, 261, 65, 25)
    # change_colors('images/test3.png')
    # is_ok_pixel(71, 59)
