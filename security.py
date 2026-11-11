
from config import *
#Ask for pin and check if it's correct
def check_pin():
    pin = input(" Enter 4-digit pin code ")
    if pin == str(PIN_CODE):
        return True
    else:
        print("Incorrect pin code")
        return False