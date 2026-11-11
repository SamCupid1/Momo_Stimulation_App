from security import *
import config
import time


def my_wallet():

    print("My wallet")
    print(" 1. Check balance\n 2. Top-up ")
    option = input("Enter your option: ")

    # checking account balance
    if option == "1":
        print(" Check balance ")
        if not check_pin():
            return
        print(f"Your available balance is GHS{config.Current_balance:2f}.")
        time.sleep(5)
        return

    # Topping up
    elif option == "2":
        print(" Top-up ")
        try:
            amount = float(input("Enter amount you want to top up: "))
        except ValueError:
            print("Invalid amount")
            return

        if amount <= 0:
            print("Invalid amount")
            return

        if not check_pin():
            return
        config.Current_balance += amount
        print(f"GHS{amount:2f} has been deposited into your account successfully. Your current balance is GHS{config.Current_balance:2f}.")
        time.sleep(5)
        print("Thank you for using this application")
        return
    else:
        print("Invalid option")
        return

