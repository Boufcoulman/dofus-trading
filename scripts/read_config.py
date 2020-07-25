import toml
var_path = "config_vars.toml"


def password():
    """
    Retourne le mot de passe du fichier de configuration
    """
    config_vars = toml.load(var_path)
    return config_vars['login_infos']['password']


def screen_infos():
    """
    Retourne les informations concernant l'écran du fichier de configuration
    """
    config_vars = toml.load(var_path)
    return config_vars['screen_infos']


if __name__ == "__main__":
    password()
