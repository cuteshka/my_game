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
            print(self.game.index_level, "saved")
            with open("last_level", "w") as scores:
                json.dump(data, scores, ensure_ascii=False, indent=4)
