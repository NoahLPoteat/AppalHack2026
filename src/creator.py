import json
from scene import scene, dialogue, choice

def write(sc):
    n = "./scenes/"+sc.name+".json"
    f = open(n, "x")
    f.write(json.dumps(Sc.toDict(), indent=4))
    f.close()



name = input("enter the name of the scene\n")
Sc = scene(name)
Sc.bg = input("bg filename (not path)\n")


flag = True


while flag:
    text = input("line of dialogue or 'exit' or 'choice'\n")
    line = dialogue()
    line.choices = []
    match(text):
        case "exit": flag = False; continue

        #currently broken
        case "choice":
            line.type = "choice"

            flag2 = True
            while flag2:
                decide = input("'new' choice or 'exit'\n")
                if decide == "exit":
                    flag2=False
                    continue
                choosy = choice()
                choosy.text = input("text display for choice\n")
                choosy.next_scene = input("next scene name or 'none'\n")
                trans = input("play transition? t/f\n")
                choosy.transition = True if trans == "t" else False
                choosy.affections = input("changes to affection (eg c+1 or 'none')\n")
                choosy.response = input("single line response or 'none'\n")
                line.choices.append(choosy)
            
            

        case _:
            line.type = "text"
            line.text = text
            line.displayname = input("displayname\n")
            line.speaker = input("speaker ('java' 'pierce' 'cindy' 'none')\n")
            line.emotion = input("speaker emotion ('basic' 'happy' 'sad' 'angry')\n")

    Sc.lines.append(line.dict2())

Sc.next_scene_default = input("next scene if no choice is made\n")

write(Sc)