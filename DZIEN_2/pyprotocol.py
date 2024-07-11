from typing import List,Protocol

class Item(Protocol):
    quantity:float
    price:float

    def total_price(self)->float:
        ...

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price
    def total_price(self)->float:
        return self.quantity*self.price


def calculate_total(items:List[Item])->float:
    return sum([item.total_price() for item in items])

total = calculate_total([
    Product('A',10,24.5),
    Product('B',2,145.6),
    Product('C',7,12),
    Product('Z',22,8.44),
    Product('X',3,99)
])

print(total)
