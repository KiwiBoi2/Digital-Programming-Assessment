# Import regular expression for validation
"""This file is used to gather customer information for the online store program."""
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
    """
    This function takes a string as input and checks if it is alphabetical.
    
    if it is alphabetical it returns True
    if it is not alphabetical it returns False
    The function allows letters, hyphens, apostrophes, and spaces
    it uses regular expression to check if the string is valid
    """
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
    """
    This function takes address number as input and checks if it is a number.
    
    if it is a number it adds it to the customerinfo dictionary
    if it is not a number it loops until a valid address number is entered
    The function allows numbers and letters (for apartment numbers)
    The function also checks if the address number is empty
    If any of these conditions are not met it loops until a valid address number is entered
    """
    # Allows only numbers
    while True:
        street_number = input("Please enter your address number: ")
        # Check if the address number is empty
        if re.fullmatch(r"\d+[a-zA-Z]?", street_number):
            print("Address number is valid.")
            customerinfo['address_number'] = street_number
            # Adding address number to the customerinfo dictionary
            print("Address number has been added to the list.")
            break
        else:
            print("Address number is invalid. Please enter a valid address number.")


# Defining address verification function
def address_street():
    """
    This function takes street name as input and checks if it is alphabetical.
    
    if it is alphabetical it adds it to the customerinfo dictionary
    if it is not alphabetical it loops until a valid street name is entered
    The function allows letters, hyphens, apostrophes, and spaces
    uses the is_alphabetical function to check if the street name is valid
    The function also removes spaces from the street name for validation
    """
    # Allows only letters, hypens, apostrophes, and spaces
    while True:
        street_name = input("Please enter your address street: ")
        # Check if the address street is empty
        unchecked_address_street = street_name.replace(" ", "")
        if is_alphabetical(unchecked_address_street):
            print("Address street is valid.")
            customerinfo['address'] = street_name
            print("Address street has been added to the list.")
            break
        else:
            print("Address street is invalid. Please enter a valid address street.")


# Calling functions
get_user_name()
address_number()
address_street()