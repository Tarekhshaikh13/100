import data
import os


# os.system('cls')

menu = data.MENU
resources = data.resources

money = 0


def check_resources(order):
    """returns false for insufficient resources"""
    for items in menu[order]["ingredients"]:
        quantity = menu[order]["ingredients"][items]
        if items == "water":
            if resources["water"] < quantity:
                return False
        elif items == "milk":
            if resources["milk"] < quantity:
                return False
        elif items == "coffee":
            if resources["coffee"] < quantity:
                return False

    return True


def took_money(coffee):
    global money
    amount = float(input("Enter the amount : $"))
    coffee_cost = menu[coffee]["cost"]
    if coffee_cost == amount:
        print("Thank you! ")
        money += coffee_cost
    elif coffee_cost < amount:
        print(f"change : ${amount-coffee_cost}")
        money += coffee_cost
    else:
        print("Money refunded (less amount)")
        took_money(coffee)


def serve_coffee(order):
    if check_resources(order):
        print("Sorry Not Enough Resources... ")
        return
    for wmc in menu[order]["ingredients"]:
        quantity = menu[order]["ingredients"][wmc]
        resources[wmc]-= quantity
    print(f"Enjoy Your :{order}")


def get_resources():
    global money
    for items in resources:
        print(f"{items} : {resources[items]}")
    print(f"money : ${money}")


def add_resources():
    for items in resources:
        quantity = float(input(f"Enter amount of {items} : "))
        resources[items] += quantity


def coffee_machine():
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        os.system('cls')

        if coffee_type == "report":
            get_resources()
        elif coffee_type == "add":
            add_resources()
        elif coffee_type == "off":
            break
        elif check_resources(coffee_type) == False:
            print("Not Enough Resources")
        else:
            took_money(coffee_type)
            serve_coffee(coffee_type)


coffee_machine()
















