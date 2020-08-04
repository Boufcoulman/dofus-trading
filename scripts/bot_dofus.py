import time
from treatment import ressource_treatment, nbr_lots
from desktop import ressource_click, null_click, scroll_down
from screen import end_of_scroll
from stopper import escape_on_escape
from window import open_dofus, open_rune_shop, altf4


def ressource_get(position):
    """
    Réalise le traitement de la ressource à la position indiquée (0 à 13)
    /! peut ne pas être valable si l'appel est fait pour les position 11, 12
    ou 13 et que la ressource concernée n'a que 1 ou 2 lots
    """
    # On fait un random click pour s'assurer qu'on est sur la fenêtre
    null_click()

    # Si la ressource n'est pas en bas de l'écran
    if position in range(11):
        # On ouvre la fenêtre de la ressource et on récupère ses données
        ressource_click(position)
        time.sleep(0.1)
        ressource_treatment(position)

        # On ferme la fenêtre de la ressource
        ressource_click(position)
        time.sleep(0.1)

    # Si la ressource est en bas de l'ecran
    else:
        # On ouvre la fenêtre de la ressource
        ressource_click(position)
        time.sleep(0.3)

        # On scroll une fois vers le bas de sorte à afficher toutes les valeurs
        scroll_down()
        time.sleep(0.3)

        # On compte combien de ligne de lot sont visibles dans la plage
        compte_lots = nbr_lots(position - 3)

        # On applique l'algorithme de récupération des données en Fonction
        ressource_treatment(position - compte_lots)

        # On ferme la fenêtre de la ressource
        ressource_click(position - compte_lots)
        time.sleep(0.1)


def add_top_ressources(entry_number):
    """
    Ajoute les infos des ressources les plus haut dans l'hdv à la base de
    données
    """
    for i in range(entry_number):
        ressource_get(i)


def scroll_whole_selection():
    """
    Parcours toute la selection actuelle de l'hotel des vente
    A lancer quand l'hdv est ouvert sans ressource selectionnée
    """
    # Permet d'interrompre le programme avec un appui sur echap
    escape_on_escape()

    # Tant qu'on est pas en bas de l'hdv
    bottom = False
    while not bottom:
        # On capture les 3 premières ressources
        add_top_ressources(3)

        # On scroll et on vérifie si on est en bas de l'hdv
        scroll_down()
        time.sleep(0.1)
        bottom = end_of_scroll()

    # Une fois qu'on est en bas, on capture les 14 premières ressources
    # (donc toutes celles affichées à l'ecran). Cela entraine 0 1 ou 2
    # doublons d'entrées dans la base, mais ce n'est pas un problème
    add_top_ressources(14)


def rune_mining():
    """
    Lance dofus, ouvre l'hotel de vente des runes de brakmar, récupère tous
    les prix et ferme dofus
    Nécessite d'avoir déconnecté son personnage sur la carte de l'hotel des
    ventes des runes de brakmar
    """
    # Permet d'interrompre le programme avec un appui sur echap
    escape_on_escape()
    open_dofus()
    open_rune_shop()
    scroll_whole_selection()
    altf4()


if __name__ == "__main__":
    scroll_whole_selection()
