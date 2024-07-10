class OldResistor:
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(OldResistor)

    def __init__(self,ohms):
        self._ohms = ohms

    def __repr__(self):
        return f'To jest obiekt klasy {self.__class__.__name__}'


    def get_ohms(self):
        return self._ohms

    def set_ohms(self,newohms):
        self._ohms = newohms
