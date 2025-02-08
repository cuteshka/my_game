import json


class LastLevel:
    def __init__(self, game):
        self.game = game

    def load(self):
        try:
            with open("last_level", "r") as data:
                scores = json.load(data)
                self.game.index_level = scores["level"]
            self.game.load_level()
            self.game.start()
        except FileNotFoundError:
            print("No saved data")

    def save(self):
        data = {
            "level": self.game.index_level
        }
        with open("last_level", "w") as scores:
            json.dump(data, scores, ensure_ascii=False, indent=4)

    def get_curr_level_number(self):
        try:
            with open("last_level", "r") as data:
                scores = json.load(data)
                return scores["level"]
        except FileNotFoundError:
            return 1
