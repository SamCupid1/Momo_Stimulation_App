from security import *


#option to allow cash out
def allow_cash_out():
    print("Allowing cash out")
    if not check_pin():
        return
    print("Cash out allowed successfully! ")