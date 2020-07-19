# WIP:dofus-trading
Scripts python personnalisés permettant de récupérer des prix de l'hôtel de vente dofus de manière automatisée
La vocation secondaire de ce projet est éducative pour moi. N'hesitez pas à faire des retours concernant des pistes d'améliorations, sur le fonctionnement, le nommage des fichiers, des fonctions, l'utilisation de git, les dépendances, etc...

## Description des fichiers

**scripts/db_functions.py** contient les fonctions utiles à la manipulation de la base de données.<br>
**scripts/desktop_functions.py** contient les fonctions liées à la simulation de geste humain (souris, clavier, ...).<br>
**scripts/image_functions.py** contient les fonctions liées à la manipulation d'image.<br>
**scripts/parsing_functions.py** contient les fonctions liées à la détection de texte.<br>
**scripts/hdv_treatment_functions.py** contient la fonction à utiliser quand une ressource est cliquée. Gère la récupération des informations de la ressource et l'ajout dans la base de données.<br>
**scripts/stopper.py** contient les fonctions permettant de gérer les interruptions de script
**scripts/dofus_window.py** contient les scripts d'ouverture/fermeture de dofus
**scripts/bot_functions.py** contient les scripts à ordonnancer/ exécuter pour récupérer alimenter la base de données en mâsse.

## Projets de scripts à faire tourner régulièrement :
* Récupération du prix de toutes les runes de forgemagie classiques
* Récupération du prix de ressources précises présélectionnées
* Récupération de l'ensemble des prix d'un hdv ressource/rune/consommable (en dernier ça)


## Setup pour Windows en vrac
- Avoir python à jour (pour éviter des problèmes, de préférences l'installer via [l'installer windows](https://www.python.org/ftp/python/3.8.4/python-3.8.4-amd64.exe) et sélectionner les options : pour l'utilisateur courant, ajouter le répertoire python au PATH et autoriser les noms trop longs)
- Récupérer le projet git
- Installer pipenv, dans le shell windows : `pip install pipenv`
- Lancer pipenv dans le dossier du projet en local, toujours dans le shell windows : `pipenv shell`
- Installer les dépendances : `pipenv install`
- Changer les valeurs en dur de sorte à faire correspondre les fenêtres de capture et de clic à son écran. (procédé à détailler)
- Ajouter le répertoire d'installation de dofus à la variable d'environnement windows, PATH :
`C:\Users\<votre_session_utilisateur>\AppData\Local\Ankama\zaap\dofus` par défaut
- Mettre son jeu à jour via le launcher
- Changer les paramètres de connexion dans la fenêtre de jeu de sorte à avoir une connexion directe vers le jeu et non au choix des serveurs ou des personnages

## Setup pour la récupération des prix des runes
- Se connecter à son personnage et l'emmener sur la carte d'hotel de vente des runes (de Brakmar, potentiellement fonctionnel à Bonta et à Brakmar)
