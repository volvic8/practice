class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name


rider = Rider("take yutaka")
horse = Horse("deep impact", rider)
