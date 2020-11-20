import yaml


def load_yaml(path: str):
    with open(path) as f:
        data = yaml.load(f)
    return validate_yaml(data)

# TODO VALIDATION
def validate_yaml(data):
    return data
