from data import MENU

MONEY = 0


def resource_limit():
    print(f"Water: {resources['water']}gm")
    print(f"Milk: {resources['milk']}gm")
    print(f"Coffee: {resources['coffee']}gm")
    print(f"Money: ${MONEY}")


def coin_check():
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quart = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = quart * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def calculation(cost, money):
    if cost > money:
        print("Sorry that's not enough money. Money refunded.")
    elif cost < money:
        money -= cost
        print(f"Here is ${round(money, 2)} in change.")
        global MONEY
        MONEY += cost
    return money


def check_drink(drink, resource):
    count = 0
    for supply in drink:
        if resource[supply] < drink[supply]:
            print(f"Sorry there is not enough {supply}")
            count += 1
    if count == 0:
        for supply in drink:
            resource[supply] = resource[supply] - drink[supply]
    return resource


# def resource_sufficient(resource, money):
def check_answer(choice):
    if choice == "report":
        resource_limit()
    elif choice == "espresso":
        money = coin_check()
        is_money_enough = calculation(rate, money)
        if is_money_enough >= 0:
            print(f"Here is your {choice} ☕. Enjoy!")
    elif choice == "latte":
        money = coin_check()
        is_money_enough = calculation(rate, money)
        if is_money_enough >= 0:
            print(f"Here is your {choice} ☕. Enjoy!")
    elif choice == "cappuccino":
        money = coin_check()
        is_money_enough = calculation(rate, money)
        if is_money_enough >= 0:
            print(f"Here is your {choice} ☕. Enjoy!")


resources = {"water": 300, "milk": 200, "coffee": 100}

is_machine_off = True
while is_machine_off:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')
    if user_choice == "off":
        is_machine_off = False
    elif user_choice == "report":
        check_answer(user_choice)
    else:
        rate = float(MENU[user_choice]["cost"])
        check_answer(user_choice)
        check_drink(MENU[user_choice]["ingredients"], resources)
