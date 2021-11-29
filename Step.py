class Step:
    def __init__(self, step_data):
        self.description = step_data["description"]
        self.directions = step_data["directions"]
        self.loot = step_data["loot"]
        self.enemy = step_data["enemy"]

    def describe(self):
        print(self.description)

    def tell_directions(self):
        print("where to next?")
        for index, direction in enumerate(self.directions):
            print(index, direction)

    def tell_loot(self):
        print(self.loot)

    def tell_enenmy(self):
        print(self.enemy)

    def __str__(self) -> str:
        s = f"""
        Description:{self.describe()}
        Directions: {self.tell_directions()}
        loot: {self.tell_loot()}
        """
        return s
