from pynput import mouse, keyboard
from stopper import escape_on_escape
import env_var
import time


def use_key(typing_device, keyboard_key):
    """
    Simule un appui bref sur une touche
    Pour une obscure raison, la fonction keyboard.Controller.tap n'est pas
    présente dans le paquet pynput de ma machine, autrement
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

    time.sleep(0.8)

    # Appel de windows+R
    with typing_device.pressed(keyboard.Key.cmd):
        use_key(typing_device, 'r')

    time.sleep(0.2)

    # Lancement de dofus
    typing_device.type('dofus')
    use_key(typing_device, keyboard.Key.enter)

    time.sleep(10)
    # Passage de la popup "lancement sans launcher"
    use_key(typing_device, keyboard.Key.enter)

    time.sleep(0.2)
    # Saisie du mot de passe
    typing_device.type(PASSWORD)


if __name__ == "__main__":
    open_dofus()
