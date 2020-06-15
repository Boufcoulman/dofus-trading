import mss
from PIL import Image
import numpy as np
import re
import pytesseract


def screen_rectangle(screen_name, top, left, width, height):
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
            if r > 90:
                r = 0
                v = 0
                b = 0
            else:
                r = 255
                v = 255
                b = 255
            img[i, j] = (r, v, b)

    imgdone = Image.fromarray(img)
    path_done = re.sub(r'^(.*)([a-zA-Z_]*).png', r'\1\2_done.png', path_image)
    imgdone.save(path_done)


def text_extract(filepath):
    """
    Fonction de récupération de texte d'une image en utilisant pytesseract
    """
    text = pytesseract.image_to_string(Image.open(filepath))
    return text

# Debug zone


print(text_extract('images/test_prix_done.png'))
change_colors('images/test_full.png')
# screen_rectangle('images/test.png', 160, 160, 160, 135)
