class MojaMeta(type):
    def __new__(cls,clsname,superclasses,attrs):
        print(f"____________ {cls.__class__.__name__} ______________")
        print(f"nazwa klasy: {clsname}")
        print(f"klasy dziedziczone: {superclasses}")
        print(f"słownik atrybutów: {attrs}")
        return type.__new__(cls, clsname,superclasses,attrs)
    def jedynka(cls):
        return 1

class Ekstra(type):
    def __new__(cls,clsname,superclasses,attrs):
        print(f"____________ Hej, jestem ekstra! ______________")


class S:
    pass

class F:
    pass

class Specjalna(S,metaclass=MojaMeta):
    pass

class B(Specjalna):
    pass

class C(F,B):
    pass

ck = C()

cf = C
print(cf.jedynka())
