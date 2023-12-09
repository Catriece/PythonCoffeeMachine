MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_wallet = 0

# TODO 4: Check sufficiency of resources


def compare_resources(needed_ingredient, resource_level):
    """Compares current resource level in machine to ingredient needed to make the drink.
    Returns false if the needed ingredient exceeds the current resource level of machine."""
    if needed_ingredient > resource_level:
        return False
    else:
        return True


def check_resources(drink_choice):
    """Uses compare_resources function to check availability of individual ingredients.
    If one ingredient is unavailable, an alert is sent."""
    ingredients = drink_choice["ingredients"]
    for ingredient in ingredients:
        resource_check = compare_resources(ingredients[f"{ingredient}"], resources[f"{ingredient}"])
        if resource_check is False:
            print(f"Sorry, there is not enough {ingredient}.\n")
            print_report()
            return False

    # TODO 5a: Ask user number of quarters, dimes, nickles, pennies being inserted


def calculate_monies_in():
    """Calculates the amount of money input by converting amount of coins into a dollar amount. Returns the total."""
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters: "))
    dimes = 0.10 * int(input("How many dimes: "))
    nickles = 0.05 * int(input("How many nickles: "))
    pennies = 0.01 * int(input("How many pennies: "))

    total = quarters + dimes + nickles + pennies
    return total


# function to compare money in and cost of coffee
def compare_cost(drink_choice_cost, money_from_user):
    """Compares the amount of money put into the machine to the cost of the drink. Returns change if necessary."""
    if money_from_user > drink_choice_cost:
        refund = money_from_user - drink_choice_cost
        print(f"Money refunded: ${round(refund, 2)}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# TODO 7: Make coffee for user


def make_drink(drink_choice):
    """Deducts ingredients used to make drink of choice from the resources available in the coffee machine."""
    ingredients = drink_choice["ingredients"]
    for ingredient in ingredients:
        resources[f"{ingredient}"] = resources[f"{ingredient}"] - ingredients[f"{ingredient}"]
    print("\nMaking your drink...\n")


def print_report():
    """Prints report of coffee machines resources"""
    print(f"\nCoffee Machine Report:\nWater: {resources["water"]}ml\n"
          f"Milk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${machine_wallet}")

# TODO 2b: Set a flag and while loop otherwise that keeps machine on
machine_off = False

while not machine_off:

    # TODO 1: Prompt user by asking "What would you like?
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 3: Print report when user enters "report"
    if choice == 'report':
        print_report()

    # TODO 2: Turn off Coffee Machine by entering "off"
    # TODO 2a: If "choice" input equals "off" turn machine off.

    elif choice == 'off':
        print("\nPowering down...")
        machine_off = True

    else:

        # TODO 1a: Select drink from menu
        drink = MENU[choice]
        continue_on = check_resources(drink)

        if continue_on is False:
            continue
        else:
            # TODO 5: Process coins
            money_in = calculate_monies_in()
            print("\nMoney in: $", round(money_in, 2))
            print("Price of drink: $", round(drink["cost"], 2))
            try_payment = compare_cost(drink["cost"], money_in)

            # TODO 6: Check success of transaction
            if try_payment is True:
                machine_wallet += drink["cost"]
                make_drink(drink)
                print(f"Here is your {choice}. Enjoy!")
            else:
                continue

