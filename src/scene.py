import json

class scene:
    name = ""
    bg = ""
    lines = []
    next_scene_default = ""
    def __init__(self, name):
        self.name=name
    def toDict(self):
        return {
            "name": self.name,
            "bg": self.bg,
            "lines": self.lines,
            "next_scene_default": self.next_scene_default
        }

class dialogue:
    type = "" #text, choice
    text = "" #leave blank for choice
    displayname = ""
    speaker = "" #sprites
    emotion = "" #basic/empty, happy, sad, angry
    choices = [] # leave blank for type==text
    #a dict containing a list of dicts is jank, apparantly
    def dict2(self):
        d = self.__dict__
        if self.choices:
            d["choices"] = [i.__dict__ for i in self.choices]
        return d


class choice:
    text = ""
    next_scene = "" #json
    transition = False #whether to actually change the scene or just quiet change
    affections = "" #ex c+1, j-1
    response = "none" # say "none" if blank
    

def loadJSON(pathname):
    with open(pathname, "r") as json_data:
        d = json.loads(json_data.read())
        json_data.close()
    print(d)
    sc = scene(d["name"])
    sc.bg = d["bg"]
    sc.lines = d["lines"]
    sc.next_scene_default = d["next_scene_default"]
    return sc
    