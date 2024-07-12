from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper


def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls


class DebugMeta(type):
    def __new__(cls, clsname,bases,attrs):
        obj = super().__new__(cls, clsname,bases,attrs)
        obj = debugmethods(obj)
        return obj

    def __init__(cls, clsname,bases,attrs):
        cls.fc = cls.fc

    def fc(cls):
        return "ważna informacja"


class Base(metaclass=DebugMeta):pass

class Calc(Base):
    def add(self,x,y):
        return (x+y)*100

    def mul(self,x,y):
        return 0.5*x*y

    def div(self,x,y):
        return x/(y+10)

    @classmethod
    def licz(cls,a,b):
        return a-2*b

    @staticmethod
    def costam(self,i):
        return i*90

mc = Calc()
print(mc.add(4,7))
print(mc.mul(4,7))
print(mc.div(4,7))
print(mc.licz(4,7))
print(mc.costam(56))

print(mc.fc())

print(Calc.fc())
