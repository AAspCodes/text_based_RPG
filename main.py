import yaml


def read_from_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def readEnemies():
    return read_from_yaml("enemies.yaml")


def readSteps():
    return read_from_yaml("steps.yaml")


if __name__ == "__main__":
    pass
