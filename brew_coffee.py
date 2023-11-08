from data import resources, MENU


def is_ingredient_present(coffee_type):
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("Insufficient Water. Sorry")
        return False
    elif MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient Coffee. Sorry")
        return False
    elif MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("Insufficient Milk. Sorry")
        return False
    else:
        return True


def add_transaction(coffee_type):
    print("Please insert the coins: ")
    dollars = int(input("Enter the amount of $: "))
    quarters = int(input("Enter the amount of quarters: "))
    total_money = dollars + (0.25 * quarters)
    if total_money < MENU[coffee_type]["cost"]:
        print("\n-------------ERROR START--------------\n")
        print(f"Sorry. You do not have enough money to buy {coffee_type}.")
        print(f"Cost: ${MENU[coffee_type]['cost']}")
        print(f"You inserted: ${total_money}")
        print("\n-------------ERROR END--------------\n")
        return False
    elif total_money == MENU[coffee_type]["cost"]:
        print("\n-------------TRANSACTION START--------------\n")
        print(f"Here is your {coffee_type} coffee. Enjoy!")
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["money"] += MENU[coffee_type]["cost"]
        print("\n-------------TRANSACTION END--------------\n")
        return True
    else:
        change = total_money - MENU[coffee_type]["cost"]
        print("\n-------------TRANSACTION START--------------\n")
        print(f"Here is your {coffee_type} coffee. Enjoy!")
        print("Please collect your change: ")
        print(f"change: {change}")
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["money"] += MENU[coffee_type]["cost"]
        print("\n-------------TRANSACTION END--------------\n")
        return True


def brew_coffee(coffee_type):
    if is_ingredient_present(coffee_type):
        if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
            if add_transaction(coffee_type):
                print("Thank you for using my coffee machine")
        else:
            print("Sorry, we don't have that coffee")
