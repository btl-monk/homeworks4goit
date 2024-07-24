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


