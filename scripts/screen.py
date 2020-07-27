import mss
from PIL import Image
import numpy as np
import re
from read_config import screen_infos


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


def change_colors(path_image):
    """
    Fonction de changement de couleurs des pixels pour convertir
    en images avec polices noir sur blanc
    """
    imgpil = Image.open(path_image)
    # anciennement np.asarray
    img = np.array(imgpil)  # Transformation de l'image en tableau numpy

    img = img[:, :, :3].copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r, v, b = img[i, j]
            if r > 100:
                r = 0
                v = 0
                b = 0
            else:
                r = 255
                v = 255
                b = 255
            img[i, j] = (r, v, b)

    imgdone = Image.fromarray(img)
    path_done = re.sub(r'^(.*)([a-zA-Z_]*).png', r'\1\2_bw.png', path_image)
    imgdone.save(path_done)

    return path_done


def end_of_scroll():
    """
    Détecte si on atteind le bas de l'hdv
    """
    temp_img_name = 'images/check_if_bottom.png'
    # Capture du pixel
    x_pixel = screen_infos('x_pixel')
    y_pixel = screen_infos('y_pixel')
    screen_rectangle(temp_img_name, x_pixel, y_pixel, 1, 1)

    # Vérification de la teinte du pixel
    img_scroll = Image.open(temp_img_name)
    pix_scroll = list(img_scroll.getdata())
    r = pix_scroll[0][0]
    is_bottom = r > 50

    return is_bottom


if __name__ == "__main__":
    print(end_of_scroll())
    # change_colors('images/test_full.png')
    # screen_rectangle('images/test.png', 160, 160, 160, 135)
    # screen_rectangle('images/test_fenetre.png', 810, 261, 90, 25)
    # change_colors('images/test_fenetre.png')
