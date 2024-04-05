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
}


# TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
def check(coffee_type):
    if coffee_type == 'espresso':
        if resources['water'] >= MENU[coffee_type]['ingredients']['water']:

            return 1
        # else:
        #     print("Sorry there is not enough water.")
        #     return 0
        elif resources['coffee'] >= MENU[coffee_type]['ingredients']['coffee']:

            return 1
        else:
            print("Sorry there is not enough water.")
            return 0
    else:
        if resources['water'] >= MENU[coffee_type]['ingredients']['water']:
            return 1
        # else:
        #     print("Sorry there is not enough milk.")
        #     return 0
        elif resources['coffee'] >= MENU[coffee_type]['ingredients']['coffee']:

            return 1
        # else:
        #     print("Sorry there is not enough coffee.")
        #     return 0
        elif resources['milk'] >= MENU[coffee_type]['ingredients']['milk']:

            return 1
        else:
            print("Sorry there is not enough milk.")
            return 0


def coffee_maker(coffee_type):
    if coffee_type == 'espresso':
        resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
        resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']


def check_change(coffee_type, q, d, n, p):
    cost = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    if cost < MENU[coffee_type]['cost']:
        return MENU[coffee_type]['cost'] - cost
    elif cost == MENU[coffee_type]['cost']:
        return 0
    else:
        return -1


while True:

    while True:
        Money = 0
        ans = input("What would you like? (espresso/latte/cappuccino):")
        if ans == 'report':
            for y in resources:
                print(f"{y}: {resources[y]}")

            print(f"${Money}")
        else:
            break
    # drink = MENU[ans]
    if ans == 'off':
        break
    elif check(ans) == 0:
        break
    print("Please insert of coins.")
    qua = int(input("How many quarters?: "))
    dim = int(input("How many dimes?: "))
    nic = int(input("How many nickles?: "))
    pen = int(input("How many pennies?: "))
    if check_change(ans, qua, dim, nic, pen) == -1:
        print("Sorry that's not enough money. Money refunded.")
        break
    Money = Money + 0.25 * qua + 0.1 * dim + 0.05 * nic + 0.01 * pen
    change = check_change(ans, qua, dim, nic, pen)
    coffee_maker(ans)
    print(f"Here is ${change} in change")
    print(f"Here is your {ans} ☕ Enjoy!")
