import random as rn

class Product:
    def __init__(self, id: str, price: float):
        self.id = id
        self.price = price

class CartItem:
    pass

class ShoppingCart:
    pass


class Shop:
    def create_stock(self, products_number: int) -> list[CartItem]:
        A = []
        for i in range(products_number):
            id = '0' * (8 - len(str(i))) + str(i)
            prod = Product(id=id, price = (rn.random() * 99 + 1))
            A += [CartItem(product=prod, quantity=(rn.random(1, 20)))]
        return A
    
    def __init__(self, products_number: int):
        self.stock = self.create_stock(products_number)
        self.shopping_carts = None

