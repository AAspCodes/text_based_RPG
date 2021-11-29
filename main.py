import yaml


def read_from_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def read_enemies():
    return read_from_yaml("enemies.yaml")


def read_steps():
    return read_from_yaml("steps.yaml")

def game_loop():
    enemies = readEnemies()
    steps = readSteps()
    step_pos = 0

    while True:
        step = steps[step_pos]
        print(step["description"])
        print("choose your next step")
        for index, direction in enumerate(step["paths"]):
            print(f"{index}  {direction}")
        choice = input()

if __name__ == "__main__":
    game_loop()
