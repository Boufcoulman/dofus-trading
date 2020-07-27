try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from scripts.parsing_functions import data_extract, lot_parsing, price_parsing
from scripts.image_functions import change_colors, screen_rectangle
import numpy as np
import mss
import time


with mss.mss() as sct:
    # La partie de l'ecran à capturer
    monitor = {"top": 400, "left": 400, "width": 200, "height": 200}
    print(time.time())
    # Capture l'écran
    sct_img = sct.grab(monitor)
    print(time.time())
    # Sauvegarde l'image
    mss.tools.to_png(sct_img.rgb, sct_img.size, output='images/test.png')
    print(time.time())

    time.sleep(1)
    print(time.time())
# screen_rectangle('images/test_almost_bottom_scroll.png', 1210, 845, 1, 1)

# Fênetre de clic ressource :
# (667, 245), (665, 208), (892, 210), (893,245)

# Fênetre de clic hors hdv :
# (356, 92), (347, 29), (1183, 32), (1181, 94)

# im = Image.open('images/test_almost_bottom_scroll.png')
# pix_val = list(im.getdata())
# print(pix_val)

# screen_rectangle('images/test_fenetre.png', 830, 491, 70, 25)
# change_colors('images/test_fenetre.png')
# print(data_extract('images/test_fenetre_bw.png'))
# print(lot_parsing(data_extract('images/test_fenetre_bw.png')))
#
# screen_rectangle('images/test_fenetre.png', 940, 491, 80, 25)
# change_colors('images/test_fenetre.png')
# print(data_extract('images/test_fenetre_bw.png'))
# print(price_parsing(data_extract('images/test_fenetre_bw.png')))
# print(lot_parsing(data_extract('images/test_fenetre_bw.png')))

# def ocr_core(filename):
#     """
#     This function will handle the core OCR processing of images.
#     """
#     text = pytesseract.image_to_string(Image.open(filename))
#     # We'll use Pillow's Image class to open the image and pytesseract to dete
#     # the string in the image
#     return text

# im_sharp = im.filter(ImageFilter.SHARPEN)
# # Saving the filtered image to a new file
# im_sharp.save('image_sharpened.jpg')
#
# # Splitting the image into its respective bands, i.e. Red, Green,
# # and Blue for RGB
# r, g, b = im_sharp.split()
#
# # Viewing EXIF data embedded in image
# exif_data = im._getexif()
# exif_data
# changer_couleurs('images/test_prix_colorized.png')


# Debug zone


# # Parcours des images du dossier
# for filename in os.listdir('images'):
#     print(filename)
#     print(ocr_core('images/'+filename))
# print(ocr_core('images/test_full_done.png'))


# def changer_couleurs(filename):
#     # Lecture de l'image
#     im = Image.open(filename)
#
#     pix_val = list(im.getdata())
#
#     nred = 0
#     ngreen = 0
#     nblue = 0
#
#     for red, green, blue in pix_val:
#         print(red, green, blue)
#         if red > 90:
#             nred = 0
#             ngreen = 0
#             nblue = 0
#         else:
#             nred = 255
#             ngreen = 255
#             nblue = 255
