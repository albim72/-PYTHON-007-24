from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x=x

zlicz = Liczba(43)
print(zlicz.x)


@dataclass
class DLiczba:
    x:int
    # def __init__(self,z,y):
    #     self.z=z
    #     self.y=y

dlicz = DLiczba(543)
print(dlicz.x)
