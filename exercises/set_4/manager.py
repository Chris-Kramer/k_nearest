import phone_book
import sys

def main():
  option = input("""Type
  'search'       to search by name
  'add' or 'new' to create a new entry  
  'edit'         to edit an existing entry
  'set'          to add or edit an entry
  'quit'         to quit the manager
Enter your choice: """)
  if option == 'search':
    search()
  elif option == 'add' or option == 'new':
    add()
  elif option == 'edit':
    edit()
  elif option == 'set':
    add_or_edit()
  elif option == 'quit':
    sys.exit()
  else:
    print(f"'{option}' is not a valid command.")
  main()

def search():
  name = input("Enter the name to serarch: ")
  try:
    number = phone_book.get(name)
    print(number)
  except phone_book.ContactNotFoundError:
    print(f"No entry found for {name}.")

def add():
  name = input("Enter a name for the new entry: ")
  number = input_phone_number(f"Enter a phone number for {name}: ")
  try:
    phone_book.add(name,number)
  except phone_book.DuplicateContactError:
    print(f"There is already an entry for {name}.")

def edit():
  name = input("Enter a name for the entry to update: ")
  number = input_phone_number(f"Enter a phone number for {name}: ")
  try:
    phone_book.update(name,number)
  except phone_book.ContactNotFoundError:
    print(f"There is no entry for {name}.")

def add_or_edit():
  name = input("Enter a name: ")
  number = input_phone_number(f"Enter a phone number for {name}: ") 
  try:
    phone_book.add(name,number)
  except phone_book.DuplicateContactError:
    phone_book.update(name,number)

def input_phone_number(message):
  n = input(message)
  if phone_book.is_phone_number(n):
    return n
  else:
    print(f"'{n}' is not a phone number.")
    return input_phone_number(message)
  
if __name__ == "__main__":
  main()
