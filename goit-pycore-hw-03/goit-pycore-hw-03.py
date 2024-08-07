print("_____________________________task01________________________________________________________________")

from datetime import datetime, date
import random

# actually current day
current_day = datetime.now().date()
print(f"Today is {current_day}.")

# function which calculate quantity of days from date to current day
def get_days_from_today(date):
    converted_date = datetime.strptime(date, "%Y-%m-%d").date()
    print(converted_date)

    q_days = (current_day - converted_date).days
   
    print(f"Soooo, there are {q_days} days from {date} till today!")


# Checking is user input correct date

correct_year = False
correct_month = False
correct_day = False

while not correct_year:
    year = input("Please, input year (4 digits) >>> ").strip()
    if year.isdigit() and len(year) == 4:
        correct_year = True
    else:
        print(f"Opppss! Sad, but {year} is not correct, try one more time! I'm believe in you!")
       
while not correct_month:
    month = input("Please, input month (2 digits) >>> ").strip()
    if month.isdigit() and len(month) == 2 and int(month) < 13:
        correct_month = True
    else:
        print(f"Opppss! Sad, but {month} is not correct, try one more time! I'm believe in you!")

while not correct_day:
    day = input("Please, input day (2 digits) >>> ").strip()
    if day.isdigit() and len(day) == 2 and int(day) < 32:
        correct_day = True
    else:
        print(f"Opppss! Sad, but {day} is not correct, try one more time! I'm believe in you!")

# date in correct format
date = f"{year}-{month}-{day}"

get_days_from_today(date)

import random

print("_____________________________task02________________________________________________________________")
lottery_finish = False

def get_numbers_ticket(min, max, quantity):
    number_range = []

    # get number range form min to max
    for i in range(min, max):
        number_range += [i]

    #get random unique numbers from a range and sort them
    is_numbers_unique = False
    while not is_numbers_unique:
        random_numbers = random.sample(number_range, quantity)
        random_numbers.sort()
    
        unique_random_numbers = set(random_numbers)
        clear_random_list = list(unique_random_numbers)
        clear_random_list.sort()

        is_numbers_unique = True if random_numbers == clear_random_list else print("List not unique, try again.")

    return random_numbers
# user should enter correct data for get random numbers
while True:
    try:
        quantity_of_winning_numbers = int(input("Please, enter quantity of winning numbers form 0 to 999 >>> "))
        
        min_possible_number = int(input("Please, enter minimum possible number in range form 1 to 1000 >>> "))

        max_possible_number = int(input("Please, enter maximum possible number, higher than (minimum + quantity of winning numbers) and <1000 >>> "))
        
        if quantity_of_winning_numbers < 0 or quantity_of_winning_numbers > 999:
            raise Exception("Be careful, enter how many winning numbers do you want! I know you can, let's go, from 1 to 999.")
        elif  min_possible_number < 1 or min_possible_number > 1000:
             raise Exception("Really? That's not funny! Minimum possible number isn't correct, enter correct number [0-1000]! Let's try again!")
        elif max_possible_number < 0 or max_possible_number > 1000 or max_possible_number < (quantity_of_winning_numbers + min_possible_number): 
             raise Exception("Hey, don't play with me, maximum number isn't correct. Read careful and enter maximum number! Let's go, one more time.")
        else:
             lottery_numbers = get_numbers_ticket(min_possible_number, max_possible_number, quantity_of_winning_numbers)
             print("Your lottery numbers:", lottery_numbers)
             break
    #  processing ValueError exeption if entered not a numbers
    except ValueError: 
        print("Ohh come on, enter only numbers, please!")
        continue
    except Exception as e:
        print (e)
        continue

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

    
    



