#check if recipient number entered is in the right format
def validate_number(recipient_number,prefix):

    if recipient_number.isdigit() and len(recipient_number) ==10 :
        for n in prefix:
            if recipient_number.startswith(n):
                return True
    return False