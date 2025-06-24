from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

on_off = True

while on_off:
    
    choice = input(f"What would you like? ({menu.get_items()}): ")
    
    match choice:
        case "latte":
            if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
                if money_machine.make_payment(menu.find_drink(choice).cost):
                    coffee_maker.make_coffee(menu.find_drink(choice))
        
        case "espresso":
            if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
                if money_machine.make_payment(menu.find_drink(choice).cost):
                    coffee_maker.make_coffee(menu.find_drink(choice))
            
        case "cappuccino":
            if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
                if money_machine.make_payment(menu.find_drink(choice).cost):
                    coffee_maker.make_coffee(menu.find_drink(choice))
            
        case "off":
            on_off = False
            
        case "report":
            coffee_maker.report()
            money_machine.report()
