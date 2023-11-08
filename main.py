from data import MENU
from coffee_report import get_report
from brew_coffee import brew_coffee

turn_off = False

while (not turn_off):
    print("Welcome to my coffee machine")
    print("MENU:")
    print("ITEMS - PRICE")
    for item in MENU:
        print(f"{item} - ${MENU[item]['cost']}")
    user_input = input("What would you like: ")
    # add report functionality - done
    if user_input == "report":
        get_report()
    elif user_input == "off":
        print("Shutting down coffee Machine..")
        print("Thank you for using my coffee machine")
        turn_off = True
        exit()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        brew_coffee(user_input)
