import toml
var_path = "config_vars.toml"


def password():
    config_vars = toml.load(var_path)
    print(config_vars['screen_infos']['test'])


if __name__ == "__main__":
    password()
