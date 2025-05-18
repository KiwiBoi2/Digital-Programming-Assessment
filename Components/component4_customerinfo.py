# Import regular expressions for validation
import re
# Setting up customer information storage
customer_info = {
    "name": [],
    "email": [],
    "phone": [],
    "address": [],
}

# Defining alphabetical verification function
def is_alphabetical(name):
    # Allowing letters, hyphens, apostrophes, and spaces
    allowed_characters = r"[a-zA-Z-']+"  
    return bool(re.fullmatch(allowed_characters, name))

# Defining getting user name function
def get_user_name(name):
    # Using function to verify the customer name
    while True:
        name = input("Please enter the your name: ")
        # Remove spaces for validation
        unchecked_name = name.replace(" ", "")  
        # Check if the name is empty
        if is_alphabetical(unchecked_name):
            print("Customer name is valid.")
            customer_info["name"].append(name)
            print("Customer name has been added to the list.")
            print(customer_info)
            break
        else:
            print("Customer name is invalid. Please enter a valid name.")

# Defining email verification function
# Get email (must contain '@' and '.')
def get_user_email():
    while True:
        email = input("Please enter your email (example@domain.com): ").strip()
        if "@" in email and "." in email:
            print("Email accepted.")
            customer_info["email"].append(email)
            break
        else:
            print("Invalid email. Please try again.")

# Get phone (must be digits only, or contain basic separators)
def get_user_phone():
    while True:
        phone = input("Please enter your phone number: ").strip()
        cleaned = phone.replace(" ", "").replace("-", "").replace("+", "")
        if cleaned.isdigit():
            print("Phone number accepted.")
            customer_info["phone"].append(phone)
            break
        else:
            print("Invalid phone number. Please try again.")

# Get address (must contain at least 3 parts: street, suburb, city)
def get_user_address():
    while True:
        address = input("Please enter your address (e.g. 319 Te Irirangi Drive, Flat Bush, Auckland 2016): ").strip()
        parts = address.split(",")
        if len(parts) >= 3:
            print("Address accepted.")
            customer_info["address"].append(address)
            break
        else:
            print("Invalid address. Please include street, suburb, and city/postcode.")

# Run prompts
get_user_name("name")
get_user_email("email")
get_user_phone("phone")
get_user_address("address")

# Print final customer info
print("\nCollected Customer Info:")
print(customer_info)
