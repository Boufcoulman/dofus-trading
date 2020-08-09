Pour faire fonctionner le bot, il est nécessaire de renseigner un fichier de configuration avec les valeurs adaptées.

Il est nécessaire de créer le fichier `config.toml` en se basant sur le squelette `config_default.toml`.

Pour récupérer les valeurs des pixels et des dimensions à renseigner dans le fichier de configuration, il est possible d'utiliser le script setup_tools.py.
C'est un peu trop d'efforts pour moi de détailler sous forme de doc exhaustive les mesures à prendre, go dans mes dms si besoin est.

Dans `password`, il est nécessaire de rentrer le mot de passe du compte dofus présaisi sur lequel les actions du bot seront effectuées.

Dans `db_path` il est nécessaire de rentrer le chemin et le nom du fichier où enregistrer les données.

Pour synchroniser la base récupérée via GoogleDrive il est possible d'utiliser l'utilitaire de Google pour avoir son drive synchronisé sur son poste et renseigner le chemin de la base de données directement dans le drive : https://support.google.com/drive/answer/2374987.
