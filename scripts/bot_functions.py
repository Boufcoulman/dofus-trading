from hdv_treatment_functions import ressource_treatment
from desktop_functions import ressource_click, null_click
import time


def ressource_get(position):
    """
    Réalise le traitement de la ressource à la position indiquée (0 à 13)
    """
    # On fait un random click pour s'assurer qu'on est sur la fenêtre
    null_click()

    # On ouvre la fenêtre de la ressource et on récupère ses données
    ressource_click(position)
    time.sleep(0.1)
    ressource_treatment(position)

    # On ferme la fenêtre de la ressource
    ressource_click(position)


def add_top_ressources(entry_number):
    """
    Ajoute les infos des 3 ressources les plus haut dans l'hdv à la base de
    données
    """
    for i in range(entry_number):
        ressource_get(i)


# Debug zone
# add_top_ressources(4)
ressource_get(1)
