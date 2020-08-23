from pynput import mouse, keyboard
from stopper import escape_on_escape
from read_config import screen_infos, tempo_infos
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


def open_ankama_launcher():
    """
    Permet d'ouvrir dofus via le launcher
    Le compte doit déjà être loggé
    Le répertoire contenant "Ankama Lancher.exe" doit être ajouté
    au PATH windows
    """
    escape_on_escape()

    # Ajout du clavier
    typing_device = keyboard.Controller()

    # Appel de windows+R
    with typing_device.pressed(keyboard.Key.cmd):
        use_key(typing_device, 'r')
    time.sleep(tempo_infos('quick_tempo'))

    # Lancement de Ankama launcher
    typing_device.type('"Ankama launcher"')
    use_key(typing_device, keyboard.Key.enter)


def full_screen():
    """
    Permet de passer en plein écran
    """
    # Ajout du clavier
    typing_device = keyboard.Controller()
    # Vérification plein écran windows+arrow up
    with typing_device.pressed(keyboard.Key.cmd):
        use_key(typing_device, keyboard.Key.up)


def instant_click(x, y):
    """
    Permet de cliquer là où on veut
    """
    # Permet d'avoir des cliques souris adéquats
    change_pixelisation()

    # Placement de la souris sur l'hôtel de vente
    mickey = mouse.Controller()
    if x.isdigit() and y.isdigit():
        click_x = x
        click_y = y
    else:
        click_x = screen_infos(x)
        click_y = screen_infos(y)
    mickey.position = (click_x, click_y)
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
    time.sleep(tempo_infos('init_tempo'))
    open_ankama_launcher()
