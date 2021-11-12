from dz1 import User
import os
import json


class Product:
    def __init__(self, name="", cost="", quantity="", description=""):
        self.description = description
        self.quantity = quantity
        self.cost = cost
        self.name = name
        self.warehouse = dict()
        if name != "" and cost != "" and quantity != "" and description != "":
            with open("file3.json", "a") as file:
                if os.stat(file.name).st_size == 0:
                    self.warehouse.update({self.name: [self.cost, self.quantity, self.description]})
                    json.dump(self.warehouse, file, ensure_ascii=False, indent=3)
                    print("Товар добавлен")
                else:
                    with open("file3.json", "r") as file_json:
                        self.warehouse = json.load(file_json)
                        self.warehouse.update({self.name: [self.cost, self.quantity, self.description]})
                    with open("file3.json", "w") as file_json:
                        #file_json.seek(0)
                        json.dump(self.warehouse, file_json, ensure_ascii=False, indent=3)
                        print("Товар добавлен")

    def print_about_products(self):
        with open("file3.json", "r") as file_json:
            self.warehouse = json.load(file_json)
            for key, value in self.warehouse.items():
                print(key, value[0], value[2])

    def print_information_about_product(self):
        with open("file3.json", "r") as file_json:
            self.warehouse = json.load(file_json)
            if self.name in self.warehouse.keys():
                print(self.name, self.warehouse.get(self.name))


class Order:
    def __init__(self):
        self.dict_of_orders = dict()

    def make_order(self):
        name_of_user = input("Введите логин")
        passwd = input("Введите пароль")
        us = User(name_of_user, passwd)
        str = us.add_new_user()
        if str == "такой уже есть" or str == "Пользователь зарегестрирован":
            while True:
                answer = us.entrance_of_user()
                if answer == "Вход успешен":
                    break

        name_of_product = input("Введите продукт")
        count = input("Введите количество товара")
        with open("file3.json", "r") as file_json:
            self.dict_of_orders = json.load(file_json)
            if name_of_product in self.dict_of_orders.keys():
                if int(count) < int(self.dict_of_orders.get(name_of_product)[1]):
                    with open("file4.json", "a") as file:
                        if os.stat(file.name).st_size == 0:
                            json.dump({name_of_user: {name_of_product: [count, "не оплачен"]}}, file,
                                      ensure_ascii=False, indent=3)
                        else:
                            with open("file4.json", "r") as file_orders:
                                dictionary_of_orders = json.load(file_orders)
                                dictionary_of_orders.update({name_of_user: {name_of_product: [count, "не оплачен"]}})
                            with open("file4.json", "w") as file_orders:
                                json.dump(dictionary_of_orders, file_orders, ensure_ascii=False, indent=3)
                else:
                    print("Количество товаров больше, чем есть",
                          count + ">" + self.dict_of_orders.get(name_of_product)[1])
            else:
                print("Такого продукта нет")

    def check_order(self):
        name_of_user = input("Введите логин")
        passwd = input("Введите пароль")
        us = User(name_of_user, passwd)
        answer = us.entrance_of_user()
        if answer == "Вход успешен":
            try:
                with open("file4.json", "r") as file:
                    self.dict_of_orders = json.load(file)
                    if name_of_user in self.dict_of_orders.keys():
                        print(name_of_user, self.dict_of_orders.get(name_of_user))
            except:
                print("error")
        else:
            print(answer)

    def add_product_to_existing_order(self):
        name_of_user = input("Введите логин")
        passwd = input("Введите пароль")
        us = User(name_of_user, passwd)
        str = us.add_new_user()
        if str == "такой уже есть" or str == "Пользователь зарегестрирован":
            while True:
                answer = us.entrance_of_user()
                if answer == "Вход успешен":
                    break

        name_of_product = input("Введите продукт")
        count = input("Введите количество товара")
        with open("file3.json", "r") as file_json:
            self.dict_of_orders = json.load(file_json)
            if name_of_product in self.dict_of_orders.keys():
                with open("file4.json", "a") as file:
                    if os.stat(file.name).st_size == 0:
                        print("Заказ ещё не создан")
                    else:
                        with open("file4.json", "r+") as orders:
                            dictionary_of_orders = json.load(orders)
                            if name_of_product in dictionary_of_orders.get(name_of_user).keys():
                                dictionary_of_orders.get(name_of_user).update({name_of_product: [count, "не оплачен"]})
                                orders.seek(0)
                                json.dump(dictionary_of_orders, orders, ensure_ascii=False, indent=3)
                            else:
                                dictionary_of_orders.get(name_of_user).update({name_of_product: [count, "не оплачен"]})
                                orders.seek(0)
                                json.dump(dictionary_of_orders, orders, ensure_ascii=False, indent=3)
            else:
                print("Такого продукта нет")

    def pay_for_order(self):
        name_of_user = input("Введите логин")
        passwd = input("Введите пароль")
        us = User(name_of_user, passwd)
        answer = us.entrance_of_user()
        if answer == "Вход успешен":
            with open("file4.json", "r") as file:
                self.dict_of_orders = json.load(file)
                for key, values in self.dict_of_orders.get(name_of_user).items():
                    values[1] = "оплачен"
                    self.dict_of_orders.get(name_of_user).update({key: values})
            with open("file4.json", "w") as file_orders:
                json.dump(self.dict_of_orders, file_orders, ensure_ascii=False, indent=3)
        else:
            print(answer)


if __name__ == "__main__":
    while True:
        str = input("Введите 1 (Добавить товар), \n"
                    "Введите 2 (Просмотреть информацию о товаре), \n"
                    "Введите 3 (Посмотерть информацию о всех товарах), \n"
                    "Введите 4 (Сделать заказ), \n"
                    "Введите 5 (Узнать информацию о заказе), \n"
                    "Введите 6 (Заплатить за заказ), \n"
                    "Введите 7 (Добавить товар в заказ),\n"
                    "Введите 0 (Для выхода): ")
        if str == '1':
            name = input("Введите название товара: ")
            cost = input("Введите цену товара: ")
            quantity = input("Введите количество товара: ")
            description = input("Введите описание товара: ")
            product = Product(name, cost, quantity, description)

        elif str == '2':
            name = input("Введите название товара: ")
            product = Product(name)
            product.print_information_about_product()
        elif str == '3':
            product = Product()
            product.print_about_products()
        elif str == '4':
            order = Order()
            order.make_order()
        elif str == '5':
            order = Order()
            order.check_order()
        elif str == '6':
            order = Order()
            order.pay_for_order()
        elif str == '7':
            order = Order()
            order.add_product_to_existing_order()
        elif str == '0':
            print("Выход")
            break
        else:
            print("Не корректный ввод. Выход")
            break
