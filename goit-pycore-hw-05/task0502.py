print("_____________________________task02________________________________________________________________")

import re
from typing import Callable

def generator_numbers(text: str):
    # using a regular expression to get all numbers in the text
    pattern = r'(\b\d+\.\d+|\b\d+)'
    matches = re.findall(pattern, text)

    for match in matches:
        yield float(match)

        if match:
            print("Found income:", match)
            
# function which use generator for calculating total 
def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total += number
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers) 

if total_income == 0:
    print("Very sad, but no income was found.")
else:
    print(f"Total income is: {total_income}")



