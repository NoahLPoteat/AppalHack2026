import json
from src.scene import scene, dialogue

def write(sc):
    n = "./scenes/"+sc.name+".json"
    f = open(n, "x")
    f.write(json.dumps(Sc.toDict(), indent=4))
    f.close()



name = input("enter the name of the scene\n")
Sc = scene(name)
print("bg todo")
print("chars todo")

flag = True


while flag:
    text = input("choose sprite, choice or exit. anything else is a dialogue line\n")
    line = dialogue()
    match(text):
        case "sprite": line.type = "sprite"
        case "choice": line.type = "choice"
        case "exit": flag = False; continue
        case _: line.type = "text"; line.text = text
    Sc.lines.append(line.__dict__)
        
write(Sc)