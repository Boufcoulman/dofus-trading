from PIL import Image
import numpy as np


def change_colors(image):
    imgpil = Image.open(image)
    # anciennement np.asarray
    img = np.array(imgpil)  # Transformation de l'image en tableau numpy

    print(img.shape)

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
    imgdone.save("images/test_nom_objet_done.png")
