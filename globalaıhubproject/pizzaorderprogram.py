import datetime
import csv


import pandas as pd
menu = pd.read_csv("C:\\Users\\irem\\Desktop\\globalaıhubproject\\menu.csv")
print(menu)

#Reading the menu from the menu.csv file

class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost
    
#Creating the Pizza superclass

class Classic(Pizza):
    cost = 30.0

    def __init__(self):
        self.description = "Classic Materials: Mushrooms, Onions, Olives"
        print(self.description +"\n")

class Margherita(Pizza):
    cost = 20.0

    def __init__(self):
        self.description = "Margherita Materials: Tomatoes, Basil , Mozzarella"
        print(self.description +"\n")

class TurkPizza(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Turk Materials: Meat, Corn, Onions"
        print(self.description +"\n")

class PlainPizza(Pizza):
    cost = 10.0
    
    def __init__(self):
        self.description = "Plain Materials: GoatCheese, Tomatoes"
        print(self.description +"\n")
        
#Creating the subclasses of the pizza superclass    

class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
          
#Creating the PizzaDecorater superclass

class Olives(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class Mushrooms(Decorator):
    cost = 7.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class GoatCheese(Decorator):
    cost = 9.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class Meat(Decorator):
    cost = 11.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class Onions(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

class Corn(Decorator):
    cost = 6.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)
        
#Creating the subclasses of the PizzaDecorater superclass


def main():
    pizzas = {
        "1": {"name": "Classic", "price": 30.0},
        "2": {"name": "Margherita", "price": 20.0},
        "3": {"name": "TurkPizza", "price": 50.0},
        "4": {"name": "PlainPizza", "price": 10.0}

    }
    
    sauces = {
        "11": {"name": "Olives", "price": 5.0},
        "12": {"name": "Mushrooms", "price": 7.0},
        "13": {"name": "GoatCheese", "price": 9.0},
        "14": {"name": "Meat", "price": 11.0},
        "15": {"name": "Onions", "price": 5.0},
        "16": {"name": "Corn", "price": 6.0}
          }

# Printing menu
    print("PIZZA MENU")
    print("----------")
    for key, value in pizzas.items():
        print(key + ". " + value["name"] + " - $" + str(value["price"]))
    print("\nSAUCE MENU")
    print("----------")
    for key, value in sauces.items():
        print(key + ". " + value["name"] + " - $" + str(value["price"]))


    pizza_choice = input("Please choose a pizza (1-4): ")
    while pizza_choice not in pizzas.keys():
        pizza_choice = input("Invalid choice. Please choose a pizza (1-4): ")
    sauce_choice = input("Please choose a sauce (11-16): ")
    while sauce_choice not in sauces.keys():
        sauce_choice = input("Invalid choice. Please choose a sauce (11-16): ")

# Getting user input

 
    pizza_price = pizzas[pizza_choice]["price"]
    sauce_price = sauces[sauce_choice]["price"]
    total_price = pizza_price + sauce_price
    
# Calculate total price

    name = input("Please enter your name: ")
    id_number = input("Please enter your id number: ")
    card_number = input("Please enter your card number: ")
    card_password = input("Please enter your card password: ") 
    time_of_order = datetime.datetime.now()
    
# Getting user information

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, id_number, card_number, card_password, order.get_description(), time_of_order])
    print("your order has been approved.")







    main()








   

    


    

