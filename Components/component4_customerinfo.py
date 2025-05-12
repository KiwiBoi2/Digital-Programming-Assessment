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
def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(email_regex, email))

# Defining getting user email function
def get_user_email(email):
    # Using function to verify the customer email
    while True:
        email = input("Please enter the your email in the following format: example@domain.com\n")
        # Check if the email is empty
        if is_valid_email(email):
            print("Customer email is valid.")
            customer_info["email"].append(email)
            print("Customer email has been added to the list.")
            print(customer_info)
            break
        else:
            print("Customer email is invalid. Please enter a valid email.")

# Defining phone number verification function
def is_valid_phone(phone):
    # Regular expression for validating a phone number
    phone_regex = r"^\+?[0-9]{1,3}[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,9}$"    
    return bool(re.fullmatch(phone_regex, phone))

# Defining getting user phone function
def get_user_phone(phone):
    # Using function to verify the customer phone
    while True:
        print("The following formats are accepted:\n 123 456 7890\n 123-456-7890\n 1234567890\n +12 34 567 890")
        phone = input("Please enter the your phone number\n")
        # Check if the phone number is empty
        if is_valid_phone(phone):
            print("Customer phone number is valid.")
            customer_info["phone"].append(phone)
            print("Customer phone number has been added to the list.")
            print(customer_info)
            break
        else:
            print("Customer phone number is invalid. Please enter a valid phone number.")

# Defining NZ address verification function
def is_valid_address(address):
    # Updated regex based on provided template format
    nz_regex = (
        r"^\d{1,5}\s+[A-Za-z0-9\s]+(?:,\s*[A-Za-z\s]+){1},\s+[A-Za-z\s]+,\s*\d{4}$"
    )
    return bool(re.fullmatch(nz_regex, address.strip()))

# Smarter formatter for names like O'Reilly, McDonald, Te Awamutu
def smart_capitalize_word(word):
    if not word:
        return word

    word = word.lower()
    
    # Handle O'Reilly
    if "'" in word:
        parts = word.split("'")
        return "'".join(part.capitalize() for part in parts)

    # Handle McDonald, MacKenzie
    if word.startswith("mc") and len(word) > 2:
        return "Mc" + word[2].upper() + word[3:]
    if word.startswith("mac") and len(word) > 3:
        return "Mac" + word[3].upper() + word[4:]

    # Regular capitalization
    return word.capitalize()

# Format address: smart capitalization while preserving commas
def format_address(address):
    parts = [part.strip() for part in address.split(',')]
    formatted_parts = []
    for part in parts:
        words = part.split()
        cap_words = [smart_capitalize_word(word) for word in words]
        formatted_parts.append(' '.join(cap_words))
    return ', '.join(formatted_parts)

# Main function: input, validate, format
def get_user_address(address):
    while True:
        print("Accepted NZ format example (must include street number, suburb, and city):")
        print("  319 Te Irirangi Drive, Flat Bush, Auckland 2016")
        print("  3/45 Something Street, Mount Eden, Auckland 1023")
        print("  23 O'Reilly Road, Manukau, Auckland 2110")
        address = input("Please enter your address:\n")
        if is_valid_address(address):
            formatted = format_address(address)
            print("Customer address is valid.")
            print(f"Formatted address: {formatted}")
            customer_info["address"].append(formatted)
            print("Customer address has been added to the list.")
            print(customer_info)
            break
        else:
            print("Customer address is invalid. Please enter a valid NZ address.")

# Calling the functions to get user information
get_user_name("name")        
get_user_email("email")
get_user_phone("phone")
get_user_address("address")