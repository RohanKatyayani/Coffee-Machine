import sys

MENU = {
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
c_inserted = 0
# TODO 1: Print Report

def print_report():
    print(f"""
Water: {resources["water"]}ml 
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}
    """)

# TODO 2: Check Resources Sufficient

def resources_sufficient(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

# TODO 3: Process Coins
def coins_inserted():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) #0.25
    dimes = float(input("How many dimes?: ")) #0.10
    nickles = float(input("how many nickles?: ")) #0.05
    pennies = float(input("how many pennies?: ")) #0.01
# TODO: Calculate hwo many coins were inserted in total and add them.
    q_inserted = quarters * 0.25
    d_inserted = dimes * 0.10
    n_inserted = nickles * 0.05
    p_inserted = pennies * 0.01
    c_inserted = q_inserted + d_inserted + n_inserted + p_inserted

    return c_inserted

# TODO 5: Make Coffee
def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")

# TODO 4: Check Transaction Successful and repeat process until 'off' is called.

coffee_machine_is_on = True

while coffee_machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        print("Coffee Machine turning off...")
        sys.exit()
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        if resources_sufficient(user_input):
            c_inserted = coins_inserted()
            cost = MENU[user_input]["cost"]
            if c_inserted >= cost:
                change = round(c_inserted - cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                resources["money"] += cost
                make_coffee(user_input)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid input.")

    # cost = MENU[user_input]["cost"]
    # elif user_input == "espresso":
    #     resources_sufficient(user_input)
    #     coins_inserted()
    #     if c_inserted >= cost:
    #         resources["money"] += 1.5
    #         resources["water"] -= 50
    #         resources["coffee"] -= 18
    #         change = round(c_inserted - cost, 2)
    #         print(f"Here's ${change} in change. Enjoy your Espresso!")
    #     else:
    #         print("Sorry that's not enough money. Money refunded.")
    # elif user_input == "latte":
    #     resources_sufficient(user_input)
    #     coins_inserted()
    #     if c_inserted >= cost:
    #         resources["money"] += 2.5
    #         resources["water"] -= 200
    #         resources["milk"] -= 150
    #         resources["coffee"] -= 24
    #         change = round(c_inserted - cost, 2)
    #         print(f"Here's ${change} in change. Enjoy your Latte!")
    #     else:
    #         print("Sorry that's not enough money. Money refunded.")
    # elif user_input == "cappuccino":
    #     resources_sufficient(user_input)
    #     coins_inserted()
    #     if c_inserted >= cost:
    #         resources["money"] += 1.5
    #         resources["water"] -= 50
    #         resources["coffee"] -= 18
    #         change = round(c_inserted - cost, 2)
    #         print(f"Here's ${change} in change. Enjoy your Espresso!")
    #     else:
    #         print("Sorry that's not enough money. Money refunded.")