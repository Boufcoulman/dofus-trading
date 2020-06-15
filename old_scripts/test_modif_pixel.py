from PIL import Image
import numpy as np
import re  # Pour faire une modification de chaine de caractère


def change_colors(path_image):
    imgpil = Image.open(path_image)
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
    path_done = re.sub(r'^(.*)([a-zA-Z_]*).png', r'\1\2_done.png', path_image)
    imgdone.save(path_done)


# Debug zone

change_colors('images/test_full.png')
