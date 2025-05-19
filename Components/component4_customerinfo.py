# Import regular expression for validation
import re
# Setting up customer information storage
customerinfo = {
    'name': '',
    'address_number': '',
    'address': '',
    'phone': '',
}

# Defining alphabetical verification function
def is_alphabetical(input_string):
    # Allowing letters, hyphens, apostrophes, and spaces
    allowed_characters = r"[a-zA-Z\-']+"
    return bool(re.fullmatch(allowed_characters, input_string))

# Defining getting user name function
def get_user_name():
    # Using function to verify the customer name
    while True:
        name = input("Please enter your name: ")
        # Remove spaces for validation
        unchecked_name = name.replace(" ", "")
        # Check if the name is empty
        if is_alphabetical(unchecked_name):
            print("Customer name is valid.")
            customerinfo['name'] = name
            print("Customer name has been added to the list.")
            break
        else:
            print("Customer name is invalid. Please enter a valid name.")
            
# Defining address verification function
def address_number():
    # Allows only numbers
    while True:
        address_number = input("Please enter your address number: ")
        # Check if the address number is empty
        if re.fullmatch(r"\d+[a-zA-Z]?", address_number):
            print("Address number is valid.")
            customerinfo['address_number'] = address_number
            print("Address number has been added to the list.")
            break
        else:
            print("Address number is invalid. Please enter a valid address number.")

# Calling functions
get_user_name()
address_number()