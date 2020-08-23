import time
from treatment import ressource_treatment, nbr_lots
from desktop import ressource_click, null_click, scroll_down
from tester import end_of_scroll, in_brakmar, in_rune_shop
from tester import is_clicked, launcher_launched, wait_test
from tester import runes_showed, ready_to_launch
from stopper import escape_on_escape
from window import open_ankama_launcher, instant_click, altf4
from window import full_screen
from read_config import tempo_infos


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
        # On attend que la ressource soit bien cliquée
        while not is_clicked(position):
            time.sleep(tempo_infos('test_tempo'))
        ressource_treatment(position)

        # On ferme la fenêtre de la ressource
        ressource_click(position)
        # On attend que la ressource soit bien décliquée
        while is_clicked(position):
            time.sleep(tempo_infos('test_tempo'))

    # Si la ressource est en bas de l'ecran il est nécessaire de scroll
    else:
        # On ouvre la fenêtre de la ressource
        ressource_click(position)
        # Dans le cas de la derniere ressource on ne peut avoir l'info du click
        if position != 13:
            # On attend que la ressource soit bien cliquée
            while not is_clicked(position):
                time.sleep(tempo_infos('test_tempo'))
        else:
            # On prie
            time.sleep(tempo_infos('lag_tempo'))

        # On scroll une fois vers le bas de sorte à afficher tous les prix lot
        scroll_down()

        # On compte combien de ligne de lot sont visibles dans la plage
        compte_lots = nbr_lots(position - 3)

        # On applique l'algorithme de récupération des données en Fonction
        ressource_treatment(position - compte_lots)

        # On ferme la fenêtre de la ressource
        ressource_click(position - compte_lots)
        while is_clicked(position):
            time.sleep(tempo_infos('test_tempo'))


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
    time.sleep(tempo_infos('init_tempo'))
    # Lancement d'Ankama Launcher
    open_ankama_launcher()
    time.sleep(tempo_infos('launch_tempo'))
    full_screen()
    wait_test(ready_to_launch)
    # Lancement de dofus
    instant_click('start_button_x', 'start_button_y')
    time.sleep(tempo_infos('launch_tempo'))
    full_screen()
    wait_test(in_brakmar)
    # Ouverture de l'hôtel de vente des runes
    instant_click('brak_rune_x', 'brak_rune_y')
    wait_test(in_rune_shop)
    instant_click('rune_box_x', 'rune_box_y')
    wait_test(runes_showed)
    # Extraction du prix des runes
    scroll_whole_selection()
    altf4()
    if launcher_launched():
        altf4()


if __name__ == "__main__":
    time.sleep(3)
    position = 0
    ressource_click(position)
    # On attend que la ressource soit bien cliquée
    while not is_clicked(position):
        time.sleep(tempo_infos('test_tempo'))
    ressource_treatment(position)
