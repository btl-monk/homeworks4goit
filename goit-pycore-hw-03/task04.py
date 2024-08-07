print("_____________________________task04________________________________________________________________")
from datetime import datetime, timedelta

users = [
    {"name": "John Wick", "birthday": "1975.07.10"},
    {"name": "Luke Skywalke", "birthday": "1085.07.13"},
    {"name": " Darth Vader", "birthday": "0006.07.14"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
# function that determines when to greet the users
def get_upcoming_birthdays(users):
    today = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        user_name = user["name"]
        user_birthday = user["birthday"]

        # convert users birthday date form string to date
        user_birthday_date = datetime.strptime(user_birthday, ("%Y.%m.%d")).date()

        # check who have birthday for today and 7 day after
        for i in range(8):
            the_date = today + timedelta(days=(i))

            if user_birthday_date.day == the_date.day and user_birthday_date.month == the_date.month:
                # check if bithday on weekday
                if the_date.weekday() in [5, 6]:
                    the_date += timedelta(days=(7 - the_date.weekday()))
                    print(the_date)
                
                congratulation_date = the_date.strftime("%Y.%m.%d")

                upcoming_birthdays.append({"name": user_name, "congratulation_date": congratulation_date})
                break
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)

print("List of upcoming birthdays of this week:", upcoming_birthdays)

print("_________________________________________________________")
