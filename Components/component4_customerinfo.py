# Import regular expressions for validation
import re
# Setting up customer information storage
customer_info = {
    "name": [],
    "email": [],
    "phone": [],
    "address": [],
    "city": [],
}

# Defining alphabetical verification function
def is_alphabetical(name):
    # Allowing letters, hyphens, apostrophes, and spaces
    allowed_characters = r"[a-zA-Z-']+"  
    return bool(re.fullmatch(allowed_characters, name))
# Using function to verify the customer name
while True:
    name = input("Please enter the your name: ")
    # Remove spaces for validation
    unchecked_name = name.replace(" ", "")  
    # Check if the name is empty
    if is_alphabetical(unchecked_name):
        print("Customer name is valid.")
        customer_info.append(name)
        print("Customer name has been added to the list.")
        print(customer_info)
        break
    else:
        print("Customer name is invalid. Please enter a valid name.")
