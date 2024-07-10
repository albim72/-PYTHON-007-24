class Book:
    def __init__(self,id,tytul,autor,rok):
        self._id = id
        self.tytul = tytul
        self._autor = autor
        self._rok = rok

    @property
    def tytul(self):
        return self._tytul

    @tytul.setter
    def tytul(self,nowytytul):
        self._tytul = "Nowy tytuł ->" + nowytytul

bk1 = Book(4,"Wiedźmin","Andrzej Sapkowski",2024)
print(bk1.tytul)
bk1.tytul = "Wiedźmin. Krew elfów"
print(bk1.tytul)
