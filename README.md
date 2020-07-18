# WIP:dofus-trading
Scripts python personnalisés permettant de récupérer des prix de l'hôtel de vente dofus de manière automatisée
La vocation secondaire de ce projet est éducative pour moi. N'hesitez pas à faire des retours concernant des pistes d'améliorations, sur le fonctionnement, le nommage des fichiers, des fonctions, l'utilisation de git, les dépendances, etc...

## Description des fichiers

**scripts/db_functions.py** contient les fonctions utiles à la manipulation de la base de données.<br>
**scripts/desktop_functions.py** contient les fonctions liées à la simulation de geste humain (souris, clavier, ...).<br>
**scripts/image_functions.py** contient les fonctions liées à la manipulation d'image.<br>
**scripts/parsing_functions.py** contient les fonctions liées à la détection de texte.<br>
**scripts/hdv_treatment_functions.py** contient la fonction à utiliser quand une ressource est cliquée. Gère la récupération des informations de la ressource et l'ajout dans la base de données.<br>
**scripts/bot_functions.py** contient les scripts à ordonnancer/ exécuter pour récupérer alimenter la base de données en mâsse.

## Projets de scripts à faire tourner régulièrement :
* Récupération du prix de toutes les runes de forgemagie classiques
* Récupération du prix de ressources précises présélectionnées
* Récupération de l'ensemble des prix d'un hdv ressource/rune/consommable (en dernier ça)


## Setup pour Windows en vrac
upgrade pip : python -m pip install --upgrade pip
Récupérer le projet git
Installer pipenv, dans le shell windows : pip install pipenv
Lancer pipenv dans le dossier du projet en local, toujours dans le shell windows : pipenv shell
Installer les dépendances : pipenv install
