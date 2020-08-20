import mss
from PIL import Image
import numpy as np
import re
from read_config import screen_infos
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


def end_of_scroll():
    """
    Détecte si on atteind le bas de l'hdv
    """
    image_name = 'images/check_if_bottom.png'
    # Capture du pixel
    x_pixel = screen_infos('x_pixel')
    y_pixel = screen_infos('y_pixel')
    screen_rectangle(image_name, x_pixel, y_pixel, 1, 1)

    # Vérification de la teinte du pixel
    img_scroll = Image.open(image_name)
    pix_scroll = list(img_scroll.getdata())
    r = pix_scroll[0][0]
    is_bottom = r > 50

    return is_bottom


def is_ok_color(value, goal, tolerance):
    return value >= goal - tolerance and value <= goal + tolerance


def is_ok_pixel(x, y, r=50, g=50, b=50, tr=5, tg=5, tb=5):
    """
    Indique si un pixel est dans la bonne plage de couleur
    """
    image_name = 'images/check_pixel.png'
    # Capture du pixel
    screen_rectangle(image_name, x, y, 1, 1)

    # Véification de la teinte du pixel
    img_pixel = Image.open(image_name)
    pixel = list(img_pixel.getdata())
    mr, mg, mb = pixel[0]
    print(mr, mg, mb)
    is_ok_red = is_ok_color(mr, r, tr)
    is_ok_blue = is_ok_color(mb, b, tb)
    is_ok_green = is_ok_color(mg, g, tg)
    print(is_ok_red, is_ok_green, is_ok_blue)


def test():
    image_name = 'images/ressource_name.png'
    img_pixel = Image.open(image_name)
    pixel = list(img_pixel.getdata())
    print(pixel)


if __name__ == "__main__":
    # print(end_of_scroll())
    # test()
    # time.sleep(5)
    change_colors('images/ressource_name.png')
    # screen_rectangle('images/test3.png', 10, 42, 100, 32)
    # change_colors('images/test3.png')
    # is_ok_pixel(71, 59)
