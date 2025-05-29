# Import regular expression for validation
"""This file is used to gather customer information for the online store program."""
import re


# Setting up customer information storage
customerinfo = {
    'name': '',
    'address_number': '',
    'address': '',
    'suburb': '',
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


def is_numeric(input_string):
    """
    This function takes a string as input and checks if it is numeric.
    if it is numeric it returns True
    if it is not numeric it returns False
    The function allows numbers and letters (for apartment numbers)
    it uses regular expression to check if the string is valid
    """
    # Allowing numbers and letters (for apartment numbers)
    allowed_characters = r"[0-9]+"
    return bool(re.fullmatch(allowed_characters, input_string))


# Defining getting user name function
def get_user_name():
    """
    This function takes customer name as input and checks if it is alphabetical.
    if it is alphabetical it adds it to the customerinfo dictionary
    if it is not alphabetical it loops until a valid name is entered
    """
    # Using function to verify the customer name
    while True:
        name = input("Please enter your name: ")
        # Remove spaces for validation
        unchecked_name = name.replace(" ", "")
        # Check if the name is empty
        if is_alphabetical(unchecked_name):
            print("Customer name is valid.")
            # .title() automatically capitalizes the first letter of each word
            # for proper name formatting
            customerinfo['name'] = name.title()
            # Adding customer name to the customerinfo dictionary
            print("Customer name has been added to the list.")
            break
        else:
            # If the name is not valid it prints this error message
            # loops until a valid name is entered
            print("Customer name is invalid. Please enter a valid name.")


# Defining address verification function
def get_address_number():
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
            # If the address number is not valid it prints this error message
            # loops until a valid address number is entered
            print("Address number is invalid. Please enter a valid address number.")


# Defining address verification function
def get_address_street():
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
            # .title() automatically capitalizes the first letter of each word
            # for proper street name formatting
            customerinfo['address'] = street_name.title()
            # Adding address street to the customerinfo dictionary
            print("Address street has been added to the list.")
            break
        else:
            # If the address street is not valid it prints this error message
            # loops until a valid address street is entered
            print("Address street is invalid. Please enter a valid address street.")


def get_user_phone_number():
    """
    This function takes phone number as input and checks if it is a number.
    if it is a number it adds it to the customerinfo dictionary
    if it is not a number it loops until a valid phone number is entered
    The function allows numbers and letters (for apartment numbers)
    The function also checks if the phone number is empty
    If any of these conditions are not met it loops until a valid phone number is entered
    """
    # Allows only numbers
    while True:
        customer_number = input("Please enter your phone number: ")
        # Check if the phone number is empty
        if is_numeric(customer_number) and len(customer_number) <=12:
            print("Phone number is valid.")
            customerinfo['phone'] = customer_number
            # Adding phone number to the customerinfo dictionary
            print("Phone number has been added to the list.")
            break
        else:
            # If the phone number is not valid it prints this error message
            # loops until a valid phone number is entered
            print("Phone number is invalid. Please enter a valid phone number.")


def get_address_suburb():
    """
    This function takes suburb name as input and checks if it is alphabetical.
    if it is alphabetical it adds it to the customerinfo dictionary
    if it is not alphabetical it loops until a valid street name is entered
    The function allows letters, hyphens, apostrophes, and spaces
    uses the is_alphabetical function to check if the suburb name is valid
    """
    # Allows only letters, hypens, apostrophes, and spaces
    while True:
        suburb_name = input("Please enter your address suburb: ")
        # Check if the address street is empty
        unchecked_address_street = suburb_name.replace(" ", "")
        if is_alphabetical(unchecked_address_street):
            print("Address suburb is valid.")
            # .title() automatically capitalizes the first letter of each word
            # for proper street name formatting
            customerinfo['address'] = suburb_name.title()
            # Adding address street to the customerinfo dictionary
            print("Address suburb has been added to the list.")
            break
        else:
            # If the address street is not valid it prints this error message
            # loops until a valid address street is entered
            print("Address suburb is invalid. Please enter a valid address suburb.")
