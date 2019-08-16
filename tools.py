import yaml


def load_config(config_file):
    with open(config_file, 'r') as f:
        cfg_dict = yaml.load(f, yaml.FullLoader)
    return cfg_dict
