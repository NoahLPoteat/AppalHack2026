import json
from scene import scene

def write(sc):
    n = "./scenes/"+sc.name+".txt"
    f = open(n, "x")
    f.write(json.dumps(Sc.toDict()))
    f.close()



name = input("enter the name of the scene\n")

Sc = scene(name)


write(Sc)