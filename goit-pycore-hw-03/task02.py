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
