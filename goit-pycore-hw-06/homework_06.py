print("_____________________________homework06________________________________________________________________")
import re
from collections import UserDict

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

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

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
        return f"Contact name: {self.name}, phones: {phone_str}"

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


def show_all_records(address_book):
    print("\n" + "-" * 40 + "ALL RECORDS IN ADDRESS BOOK" + "-" * 40)
    for name, record in address_book.data.items():
        print(record)

book = AddressBook()
print("\n" + "-" * 40 + "ADD RECORDS TO ADDRESS BOOK" + "-" * 40)
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("9999999999")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")

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
