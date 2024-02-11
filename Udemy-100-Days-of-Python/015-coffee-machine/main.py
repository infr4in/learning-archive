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
    "money": 0.0,
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def make_a_coffee(coffee, drink_ingredients):
    """Deduct the required ingredients from the resources."""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {coffee} ☕. Enjoy!")


def is_enough_res(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def is_enough_coins(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        resources["money"] += money_received
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    income = 0
    for coin in COINS:
        income += int(input(f"How many {coin}? ")) * COINS[coin]
    return income


def report():
    """Shows the current resource values."""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if user_choice in MENU:
        drink = MENU[user_choice]
        if is_enough_res(drink["ingredients"]):
            payment = process_coins()
            if is_enough_coins(payment, drink["cost"]):
                make_a_coffee(user_choice, drink["ingredients"])
    elif user_choice == "report":
        report()
    elif user_choice == "off":
        is_on = False
    else:
        print("There's no such command. You can only type 'report', 'off' or the coffee you want.")
