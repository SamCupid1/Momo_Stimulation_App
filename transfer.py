from sys import prefix

import config
from security import  check_pin
from validate import validate_number

def transfer_money():
    global Current_balance
    print(" Transferring Money")
    print(" 1. Telester \n 2. Other networks \n 0. Exit")
    option = input("Select network type: ")

    # Transfer to telester number
    if option == "1":
        print(" Transferring to telester user ")
        # prefix = ['059','054','024','025']
        charge_rate = 0.005
    elif option == "2":
        print(" Transferring to other networks ")
        #prefix = ['055','050','020']
        charge_rate = 0.01
    elif option == "0":
        print("Thank you for using this application")
        return
    else:
        print("Invalid option")
        return

    recipient_number = input("Please enter recipient number that begins with('059','054','024','025'): ")
    if not validate_number(recipient_number,['059','054','024','025']):
        print("Invalid number")
        return
    amount = input("Enter amount to transfer: ")
    if not amount.isdigit():
        print("Invalid amount")
        return

    amount = float(amount)
    charges = charge_rate * amount
    total = amount + charges

    if total > config.Current_balance:
        print("Insufficient amount ")
        return


    print(f" Transferring GHS {amount:1f} to {recipient_number}. \n "
          f"You will be charged GHS ", total)
    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != "y":
        print("Transaction cancelled!")
        return
    if not check_pin():
        return
    config.Current_balance -= total
    print(f" Transferred successfully\n"
            f"You have transferred GHS {amount:2f} to {recipient_number}. \n "
            f"Your current balance is GHS {config.Current_balance:3f}. ")
    print("Thank you for using this application")

