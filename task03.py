print("_____________________________task03________________________________________________________________")
import re 

raw_numbers = [
    "+067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# function which normalize phone numbers to one standard
def normalize_phone(phone_number):
    # remove all extra symbols 
    clear_digits = re.sub(r"\D", "", phone_number)

    #number without code is 10 digit, so get clean phone number then add code for each one's
    # length of phone number is constanta 
    phone_number_length = 10
    if len(clear_digits) > phone_number_length:
        number_without_code = clear_digits[-10:]
        correct_phone_number = "+38" + number_without_code
        return correct_phone_number
    else:
        number_without_code = clear_digits
        correct_phone_number = "+38" + number_without_code
        return correct_phone_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print(" Normalized phone numbers for SMS-spam:", sanitized_numbers)

    
    


