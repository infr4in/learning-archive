from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower().strip()
    if choice in menu.get_items().split("/"):
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        print("There's no such command. You can only type 'report', 'off' or the coffee you want.")