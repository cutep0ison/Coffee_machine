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
    "money": 0
}


# for espresso coffee
e_water = MENU["espresso"]["ingredients"]["water"]
e_coffee = MENU["espresso"]["ingredients"]["coffee"]


# function for espresso coffee
def resources_espresso(r_water, e_water, r_coffee, e_coffee):
    if r_water - e_water >= 0 and r_coffee - e_coffee >= 0:
        return True
    else:
        return False


# for latte coffee
l_water = MENU["latte"]["ingredients"]["water"]
l_milk = MENU["latte"]["ingredients"]["milk"]
l_coffee = MENU["latte"]["ingredients"]["coffee"]


# function for latte coffee
def resources_latte(r_water, l_water, r_milk, l_milk, r_coffee, l_coffee):
    if r_water - l_water >= 0 and r_milk - l_milk >= 0 and r_coffee - l_coffee >= 0:
        return True
    else:
        return False


# for cappuccino coffee
c_water = MENU["cappuccino"]["ingredients"]["water"]
c_milk = MENU["cappuccino"]["ingredients"]["milk"]
c_coffee = MENU["cappuccino"]["ingredients"]["coffee"]


# function for espresso coffee
def resources_cappuccino(r_water, c_water, r_milk, c_milk, r_coffee, c_coffee):
    if r_water - c_water >= 0 and r_milk - c_milk >= 0 and r_coffee - c_coffee >= 0:
        return True
    else:
        return False


resources_available = True
while resources_available:
    # for resources
    r_water = resources["water"]
    r_milk = resources["milk"]
    r_coffee = resources["coffee"]
    r_money = resources["money"]

    user_input = input("What would you like? (espresso(1.5$☕)/latte(2.5$☕)/cappuccino(3.0$☕)):")
    if user_input == "report":
        print(resources)
    elif user_input == "off":
        resources_available = False
    else:
        quater = float(input("Amount of quater: ")) * 0.25
        dimes = float(input("Amount of dimes: ")) * 0.10
        nickles = float(input("Amount of nickles: ")) * 0.05
        pennies = float(input("Amount of pennies: ")) * 0.01
        user_amount = quater + dimes + nickles + pennies
        cappuccino_cost = MENU["cappuccino"]["cost"]
        latte_cost = MENU["latte"]["cost"]
        espresso_cost = MENU["espresso"]["cost"]

        if user_input == "espresso":
            resources_espresso(r_water, e_water, r_coffee, e_coffee)
            if resources_espresso(r_water, e_water, r_coffee, e_coffee):
                if user_amount >= espresso_cost:
                    resources["water"] = r_water - e_water
                    resources["coffee"] = r_coffee - e_coffee
                    resources["money"] = r_money + espresso_cost
                    print(f"Here is your coffee ☕ and change: {round((user_amount - espresso_cost), 2)}$")
                else:
                    print("Pls,enter correct amount of money 😒")
            else:
                resources_available = False
                print(f'Sorry💔,not enough ingredients.Here is your refund {round(user_amount , 2)}$')
        elif user_input == "latte":  # calculation for latte coffee
            resources_latte(r_water, l_water, r_milk, l_milk, r_coffee, l_coffee)
            if resources_latte(r_water, l_water, r_milk, l_milk, r_coffee, l_coffee):
                if user_amount >= latte_cost:
                    resources["water"] = r_water - l_water
                    resources["milk"] = r_milk - l_milk
                    resources["coffee"] = r_coffee - l_coffee
                    resources["money"] = r_money + latte_cost
                    print(f"Here is your coffee ☕ and change: {round((user_amount - latte_cost), 2)}$")
                else:
                    print("Pls,enter correct amount of money 😒")
            else:
                resources_available = False
                print(f'Sorry💔,not enough ingredients.Here is your refund {round(user_amount , 2)}$')
        elif user_input == "cappuccino":
            resources_cappuccino(r_water, c_water, r_milk, c_milk, r_coffee, c_coffee)
            if resources_cappuccino(r_water, c_water, r_milk, c_milk, r_coffee, c_coffee):
                if user_amount >= cappuccino_cost:
                    resources["water"] = r_water - c_water
                    resources["milk"] = r_milk - c_milk
                    resources["coffee"] = r_coffee - c_coffee
                    resources["money"] = r_money + cappuccino_cost
                    print(f"Here is your coffee ☕ and change: {round((user_amount - cappuccino_cost), 2)}$")
                else:
                    print("Pls,enter correct amount of money 😒")
            else:
                resources_available = False
                print(f'Sorry💔,not enough ingredients.Here is your refund {round(user_amount , 2)}$')

