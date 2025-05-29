# Importing necessary libraries
import random
import re
from random import randint
import pandas as pd
from colorama import Fore, Style, init
# Auto reset colorama
init(autoreset=True)

#name library for random name picker
names = ["Olivia","James","Charlotte","Ethan","Amelia","Liam","Sophie","Benjamin","Isla","Noah","Emily","Lucas","Ava","Oliver","Grace"]


# Setting up customer information storage
customerinfo = {
    'name': '',
    'address_number': '',
    'address_street': '',
    'address_suburb': '',
    'phone': '',
    
}


# Pickup and Delivery constants
PICKUP_CONSTANT = 1
DELIVERY_CONSTANT = 2

#welcome function
def welcome():
    #Welcome banner for shop
    banner = """ _____                                                                                                  _____ 
( ___ )------------------------------------------------------------------------------------------------( ___ )
 |   |                                                                                                  |   | 
 |   |   ██████  ██░ ██  ▄▄▄       ██▀███   ██▓███     ▄▄▄█████▓ ██░ ██  ██▓ ███▄    █   ▄████  ██████  |   | 
 |   | ▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██░ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒██    ▒  |   | 
 |   | ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▓██░ ██▓▒   ▒ ▓██░ ▒░▒██▀▀██░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░ ▓██▄    |   | 
 |   |   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▄█▓▒ ▒   ░ ▓██▓ ░ ░▓█ ░██ ░██░▓██▒  ▐▌██▒░▓█  ██▓ ▒   ██▒ |   | 
 |   | ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒▒██▒ ░  ░     ▒██▒ ░ ░▓█▒░██▓░██░▒██░   ▓██░░▒▓███▀▒██████▒▒ |   | 
 |   | ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒▓▒░ ░  ░     ▒ ░░    ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒▒ ▒▓▒ ▒ ░ |   | 
 |   | ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░▒ ░            ░     ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░░ ░▒  ░ ░ |   | 
 |   | ░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░ ░░            ░       ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░   ░░  ░  ░   |   | 
 |   |       ░   ░  ░  ░      ░  ░   ░                           ░  ░  ░ ░           ░       ░      ░   |   | 
 |___|                                                                                                  |___| 
(_____)------------------------------------------------------------------------------------------------(_____)
"""
    #name randomiser
    num = randint(0,14)
    botname = (names[num])
    #print welcome message
    print(banner)
    print(f"\nWelcome to Sharp Things, my name is", botname)
    print("I shall be assisting you in selecting and purchasing your blade\n")

# Function to check the user's choice for pickup or delivery
def choice_checker():
    #Checking choice
    while True:
        try:
            choice = int(input("Please enter 1 or 2\n"))
            if choice >= PICKUP_CONSTANT and  choice <= DELIVERY_CONSTANT:
                #If pickup selected
                if choice == 1:
                    print("Pickup Selected")
                    # Set the choice to 1 for pickup
                    # This will be used later in the code to determine if the user chose pickup or delivery
                    choice = 1
                    break
                #If delivery selected
                elif choice == 2:
                    print("Delivery Selected")
                    # Set the choice to 2 for delivery
                    # This will be used later in the code to determine if the user chose pickup or delivery
                    choice = 2
                    break
                else:
                    choice = int(input("That is not a valid number. Please enter 1 or 2"))
        except ValueError:
            print("That is not a valid number. Please enter 1 or 2")
    # Calling functions based on pickup or delivery choice
    if choice == 1:
        get_user_name()
        get_user_phone_number()
        
    elif choice == 2:
        get_user_name()
        get_address_number()
        get_address_street()
        get_address_suburb()
        get_user_phone_number()

# Function to ask the user if they would like to pick up their item from the store or have it delivered
def pickup_delivery():
    #This function will ask the user if they would like to pick up their item from the store or have it be delivered
    #Ask for pickup or delivery
    print("Would you like to pick up your item from the store or have it be delivered? \nEnter 1 for Pickup \nEnter 2 for Delivery")
    # Call the choice_checker function to validate the user's choice
    choice_checker()


# Cost format function
def format_cost_column(df):
    df["cost"] = df["cost"].apply(lambda x: f"${x:,.2f}")
    return df

# Colour mapping for categories
category_colors = {
    "European": Fore.BLUE,
    "Duelling": Fore.GREEN,
    "Asian": Fore.YELLOW,
    "Decorative": Fore.MAGENTA,
    "Practical": Fore.RED,
    "Accessories": Fore.CYAN,
}

# Menu info
menu_data = [
    # European Swords
    {"Category": "European", "Sword Type": "Arming Sword", "Price": 1000},
    {"Category": "European", "Sword Type": "Longsword", "Price": 1500},
    {"Category": "European", "Sword Type": "Bastard Sword", "Price": 1500},
    {"Category": "European", "Sword Type": "Claymore", "Price": 2000},
    {"Category": "European", "Sword Type": "Falchion", "Price": 1000},
    
    # Duelling Swords
    {"Category": "Duelling", "Sword Type": "Rapier", "Price": 1500},
    {"Category": "Duelling", "Sword Type": "Sabre", "Price": 1200},
    {"Category": "Duelling", "Sword Type": "Estoc", "Price": 1500},

    # Asian Swords
    {"Category": "Asian", "Sword Type": "Katana", "Price": 15000},
    {"Category": "Asian", "Sword Type": "Wakizashi", "Price": 7000},
    {"Category": "Asian", "Sword Type": "Dao", "Price": 1500},
    {"Category": "Asian", "Sword Type": "Jian", "Price": 1000},
    
    # Decorative Swords
    {"Category": "Decorative", "Sword Type": "Replicas", "Price": 500},
    {"Category": "Decorative", "Sword Type": "Custom Blades", "Price": 1500},
    
    # Practical Swords
    {"Category": "Practical", "Sword Type": "Training Blades", "Price": 700},
    {"Category": "Practical", "Sword Type": "Feder Blades", "Price": 1000},
    {"Category": "Practical", "Sword Type": "Wooden Blades", "Price": 200},
    
    # Accessories
    {"Category": "Accessories", "Sword Type": "Scabbards", "Price": 150},
    {"Category": "Accessories", "Sword Type": "Sword Stands", "Price": 100},
    {"Category": "Accessories", "Sword Type": "Maintenance Kits", "Price": 45},
]

def menu():
    # Weapon list display function
    # Create DataFrame
    menu_df = pd.DataFrame(menu_data)

    # Sort by category
    menu_df = menu_df.sort_values(by="Category")

    # Reset index and reassign numbering
    menu_df = menu_df.reset_index(drop=True)
    menu_df.insert(0, "Number", range(1, len(menu_df) + 1))

    # Alignment and printing
    for category, group in menu_df.groupby("Category"):
        # Default color to white
        color = category_colors.get(category, Fore.WHITE)
        print(f"\n{color}=== {category} ==={Style.RESET_ALL}")
        for _, row in group.iterrows():
            # {:2d} -> number (2 digits), {:25s} -> item name (25 characters wide, left-aligned), {:>6} -> price (right-aligned 6 spaces)
            print(f"{row['Number']:2d}. {row['Sword Type']: <16} ${row['Price']:>9.2f}")


    # Start Order
    order = []

    # Loop order while ordering
    while True:
        choice = input("\nEnter the number of the item you want to order (or 0 to finish ordering)\n")

        if not choice.isdigit():
            print("Please enter a valid number")
            continue

        choice = int(choice)

        if choice == 0:
            break 

        if choice in menu_df["Number"].values:
            item = menu_df.loc[menu_df["Number"] == choice].iloc[0]
            order.append(item)
            print(f"Added {item['Sword Type']} to your order!")

        else:
            print("Invalid choice, please try again.")

    # Define order confirmation function
    def confirm_order(order):

        confirm = input("Do you want to confirm your order? (Yes/No): ").strip().lower()
        if confirm == "yes":
            print("Thank you for your order!")
        elif confirm == "no":
            print("Order cancelled.")
            menu()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_order(order)
    # Show final order
    if order:
        print("\nYour Order Summary")
        total = 0
        for idx, item in enumerate(order, 1):
            print(f"{idx}. {item['Sword Type']} - ${item['Price']:.2f}")
            total += item['Price']
        if total > 50:
            print(Fore.GREEN + "Your order is above $50, shipping is free!")
        else:
            print(Fore.RED + "Your order is below $50, shipping is $14.")
            total += 14
        print(f"\nTotal: ${total:.2f}")

    else:
        print("You didn't order anything.")
    confirm_order(order)


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
            customerinfo['address_street'] = street_name.title()
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
            customerinfo['address_suburb'] = suburb_name.title()
            # Adding address street to the customerinfo dictionary
            print("Address suburb has been added to the list.")
            break
        else:
            # If the address street is not valid it prints this error message
            # loops until a valid address street is entered
            print("Address suburb is invalid. Please enter a valid address suburb.")


def main():
    welcome()  # Call the welcome function
    pickup_delivery()  # Call the pickup_delivery function
    menu()  # Call the menu function to display the sword menu

main()