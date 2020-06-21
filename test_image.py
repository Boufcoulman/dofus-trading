try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from scripts.parsing_functions import text_extract
from scripts.image_functions import change_colors, screen_rectangle


screen_rectangle('images/test_fenetre.png', 940, 353, 80, 25)
change_colors('images/test_fenetre.png')
print(text_extract('images/test_fenetre_done.png'))

# def ocr_core(filename):
#     """
#     This function will handle the core OCR processing of images.
#     """
#     text = pytesseract.image_to_string(Image.open(filename))
#     # We'll use Pillow's Image class to open the image and pytesseract to detec
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
