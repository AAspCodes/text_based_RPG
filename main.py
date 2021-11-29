import yaml
from Step import Step


def read_from_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def read_enemies():
    return read_from_yaml("enemies.yaml")


def read_steps():
    return read_from_yaml("steps.yaml")

    pass
def game_loop():
    enemies = read_enemies()
    steps = read_steps()
    step_pos = 0

    while True:
        step = Step(steps[step_pos])
        step.describe()
        step.tell_directions()
        choice = input()

if __name__ == "__main__":
    game_loop()
