print("_____________________________task04________________________________________________________________")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# add contact 
def add_contact(args, contacts):
    name, phone = args
# add a contact if user enters digits for a phone number
    if phone.isdigit():
        contacts[name] = phone
        return f"Contact {name} added."
    else:
        return "Input only digits for phone number, please!"

# function which changes contact
def change_contact_phone(args, contacts):
    name, phone = args
    
    if name in contacts:
        contacts[name] = phone
        return f"Phone number was changed for contact {name} to {phone}"
    else:
        return f"We don't have any contact {name}. Try another one."

# function shows phone number
def phone_username(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        return f"Contact {name} doesn't exist. Try another one."
    
# function displays all available contacts
def all(contacts):
    if not contacts:
        return "Seems, we don't have any contacts! No contacts found."
    
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
            print("Pardon, this command is invalid!")

if __name__ == "__main__":
    main()