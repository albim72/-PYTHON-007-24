from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,n):
        return f"wartośc wynosi: {n}"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7


class Regular(Prototyp):
    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1888

    def policz_x(self):
        return super().policz_x() + self.y*1.6


rg = Regular(5,7)
print(f'metoda policz() -> {rg.policz()}')
print(f'metoda policz_x() -> {rg.policz_x()}')
print(rg.msg(10))
