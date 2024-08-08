print("_____________________________homework08________________________________________________________________")

import re
import pickle
from collections import UserDict
from datetime import datetime, timedelta
from functools import wraps
import pathlib
addressbook_file = pathlib.Path(__file__).parent / "data/addressbook.pkl"

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
    
    def get_phone(self):
        return self.phones[0]

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
            user_birthday_date = user_birthday.value.date()

            # check who have birthday for today and 7 day after
            for i in range(8):
                the_date = today + timedelta(days=(i))

                if user_birthday_date.day == the_date.day and user_birthday_date.month == the_date.month:
                    # check if bithday on weekday
                    if the_date.weekday() in [5, 6]:
                        the_date += timedelta(days=(7 - the_date.weekday()))
                        # print(the_date)
                    
                    congratulation_date = the_date.strftime("%d.%m.%Y")

                    # upcoming_birthdays.append({"name": user_name, "congratulation_date": congratulation_date})
                    upcoming_birthdays.append((user_name, congratulation_date))
                    break
    pizza_day_for = "; ".join(f"{name}: {date}" for name, date in upcoming_birthdays)
    return pizza_day_for

# _____________________________________________________________________________________________

# decorator_4_add_contacts
def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            name, phone = args[0]
            # must enter only letters for the contact name
            if not name.isalpha():
                raise ValueError("Input only alphabets for name please!")
            # must enter only digits for the phone number
            if not phone.isdigit():
                raise ValueError("Input only digits for phone number please!")
            
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name and phone please. Error: {e}"

    return wrapper

# decorator_4_change_contact
def change_input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            phone = args[0][1]
            # must enter only digits for the phone number
            if not phone.isdigit():
                raise ValueError("Input only digits for phone number please!")
            
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name and phone please. Error: {e}"

    return wrapper

# decorator_4_phone
def name_input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            name = args[0][0]
            # must enter only letters for the contact name
            if not name.isalpha():
                raise ValueError("Input only alphabets for name please!")
            
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name please. Error: {e}"

    return wrapper

# decorator_4_all
def all_input_error(func):
    @wraps(func)
    def wrapper(contacts):
        try:
            if len(contacts) == 0:
                return "Seems, we don't have any contacts! No contacts found."
            
            return func(contacts)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name please. Error: {e}"

    return wrapper

# decorator_4_input_parser
def command_input_error(func):
    @wraps(func)
    def wrapper(user_input):
        try:
            command, *args = user_input.split()
            command = command.strip().lower()
            
            if command in ["close", "exit"] and len(args) > 0:
                print(f"Enter \"{command}\" command without arguments!")
                return user_input
            elif command == "hello" and len(args) > 0:
                print(f"Enter \"{command}\" command without arguments!")
                return user_input
            elif command == "add" and len(args) > 2:
                print(f"Only 2 arguments for \"{command}\"command - name and phone number!")
                return user_input
            elif command == "change" and len(args) > 2:
                print(f"Only 2 arguments for \"{command}\" command - name and phone number!")
                return user_input
            elif command == "phone" and len(args) > 1:
                print(f"Enter only name for \"{command}\"command.")
                return user_input
            elif command == "all" and len(args) > 0:
                print(f"Enter \"{command}\" command without arguments!")
                return user_input
            
            return func(user_input)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name please. Error: {e}"

    return wrapper

# decorator_4_add_birthday
def input_error4bday(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            name, bday = args[0]
            # must enter only letters for the contact name
            if not name.isalpha():
                raise ValueError("Input only alphabets for name please!")
            # must enter only digits for the birthday number
            if not re.fullmatch(r'[\d.]+', bday):
                raise ValueError("Input only digits for birthday please!")
            
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name and birthday please. Error: {e}"

    return wrapper

# decorator_4_show-birthday
def input_error4show_birthday(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            name = args[0][0]
            # must enter only letters for the birthday name
            if not name.isalpha():
                raise ValueError("Input only alphabets for name please!")
            
            return func(*args, **kwargs)
        except AttributeError as e:
            return f"Actually, the contact does not have a birthday record."
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name please. Error: {e}"

    return wrapper

# decorator_4_birthdays
def input_error4birthday(func):
    @wraps(func)
    def wrapper(book):
        try:
            if len(book) == 0:
                return "Oooopsssss! Seems, we don't have any birthdays records! No birthdays found."
            
            return func(book)
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        except ValueError as e:
            return f"Give me just a name please. Error: {e}"

    return wrapper
# decorator_4_serialization
def serialization_errors(func):
    @wraps(func)
    def wrapper(book):
        try:
            return func(book)
        except FileNotFoundError as e:
            return f"Hmm, strange things happen sometimes, address book file not found."
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        
    return wrapper

def deserialization_errors(func):
    @wraps(func)
    def wrapper():
        try:
            return func()
        except FileNotFoundError as e:
            return f"Hmm, strange things happen sometimes, address book file not found."
        except IndexError as e:
            return f"Oh no, some index error. Error: {e}"
        
    return wrapper

@command_input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# add contact 
@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Error: Insufficient arguments. Expected format: 'add <name> <phone>'."
    
    name, phone, *_ = args
    record = book.find_record_by_name(name)
    message =  f"Contact {name} updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added."
    if phone:
        record.add_phone(phone)
    return message

# function which changes contact
@change_input_error
def change_contact_phone(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find_record_by_name(name)
    old_phones = ', '.join(str(phone) for phone in record.phones)
    
    if record:
        if  record.find_phone(phone):
            print("The phone already exists!")
        else:
            if phone:
                if old_phones:
                        list_of_old_phones = old_phones.split(',')
                        record.remove_phone(list_of_old_phones[0])
                        record.add_phone(phone)
                        return f"Phone number was changed for contact {name} to {phone}"
    else:
        return f"We don't have any contact {name}. Try another one."

# function shows phone number
@name_input_error
def phone_username(args, book: AddressBook):
    name = args[0]
    record = book.find_record_by_name(name)
    if record:
        phones = ', '.join(str(phone) for phone in record.phones)
        return f"The phone number(s) for {name} is/are: {phones}"
    else:
        return f"Contact {name} doesn't exist. Try another one."
    
# function displays all available contacts
@all_input_error
def all(book: AddressBook):
    print("\n" + "-" * 40 + "ALL RECORDS IN ADDRESS BOOK" + "-" * 40)
    for record in book.data.values():
        print(record)

# function adds birthday
@input_error4bday
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Error: Insufficient arguments. Expected format: 'add <name> <birthday>'."
    
    name, bday, *_ = args
    record = book.find_record_by_name(name)
    message =  f"Birthday for {name} updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added."
    if bday:
        record.add_birthday(bday)
    return message

@input_error4show_birthday
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find_record_by_name(name)
    if record:
        birthday = record.birthday.value.date().strftime("%d.%m.%Y")
        return f"The birthday for {name} is: {birthday}"
    else:
        return f"Contact {name} doesn't exist. Try another one."
    
@input_error4birthday
def birthdays(book: AddressBook):
    upcoming_birthdays2str = get_upcoming_birthdays(book)
    print(f"Greetings for: {upcoming_birthdays2str}")

@serialization_errors
def save_data(book, filename=addressbook_file):
    # make dir if doesn't exist
    filename.parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(book, f)

@deserialization_errors
def load_data(filename=addressbook_file):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    print("Hello my friend! Welcome to assistant bot!")

    while True:
        user_input = input("Enter a command >>> ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye my friend, see you late!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact_phone(args, book))
        elif command == "phone":
            print(phone_username(args, book))
        elif command == "all":
            print(all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print(f"Pardon, \"{user_input}\" command is invalid!")
    
    save_data(book)

if __name__ == "__main__":
    main()

# _____________________________________________________________________________________________
