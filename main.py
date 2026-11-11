from config import  HASHCODE
from transfer import transfer_money
from wallet import my_wallet
from  airtimes import airtime_and_bundle
from cash_out import allow_cash_out


print("MOMO STIMULATION APPLICATION ")

#The main interface you get after the passcode dialed
def main():

            print(" Welcome to Telester momo services ")
            print(" Select an operation \n "
                  "1. Transfer Money \n "
                  "2. Airtime and Bundle \n "
                  "3. Allow cash out \n "
                  "4. My wallet \n "
                  "0. Exit")
            print(" ")
            choice = input(" Enter choice :")

            # open transfer module
            if choice == "1":

                print("\nOPENING TRANSFER MODULE")
                transfer_money()

            # open airtime and bundle module
            elif choice == "2":
                print("\nOPENING AIRTIME AND INTERNET MODULE")
                airtime_and_bundle()

            # open cash out module
            elif choice == "3":
                print("\nOPENING CASH OUT MODULE")
                allow_cash_out()

            # open wallet module
            elif choice == "4":
                print("\nOPENING MY WALLET")
                my_wallet()

            # open transfer module
            elif choice == "0":
                print("\nThank you for using this application")
            #if invalid input
            else:
                print("You entered an invalid choice, Try again! ")
                return
#Start the program
def start():
    attempts = 0
    while attempts < 4:
        prompt = input("Please enter the HASHCODE :")
        if prompt == HASHCODE:
            main()

        else:
            attempts += 1
            print("You entered an invalid HASHCODE, Try again! ")
    print("You have entered multiple incorrect HASH-CODES.Try again later. ")
#Run
start()

