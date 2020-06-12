import time
from pynput.mouse import Button, Controller

# On définit la souris
mouse = Controller()

# On récupère la position actuelle
print(mouse.position)

# On déplace la souris ((400,200) la position de la fenêtre recherche dofus sur mon grand ecran)
mouse.position = (400, 200)

# Cliquez bandes de s****** (2 clics car on est dans dans la fenetre dofus au moment de l'exec)
mouse.click(Button.left, 2)

# Première ressource de l'hdv
mouse.position = (930, 230)


# Faire un drag and drop

# mouse.press(Button.left)
# mouse.position=(600,550)
# time.sleep(0.1)
# mouse.release(Button.left)


# Se balader sur les ressources affichées

# mouse.position=(930,230)
# time.sleep(0.1)
# mouse.click(Button.left,1)
# insert screenshot here
# time.sleep(1)
# mouse.click(Button.left,1)
##
# mouse.scroll(0,-1)
##
# time.sleep(15)
# print(mouse.position)
