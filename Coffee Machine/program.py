MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 850,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 1500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 1300,
    }
}
profit = 0
resources = {
    "water": 500,
    "milk": 700,
    "coffee": 200,
}


def check_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f'Sorry there is not enough {items}')
            return False
    return True


def process_money():
    print('Please insert Money.')
    total = int(input('How many 2000?: '))*2000
    total += int(input('How many 500?: '))*500
    total += int(input('How many 200?: ')) *200
    total += int(input('How many 100?: '))*100
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Payment Successful. Here\'s your change ₹{change}')
        profit += drink_cost
        return True
    elif money_received < drink_cost:
        print('Insufficient Funds. Here\'s your refund')
        return False


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f'Here is your {drink_name} ☕️, Enjoy')


machine_on = True

while machine_on:
    take_order = input('What would you like? (Espresso/ Latte/ Cappuccino): ').lower()
    if take_order == "off":
        machine_on = False
    elif take_order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}") 
    else:
        drink = MENU[take_order]
        if check_resources(drink['ingredients']):
            payment = process_money()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(take_order, drink['ingredients'])
