
''' Version 1 - Ask if the user wants to make change'''
def get_value():
    while True:
        value = input("Enter a dollar amount: ")
        if value.isdigit:
            return float(value)

''' Version 1 - Simple Make Change function'''
def make_change(value):
    fifty = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if value > 0.0:
        fifty = int(value//.50)
        value = value - (fifty * .50)
        value = round(value, 2)
        print(f"Change: {value}")
    if value > 0.0:
        quarters = int(value//.25)
        value = value - (quarters * .25)
        value = round(value, 2)
        print(f"Change: {value}")
    if value > 0.0:
        dimes = int(value//.10)
        value = value - (dimes * .10)
        value = round(value, 2)
        print(f"Change: {value}")
    if value > 0.0:
        nickles = int(value//.05)
        value = value - (nickles * .05)
        value = round(value, 2)
        print(f"Change: {value}")
    if value > 0.0:
        pennies = int(value//.01)

    if pennies > 1:
        penny_str =  "Pennies: " + str(pennies)
    else: 
        penny_str =  "Penny: " + str(pennies)

    print(f"Fifty Cents: {fifty}, Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, {penny_str}")




''' Version 2 - Data struct '''
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

''' Version 2 - Utilizing the data structure to make change'''
def make_change_with_coins(value):
    value = value * 100
    change = []

    for i in range(len(coins)):
        print(coins[i])
        title, divsor = coins[i]
        print(f"title: {title}")
        print(f"divsor: {divsor}")
        times = int(value//divsor)
        value = int(value - (divsor * times))
        change.append((title, times))

    print(change)


def main():
    print("Welcome to the Change Maker 5000 (tm)")

    while True:
        value = get_value()
        #make_change(value)
        make_change_with_coins(value)


main()