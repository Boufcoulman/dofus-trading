import toml
var_path = "config.toml"
try:
    config_vars = toml.load(var_path)
except FileNotFoundError:
    print("Le fichier {0} est manquant, veuillez le creer".format(var_path))
    raise


def password():
    """
    Retourne le mot de passe du fichier de configuration
    voir le fichier indiqué par `var_path` pour le modifier
    """
    return config_vars['login_infos']['password']


def screen_infos(dimension):
    """
    Retourne une information concernant l'écran du fichier de configuration
    voir le fichier indiqué par `var_path` pour le modifier
    """
    return config_vars['screen_infos'][dimension]


def mouse_infos(dimension):
    """
    Retourne une information concernant la souris du fichier de configuration
    voir le fichier indiqué par `var_path` pour le modifier
    """
    return config_vars['mouse_infos'][dimension]


def db_path():
    """
    Retourne le chemin de la base de données
    """
    return config_vars['db_infos']['db_path']


if __name__ == "__main__":
    print(password())
    print(screen_infos('test2'))
