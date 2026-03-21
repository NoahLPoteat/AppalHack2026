class scene:
    name = ""
    bg = ""
    characters = []
    lines = []
    def __init__(self, name):
        self.name=name
    def toDict(self):
        return {
            "name": self.name,
            "bg": self.bg,
            "chars": self.characters,
            "lines": self.lines
        }
    
    def play(self):
        pass


class dialogue:
    type = "" #text, choice, sprite
    text = ""
    speaker = "" #name on text box, and highlighting sprites