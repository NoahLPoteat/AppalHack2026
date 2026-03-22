import json

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
    choices = []


class choice:
    text = ""
    next_scene = ""
    transition = False
    affections = "c+1, j-1"
    

def loadJSON(pathname):
    with open(pathname, "r") as json_data:
        d = json.loads(json_data.read())
        json_data.close()
    print(d)
    sc = scene(d["name"])
    sc.bg = d["bg"]
    sc.characters = d["chars"]
    sc.lines = d["lines"]
    return sc
    