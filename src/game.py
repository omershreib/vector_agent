from level import LevelManager

class GameManager(LevelManager):
    def __init__(self, surface):
        super().__init__(surface)

    def run(self):
        self.run_level()

    def start(self):
        self.level_setup(0)
        self.run()

