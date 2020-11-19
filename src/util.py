import yaml

def loadYaml(path: str):
    with open(path) as f:
        data = yaml.load(f)
    return validateYaml(data)

#TODO VALIDATION
def validateYaml(data):
    return data