Pour faire fonctionner le bot, il est nécessaire de renseigner un fichier de configuration avec les valeurs adaptées.

Pour de vrai c'est la galère, je me surpris à redécouvrir comment fallait s'y prendre pour configurer sur un deuxième ordi et c'est trop d'ajustements imprécis et un algo trop peu robuste pour que je passe le temps de détailler en détail. Néanmoins voici quelques pistes ci-dessous si vous avez le courage :) 

Il est nécessaire de créer le fichier `config.toml` en se basant sur le squelette `config_default.toml`.

Pour récupérer les valeurs des pixels et des dimensions à renseigner dans le fichier de configuration, il est possible d'utiliser le script setup_tools.py. Il faut vérifier via des appels à screen_rectangle pour les captures.

Dans `password`, il est nécessaire de rentrer le mot de passe du compte dofus présaisi sur lequel les actions du bot seront effectuées.

Dans `db_path` il est nécessaire de rentrer le chemin et le nom du fichier où enregistrer les données.

Pour synchroniser la base récupérée via GoogleDrive il est possible d'utiliser l'utilitaire de Google pour avoir son drive synchronisé sur son poste et renseigner le chemin de la base de données directement dans le drive : https://support.google.com/drive/answer/2374987.
