#utwórz klasę Kolo(Figura) - zaimplementuj model figury i policz pole koła
#w pliku main policz pole koła dla promienia = 5.5
#pole = pi*r**2 (math.pi)

from figura import Figura
import math

class Kolo(Figura):
    def __init__(self,a):
        super().__init__(a)

    # def __init__(self,a):
    #     super().__init__(a,0)

    def policz_pole(self):
        return math.pi*self.a**2

