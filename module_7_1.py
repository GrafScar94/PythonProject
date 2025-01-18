from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        st = file.read()
        file.close()
        return st

    def add(self, *products):
        with open(self.__file_name, 'a') as file:
            for i in products:
                s = (str(i))
                f = Shop.get_products(self)
                if s in f:
                    print(f'Продукт {s} уже был в магазине, его общий вес')
                else:
                    file.write(f'{s}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
