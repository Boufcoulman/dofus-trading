import toml
var_path = "config_vars.toml"


def password():
    """
    Retourne le mot de passe du fichier de configuration
    voir le fichier indiqué par `var_path` pour le modifier
    """
    config_vars = toml.load(var_path)
    return config_vars['login_infos']['password']


def screen_infos(dimension):
    """
    Retourne une information concernant l'écran du fichier de configuration
    voir le fichier indiqué par `var_path` pour le modifier
    """
    config_vars = toml.load(var_path)
    return config_vars['screen_infos'][dimension]


if __name__ == "__main__":
    print(password())
    print(screen_infos('test2'))
