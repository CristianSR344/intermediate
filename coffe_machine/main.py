MENU = {
    """
    This Python program simulates a coffee machine that allows users to select different types of
    coffee, check available resources, make a purchase, and receive change.
    """
    
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "mocha": {
        "ingredients": {
            "water": 150,
            "milk": 200,
            "coffee": 30,
        },
        "cost": 4.5,
    }
}

machine_resources = {
    "water": 100,
    "milk": 500,
    "coffee": 100,
}
machine_money = 0.0

available_options = ["off", "report", "latte", "espresso", "cappuccino","mocha"]

#Print Report
def report(): #Prints the available resources
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g") 
    print(f"Money: ${machine_money}")


#Check if there are enough resources to make that drink
def check_ingredients(machine, coffee):
    for ingredient in coffee: #for each coffee ingredient 
        if coffee[ingredient] > machine[ingredient]: #Compares coffee ingredients with machine ingredients
            print(f"Sorry, there is not enough {ingredient}")
            return False
        
    return True
    


#If the ingredients are available then substracts the ingredients from the machine
def serve(coffee):
    
    for resource in MENU[coffee]["ingredients"]: #for each ingredient substract the coffee from the machine ingredients
        machine_resources[resource] -= MENU[coffee]["ingredients"][resource]
    print(f"Here is your {coffee.capitalize()}. Enjoy!")
    

#Receives coins
def receive_coins():
    money = 0.0

    print("Please insert coins.")
    money += (int(input("How many quarters? "))) * 0.25
    money += (int(input("How many dimes? "))) * 0.10
    money += (int(input("How many nickles? "))) * 0.05
    money += (int(input("How many pennies? "))) * 0.01

        
    return money

#Check coins
def check_coins(money):
    global machine_money #declares the global variable from machine money
    try:
        user = receive_coins() #receives coins from the user
        if user >= money: #if the user inserts more or equal amount of the cost then
            machine_money += money #adds money to the machine
            change = round(user-money,2) 
            print(f"Here is ${change} in change.") #Gives change to the user
        else:
            print("Sorry that's not enough money. Money refunded")
            return False
        return True
    except:
        print("Please enter an integer value. Ex 1, 2, 3, 4, 5")

on_off = True

while on_off:
    choice = input("What would you like? (espresso/latte/cappuccino/mocha)")
    
    if choice in available_options:
        match choice:
            case "espresso":
                if check_ingredients(machine_resources,MENU[choice]["ingredients"]): #Checks if the machine has available resources for the drink
                    if check_coins(MENU[choice]["cost"]):#if user enters more or equal money to the espresso
                        serve(choice)
                    
            case "latte":
                if check_ingredients(machine_resources,MENU[choice]["ingredients"]): #Checks if the machine has available resources for the drink
                    if check_coins(MENU[choice]["cost"]):#if user enters more or equal money to the espresso
                        serve(choice)
                    
                
            case "cappuccino": #if user enters more or equal money to the cappuccino
                if check_ingredients(machine_resources,MENU[choice]["ingredients"]): #Checks if the machine has available resources for the drink
                    if check_coins(MENU[choice]["cost"]):#if user enters more or equal money to the espresso
                        serve(choice)
                    
            
            case "mocha": #if user enters more or equal money to the cappuccino
                if check_ingredients(machine_resources,MENU[choice]["ingredients"]): #Checks if the machine has available resources for the drink
                    if check_coins(MENU[choice]["cost"]):#if user enters more or equal money to the espresso
                        serve(choice)
                    
                
            case "off":
                on_off = False
                
            case "report":
                report()
    
    else:
        print(f"{choice.capitalize()} is not a valid option! \n")
    
    

