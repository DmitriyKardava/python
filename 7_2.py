import yaml
import os.path
with open('config.yaml') as config_file:
    config = yaml.safe_load(config_file)


def config_recursive(obj, cwd):
    if isinstance(obj, dict):
        for key, val in obj.items():
            _dir = os.path.join(cwd, key)
            if not os.path.exists(_dir):
                os.makedirs(_dir)
            config_recursive(val, _dir)
    elif isinstance(obj, list):
        for _i in obj:
            config_recursive(_i, cwd)
    else:
        if obj:
            with open(os.path.join(cwd, obj), 'w'):
                pass


config_recursive(config, "")
