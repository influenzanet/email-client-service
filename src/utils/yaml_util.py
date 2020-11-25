import yaml
from constants.constants import REQUIRED_YAML_KEYS, KEY_SEPARATOR, REQUIRED_SERVER_KEYS


def load_yaml(path: str):
    with open(path) as f:
        data = yaml.load(f, yaml.SafeLoader)
    return validate_yaml(data, path)


def validate_yaml(data, path):
    if data is None:
        raise Exception("Empty configuration in file : " + path)

    # Check if Yaml contains required keys (defined in constants)
    required_keys = [key.strip()
                     for key in REQUIRED_YAML_KEYS.split(KEY_SEPARATOR)]
    if not set(required_keys) <= data.keys():
        raise Exception("YAML configuration needs keys ["
                        + REQUIRED_YAML_KEYS
                        + "] in file : " + path)

    # Check that required keys are not None or Empty
    for key in required_keys:
        if is_empty(key, data):
            raise_key_empty_error(key, path)

    # Check for host, port, connections and auth for each server
    for server in data['servers']:
        validate_server(server, path)

    return data


def is_empty(key, data):
    return data[key] is None or not len(data[key]) > 0


def raise_key_empty_error(key, path):
    raise Exception(key + " key is empty in : " + path)


def validate_server(server, path):
    """ Method to Check for presence of required keys within the server section 
    of the YAML files
    Inputs:
    server - dict representing each server defined in the config yaml
    path - path of the yaml being validated  """
    required_server_keys = [key.strip()
                            for key in REQUIRED_SERVER_KEYS.split(KEY_SEPARATOR)]
    if server is None or not set(required_server_keys) <= server.keys():
        raise Exception("Server configuration needs keys ["
                        + REQUIRED_SERVER_KEYS
                        + "] in file : " + path)

    # Check that auth contains user and password keys
    if 'password' not in server['auth'] or 'user' not in server['auth']:
        raise Exception('Auth configuration needs keys ["password", "user"] in file : '
                        + path)
