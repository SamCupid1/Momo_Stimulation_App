import config
from security import check_pin
from validate import validate_number


#Buy airtime only
def buy_airtime():
    print(" Buying Airtime\n")
    print(" Who do you want to buy the airtime for?: \n "
          "1. Buy for self \n"
          "2. Buy for others ")
    choice = input(" Select choice: ")

    # Buying airtime for self
    if choice == "1":
        recipient_number = None

    #buy for others
    elif choice == "2":
        recipient_number = input(" Enter recipient number: ")
        if not validate_number(recipient_number, ['055', '050', '020']):
            print("Invalid number")
            return

    else:
        print("Invalid option")
        return

    amount = input("Enter amount you want to buy : ")
    if not amount.isdigit():
        print("Invalid amount")
        return
    amount = float(amount)
    if amount > config.Current_balance:
        print("Insufficient amount ")
        return
    print(f" You are buying airtime of {amount:2f}.")
    confirm = input("Do you want to continue? (y/n): ").lower()
    if confirm != "y":
        print(" Operation cancelled")
        print("Thank you for using this application")
        return
    if not check_pin():
        return
    config.Current_balance -= amount
    print(f"Airtime bought successfully.\n"
          f"New balance is GHS{config.Current_balance:2f}."
          f"New balance is GHS{config.Current_balance:2f}. ")


# buy internet bundle only
def buy_bundle():
    bundles = {"1": (3, "497MB"),
               "2": (5, "980MB"),
               "3": (10, "1.2GB")}

    print("Who do you want to buy the internet bundle for?: \n"
          "1. Buy for self \n"
          "2. Buy for others ")
    choice = input(" Select option: ")

    #buy for self
    if choice == "1":
        recipient_number = None

    #buy for others
    elif choice == "2":
        recipient_number = input(" Enter recipient number: ")
        if not validate_number(recipient_number, ['059', '054', '024', '025', '055', '050', '020']):
            print("Invalid number")
            return

    else:
        return

    print(" Buying internet bundle offers \n")
    for key, value in bundles.items():
        print(f"{key}: GHS{value[0]} = {value[1]}.")
    print("0. Exit")

    select = input("Choose a bundle offer: ")
    if select not in bundles:
        return
    price, size = bundles[select]
    if price > config.Current_balance:
        print("Insufficient amount ")
        return
    print(f"Buy {size} for GHS{price:2f}. ")
    confirm = input("Do you want to continue? (y/n): ").lower()
    if confirm != "y":
        print(" Operation cancelled")
        return
    if not check_pin():
        return
    config.Current_balance -= price
    print(f"{size} bought successfully.\n"
          f"Your new balance is GHS{config.Current_balance:2f}. ")
    print("Thank you for using this application")


#Buying airtime or internet bundle
def airtime_and_bundle():
    print("Airtime and Bundle\n")
    print("What do you want to buy? : \n"
          " 1. Airtime \n "
          " 2. Internet bundle \n "
          " 0. Back to main menu")
    option = input("Enter your choice: ")
    if option == "1":
        buy_airtime()
    elif option == "2":
        buy_bundle()
    else:
        return
