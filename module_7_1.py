# Домашнее задание по теме "Режимы открытия файлов"
# Задача "Учёт товаров":

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name,} {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        s = ''
        file = open(self.__file_name, 'r' )
        s += (file.read())
        file.close()
        return s

    def add(self, *products):
        file = open(self.__file_name, 'a+')
        file.seek(0)
        sp = file.readlines()
        sp = [i.strip() for i in sp]
        for i in products:
            if str(i) not in sp:
                file.write(str(i) + '\n')
            else:
                print(f'Продукт {i} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

