class FoodOrder:
    def __init__(self, customer_name, item,price):
        self.customer_name = customer_name
        self.item = item
        self.price = price
    def show_order(self):
        print("Customer Name:{}".format(self.customer_name))
        print("Item:{}".format(self.item))
        print("Price:{}".format(self.price))

order1 = FoodOrder("yojana","burger",200)
order2 = FoodOrder("yojana","MoMo",150)
print(order1,order2)
print(order1.customer_name,order2.customer_name)
print(order1.item,order2.item)
print(order1.price,order2.price)
'''
inside class : only define methods and attributes and
outside class : call methods, define and use objects
'''
# Suppose you are working for daraz application and u have to work for new brand of Laptop
#Create a class Laptop with brand, price and method show_details()

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:",self.brand)
        print("Price:",self.price)

L1 = Laptop("Dell",80000)
L1.show_details()
L2 = Laptop("Lenovo",50000)
L2.show_details()
