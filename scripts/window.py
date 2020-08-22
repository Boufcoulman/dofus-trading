from pynput import mouse, keyboard
from stopper import escape_on_escape
from read_config import password, screen_infos, tempo_infos
import time
from pixelisation import change_pixelisation


def use_key(typing_device, keyboard_key):
    """
    Simule un appui bref sur une touche
    Pour une obscure raison, la fonction pynput.keyboard.Controller.tap n'est
    pas présente dans le paquet pynput de ma machine, autrement
    il ferait très bien le travail
    """
    typing_device.press(keyboard_key)
    typing_device.release(keyboard_key)


def open_dofus():
    """
    Permet d'ouvrir dofus et de se connecter
    Les identifiants doivent être stockés là :
    Sous ce format :
    Le répertoire contenant dofus.exe doit être ajouté au PATH windows
    """
    escape_on_escape()

    # Ajout du clavier
    typing_device = keyboard.Controller()

    time.sleep(tempo_infos('init_tempo'))

    # Appel de windows+R
    with typing_device.pressed(keyboard.Key.cmd):
        use_key(typing_device, 'r')

    time.sleep(tempo_infos('quick_tempo'))

    # Lancement de dofus
    typing_device.type('dofus')
    use_key(typing_device, keyboard.Key.enter)

    time.sleep(tempo_infos('launch_tempo'))
    # Vérification plein écran windows+arrow up
    with typing_device.pressed(keyboard.Key.cmd):
        use_key(typing_device, keyboard.Key.up)

    # Passage de la popup "lancement sans launcher"
    use_key(typing_device, keyboard.Key.enter)

    time.sleep(tempo_infos('quick_tempo'))
    # Saisie du mot de passe
    typing_device.type(password())
    # Connexion
    use_key(typing_device, keyboard.Key.enter)
    # time.sleep(tempo_infos('char_tempo'))
    # # Validation personnage (si nécessaire)
    # use_key(typing_device, keyboard.Key.enter)
    # time.sleep(tempo_infos('log_tempo'))


def open_rune_shop():
    """
    Permet d'ouvrir l'hôtel de vente des runes de brakmar
    """
    # Permet d'avoir des cliques souris adéquats
    change_pixelisation()

    # Placement de la souris sur l'hôtel de vente
    mickey = mouse.Controller()
    brak_rune_x = screen_infos('brak_rune_x')
    brak_rune_y = screen_infos('brak_rune_y')
    mickey.position = (brak_rune_x, brak_rune_y)
    # Clique
    mickey.click(mouse.Button.left)


def check_rune_box():
    """
    Permet de cocher la box affichant les runes dans l'hotel de ventes
    des runes de Brakmar
    """
    # Permet d'avoir des cliques souris adéquats
    change_pixelisation()

    # Placement de la souris sur la tickbox pour l'affichage des runes
    mickey = mouse.Controller()
    rune_box_x = screen_infos('rune_box_x')
    rune_box_y = screen_infos('rune_box_y')
    mickey.position = (rune_box_x, rune_box_y)
    # Clique
    mickey.click(mouse.Button.left)


def altf4():
    """
    Réalise un appui d'alt_l + f4 dans le but de
    fermer la fenêtre windows active
    """
    # Ajout du clavier
    typing_device = keyboard.Controller()
    # Appui alt+f4
    with typing_device.pressed(keyboard.Key.alt_l):
        use_key(typing_device, keyboard.Key.f4)


if __name__ == "__main__":
    open_dofus()
    open_rune_shop()
