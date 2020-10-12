# WIP:dofus-trading
Scripts python personnalisés permettant de récupérer des prix de l'hôtel de vente dofus de manière automatisée. Initialement compatible avec la version 2.55 de dofus.
La vocation secondaire de ce projet est éducative pour ses concepteurs. N'hesitez pas à faire des retours concernant des pistes d'améliorations, sur le fonctionnement, le nommage des fichiers, des fonctions, l'utilisation de git, les dépendances, etc...

## Description des fichiers

`scripts/database.py` contient les fonctions utiles à la manipulation de la base de données.<br>
`scripts/desktop.py` contient les fonctions liées à la simulation de geste humain (souris, clavier, ...).<br>
`scripts/screen.py` contient les fonctions liées à la manipulation d'image.<br>
`scripts/parsing.py` contient les fonctions liées à la détection de texte.<br>
`scripts/treatment.py` contient la fonction à utiliser quand une ressource est cliquée. Gère la récupération des informations de la ressource et l'ajout dans la base de données.<br>
`scripts/stopper.py` contient les fonctions permettant de gérer les interruptions de script.<br>
`scripts/window.py` contient les scripts d'ouverture/fermeture de dofus.<br>
`scripts/bot_dofus.py` contient les scripts à ordonnancer/ exécuter pour récupérer alimenter la base de données en mâsse.

## Projets de scripts à faire tourner régulièrement :
* Récupération du prix de toutes les runes de forgemagie classiques
* Récupération du prix de ressources précises présélectionnées
* Récupération de l'ensemble des prix d'un hdv ressource/rune/consommable (en dernier ça)


## Setup pour Windows en vrac
- Avoir python à jour (pour éviter des problèmes, de préférences l'installer via [l'installer windows](https://www.python.org/ftp/python/3.8.4/python-3.8.4-amd64.exe) et sélectionner les options : pour l'utilisateur courant, ajouter le répertoire python au PATH et autoriser les noms trop longs)
- Récupérer le projet git
- Installer tesseract OCR : [pour windows x64](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe) ; sources : [pytesseract](https://pypi.org/project/pytesseract/) wrapper pour python ; page git avec toutes les infos sur le projet [tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Installer pipenv, dans le shell windows : `pip install pipenv`
- Lancer pipenv dans le dossier du projet en local, toujours dans le shell windows : `pipenv shell`
- Installer les dépendances : `pipenv install`
- Ajouter le répertoire d'installation de dofus dans lequel se trouve l'executable Ankama Launcher à la variable d'environnement windows, PATH :
`C:\Users\<votre_session_utilisateur>\AppData\Local\Ankama\zaap\` par défaut
- Mettre son jeu à jour via le launcher
- Changer les paramètres de connexion dans le launcher ankama de sorte à avoir une connexion directe vers le jeu


## Setup la configuration pour qu'elle soit adaptée à son écran
Le programme a été développé en prenant en dur les valeurs de pixels adaptées à l'ordinateur de développement.

Pour rendre le bot adapté à sa machine, il faut créer un fichier `config.toml`, en suivant la documentation du répertoire `setup`.
Les valeurs des temporisations sont arbitraires, certaines sont là pour parer d'éventuels légers lag réseau, d'autres dépendent des performances du la machine qui fait tourner le bot.

## Setup pour la récupération des prix des runes
- Se connecter à son personnage et l'emmener sur la carte d'hôtel de vente des runes de Brakmar puis fermer le jeu.
- Ordonnancer la fonction rune_mining() de scripts/bot_dofus.py : sous windows, utiliser le planificateur de tâches et lancer bot_to_schedule.bat dans le dossier du script.

## Misc
- Initialement, les données étaient sauvegardées dans une base sqlite, mais dans notre cas d'utilisation pour la visualisation post récupération un fichier texte convient parfaitement. Le module sqlite est toujours présent et est en principe parfaitement fonctionnel.
