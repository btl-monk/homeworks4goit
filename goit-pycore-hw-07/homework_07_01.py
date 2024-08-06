print("_____________________________homework07_01________________________________________________________________")

import re
from collections import UserDict
from datetime import datetime, timedelta
from functools import wraps

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name can't be empty!")
        
        super().__init__(value)		

class Phone(Field):
    def __init__(self, value):
        self.phone_validation(value)
        super().__init__(value)

    def phone_validation(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Phone number must be 10 digits")

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, bday):
        if self.birthday == None:
            self.birthday = Birthday(bday)

    def remove_phone(self, phone):
        phone_2_remove = self.find_phone(phone)
        if phone_2_remove:
            self.phones.remove(phone_2_remove)

    def edit_phone(self, old_phone, new_phone):
        phone_2_edit = self.find_phone(old_phone)
        if phone_2_edit:
            self.phones.remove(phone_2_edit)
            self.add_phone(new_phone)
            print(f"{old_phone} was changed to {new_phone}.")
        else:
            print(f"Can't change {old_phone} for {self.name}. The number doesn't exist.")

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        phone_str = '; '.join(str(phone) for phone in self.phones)
        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name}, phones: {phone_str}{birthday_str}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
        print(f"{record} added!")

    def find_record_by_name(self, name):
        record = self.data.get(name)

        if record:
            print(f"Found something interesting! {record}")
            return record
        else:
            print(f"Nothing interesting. Contact with name '{name}' not found.")
            return None
        
    def delete_record_by_name(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contatc with name - '{name}' has been removed.")
        else:
            print(f"Can't remove {name}, cuz contact doesn't exit in contact book")

     # function that determines when to greet the users
def get_upcoming_birthdays(address_book):
    today = datetime.now().date()
    upcoming_birthdays = []

    for record in address_book.values():
        user_name = record.name.value
        user_birthday = record.birthday

        # convert users birthday date form string to date
        # user_birthday_date = datetime.strptime(user_birthday, ("%Y.%m.%d")).date()
        if user_birthday:
            user_birthday_date =user_birthday.value.date()

            # check who have birthday for today and 7 day after
            for i in range(8):
                the_date = today + timedelta(days=(i))

                if user_birthday_date.day == the_date.day and user_birthday_date.month == the_date.month:
                    # check if bithday on weekday
                    if the_date.weekday() in [5, 6]:
                        the_date += timedelta(days=(7 - the_date.weekday()))
                        print(the_date)
                    
                    congratulation_date = the_date.strftime("%d.%m.%Y")

                    # upcoming_birthdays.append({"name": user_name, "congratulation_date": congratulation_date})
                    upcoming_birthdays.append([user_name, congratulation_date])
                    break
    print(upcoming_birthdays)
    return upcoming_birthdays



# _____________________________________________________________________________________________

def show_all_records(address_book):
    print("\n" + "-" * 40 + "ALL RECORDS IN ADDRESS BOOK" + "-" * 40)
    for name, record in address_book.data.items():
        print(record)

book = AddressBook()
print("\n" + "-" * 40 + "ADD RECORDS TO ADDRESS BOOK" + "-" * 40)
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("9999999999")
john_record.add_birthday("09.08.1945")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday("09.08.2002")

book.add_record(jane_record)

tyson_record = Record("Mike Tyson")
tyson_record.add_phone("6666666666")

book.add_record(tyson_record)

show_all_records(book)

print("\n" + "-" * 40 + "FIND RECORD IN ADDRESS BOOK" + "-" * 40)
john = book.find_record_by_name("John")
trump = book.find_record_by_name("Trump")


print("\n" + "-" * 40 + f"Try to edit phone for {john.name}" + "-" * 40)
john.edit_phone("1234567890", "3987654321")

show_all_records(book)

found_phone = john.find_phone("3987654321")

print(f"\nFound phone for {john.name}: {found_phone}")

show_all_records(book)

print("\n" + "-" * 40 + "REMOVE SOME RECORDS FORM ADDRESS BOOK" + "-" * 40)
book.delete_record_by_name("Jane")
book.delete_record_by_name("Trump")

show_all_records(book)

print("\n" + "-" * 40 + "CONGRAT USERS FORM ADDRESS BOOK" + "-" * 40)
upcoming_birthdays = get_upcoming_birthdays(book)

print("List of upcoming birthdays of this week:", upcoming_birthdays)
