print("_____________________________task04________________________________________________________________")

from functools import wraps

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

@command_input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# add contact 
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

# function which changes contact
@change_input_error
def change_contact_phone(args, contacts):
    name, phone = args
    
    if name in contacts:
        contacts[name] = phone
        return f"Phone number was changed for contact {name} to {phone}"
    else:
        return f"We don't have any contact {name}. Try another one."

# function shows phone number
@name_input_error
def phone_username(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        return f"Contact {name} doesn't exist. Try another one."
    
# function displays all available contacts
@all_input_error
def all(contacts):
    contact_list = "Contacts:\n"
    for name, phone in contacts.items():
        contact_list += (" - " f"{name}: {phone}\n")
    
    return contact_list.strip()

def main():
    contacts = {}

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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print(f"Pardon, \"{user_input}\" command is invalid!")

if __name__ == "__main__":
    main()