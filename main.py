# Importing necessary libraries
import time  # For delays between printing messages
import re  # For regular expression validations
from random import randint  # For random name selection
import pandas as pd  # For handling menu data and formatting
from colorama import Fore, Style, init  # For coloured text to differentiate important information

# Auto reset colorama so default terminal colors are restored after each print
init(autoreset=True)

# name library for random name picker
names = [
    "Olivia", "James", "Charlotte", "Ethan", "Amelia", "Liam", "Sophie",
    "Benjamin", "Isla", "Noah", "Emily", "Lucas", "Ava", "Oliver", "Grace"
]

# Setting up customer information storage
customerinfo = {
    'name': '',  # Customer's name
    'address_number': '',  # Customer's address number
    'address_street': '',  # Customer's address street
    'address_suburb': '',  # Customer's address suburb
    'phone': '',  # Customer's phone number
}

# Pickup and Delivery constants
PICKUP_CONSTANT = 1
DELIVERY_CONSTANT = 2

# welcome function
def welcome():
    # Welcome banner for shop
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
    # name randomiser
    num = randint(0, 14)
    botname = names[num]
    # print welcome message
    print(banner)
    print("\nWelcome to Sharp Things, my name is", botname)
    print("I shall be assisting you in selecting and purchasing your blade\n")
    time.sleep(1)
    # Yellow colour to differentiate important information
    print(Fore.YELLOW + "Please note that all orders above $50 will receive free shipping,")
    print(Fore.YELLOW + "while orders below $50 will incur a shipping fee of $14.\n")
    time.sleep(1)


# Function to check the user's choice for pickup or delivery
def choice_checker():
    # Checking choice
    while True:
        try:
            choice = int(input("Please enter 1 or 2\n"))
            if PICKUP_CONSTANT <= choice <= DELIVERY_CONSTANT:
                # If pickup selected
                if choice == 1:
                    print("Pickup Selected")
                    time.sleep(0.5)
                    choice = 1
                    break
                # If delivery selected
                elif choice == 2:
                    print("Delivery Selected")
                    time.sleep(0.5)
                    choice = 2
                    break
                else:
                    choice = int(
                        input(Fore.RED + "That is not a valid number. Please enter 1 or 2"))
        except ValueError:
            print(Fore.RED + "That is not a valid number. Please enter 1 or 2")
    # Calling functions based on pickup or delivery choice
    if choice == 1:
        get_user_name()
        # Added delay so user can process information before next input
        time.sleep(0.5)
        get_user_phone_number()
        # Added delay so user can process information before next input
        time.sleep(0.5)
    elif choice == 2:
        get_user_name()
        # Added delay so user can process information before next input
        time.sleep(0.5)
        get_address_number()
        # Added delay so user can process information before next input
        time.sleep(0.5)
        get_address_street()
        # Added delay so user can process information before next input
        time.sleep(0.5)
        get_address_suburb()
        # Added delay so user can process information before next input
        time.sleep(0.5)
        get_user_phone_number()
        # Added delay so user can process information before next input
        time.sleep(0.5)


# Function to ask the user if they would like to pick up their item from the store or have it delivered
def pickup_delivery():
    # This function will ask the user if they would like to pick up their item from the store or have it be delivered
    # Ask for pickup or delivery
    print("Would you like to pick up your item from the store or have it be delivered? \nEnter 1 for Pickup \nEnter 2 for Delivery")
    # Call the choice_checker function to validate the user's choice
    choice_checker()


# Cost format function
def format_cost_column(df):
    df["cost"] = df["cost"].apply(lambda x: f"${x:,.2f}")
    return df


# Colour mapping for categories
# Different colors for each category to enhance readability and differentiation between categories
category_colors = {
    "European": Fore.BLUE,
    "Duelling": Fore.GREEN,
    "Asian": Fore.YELLOW,
    "Decorative": Fore.MAGENTA,
    "Practical": Fore.RED,
    "Accessories": Fore.CYAN,
}

# Menu info
# Formatted menu data with categories, sword types/names, and prices
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

    # Alignment and printing of menu for enhanced readability
    for category, group in menu_df.groupby("Category"):
        # Default color to white
        color = category_colors.get(category, Fore.WHITE)
        # Print category header with color
        # Using Fore.RESET_ALL to reset color after printing the category header
        print(f"\n{color}=== {category} ==={Style.RESET_ALL}")
        for _, row in group.iterrows():
            # {:2d} -> number (2 digits), {:25s} -> item name (25 characters wide, left-aligned), {:>6} -> price (right-aligned 6 spaces)
            print(
                # Using f-string formatting to print the item number, sword type, and price
                f"{row['Number']:2d}. {row['Sword Type']: <16} ${row['Price']:>9.2f}")
    time.sleep(5)  # Adding a delay to allow the user to read the menu before proceeding

    # Start order processing
    order = []

    # Loop order while ordering
    while True:
        choice = input(
            "\nEnter the number of the item you want to order (or 0 to finish ordering)\n")

        if not choice.isdigit():
            # If the input is not a digit, print an error message and continue the loop
            # using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Please enter a valid number")
            continue

        choice = int(choice)

        if choice == 0:
            break

        if choice in menu_df["Number"].values:
            item = menu_df.loc[menu_df["Number"] == choice].iloc[0]
            order.append(item)
            # Using Fore.YELLOW to print the message in yellow to indicate a successful addition
            print(Fore.YELLOW + f"Added {item['Sword Type']} to your order!")

        else:
            # If the choice is not in the menu, print an error message
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Invalid choice, please try again.")

    # Define order confirmation function
    def confirm_menu_order(order):
        confirm = input("Do you want to confirm your order? (Yes/No): ").strip().lower()
        if confirm == "yes":
            print(Fore.GREEN + "Thank you for your order!")
        elif confirm == "no":
            print(Fore.GREEN + "Order cancelled.")
            menu()
        else:
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
            confirm_menu_order(order)

    # Show final order
    if order:
        # Using Fore.LIGHTBLUE_EX to print the order summary in light blue to differentiate it from other messages
        print(Fore.LIGHTBLUE_EX + "\nYour Order Summary")
        total = 0
        # Using enumerate to number the items in the order
        for idx, item in enumerate(order, 1):
            # Using f-string formatting to print the item number, sword type, and price
            print(f"{idx}. {item['Sword Type']} - ${item['Price']:.2f}")
            # Calculate total cost
            total += item['Price']
        # If total cost is above $50, print a message indicating free shipping
        # If total cost is below $50, print a message indicating shipping cost
        if total > 50:
            # Use Fore.GREEN to print the shipping cost message in green to indicate important information
            print(Fore.GREEN + "Your order is above $50, shipping is free!")
        else:
            # Use Fore.YELLOW to print the shipping cost message in yellow to indicate important information
            print(Fore.YELLOW + "Your order is below $50, shipping is $14.")
            total += 14
        # Print the total cost of the order
        # Using f-string formatting to print the total cost with two decimal places
        print(f"\nTotal: ${total:.2f}")

    else:
        # If no items were ordered, print a message indicating that no order was placed
        # Using Fore.YELLOW to print the message in yellow to indicate important information
        print(Fore.YELLOW + "You didn't order anything.")
    confirm_menu_order(order)


# Defining alphabetical verification function
def is_alphabetical(input_string):
    # Allowing letters, hyphens, apostrophes, and spaces
    allowed_characters = r"[a-zA-Z\-']+"
    return bool(re.fullmatch(allowed_characters, input_string))


def is_numeric(input_string):
    # Allowing numbers and letters (for apartment numbers)
    allowed_characters = r"[0-9]+"
    return bool(re.fullmatch(allowed_characters, input_string))


# Defining getting user name function
def get_user_name():
    # Using function to verify the customer name
    while True:
        # Asking for customer name
        name = input("Please enter your name: ")
        # Remove spaces for validation
        unchecked_name = name.replace(" ", "")
        # Check if the name is empty
        if is_alphabetical(unchecked_name):
            # Using Fore.GREEN to print the message in green to indicate valid input
            print(Fore.GREEN + "Customer name is valid.")
            # .title() automatically capitalizes the first letter of each word for proper name formatting
            customerinfo['name'] = name.title()
            # Adding customer name to the customerinfo dictionary
            # Using Fore.CYAN to print the message in cyan to indicate successful addition
            print(Fore.CYAN + "Customer name has been added to the list.")
            break
        else:
            # If the name is not valid it prints this error message
            # loops until a valid name is entered
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Customer name is invalid. Please enter a valid name.")


# Defining address verification function
def get_address_number():
    # Allows only numbers
    while True:
        # Asking for address number
        street_number = input("Please enter your address number: ")
        # Check if the address number is empty
        if re.fullmatch(r"\d+[a-zA-Z]?", street_number):
            # Using Fore.GREEN to print the message in green to indicate valid input
            print(Fore.GREEN + "Address number is valid.")
            customerinfo['address_number'] = street_number
            # Adding address number to the customerinfo dictionary
            # Using Fore.CYAN to print the message in cyan to indicate successful addition
            print(Fore.CYAN + "Address number has been added to the list.")
            break
        else:
            # If the address number is not valid it prints this error message
            # loops until a valid address number is entered
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Address number is invalid. Please enter a valid address number.")


# Defining address verification function
def get_address_street():
    # Allows only letters, hypens, apostrophes, and spaces
    while True:
        # Asking for address street
        street_name = input("Please enter your address street: ")
        # Check if the address street is empty
        unchecked_address_street = street_name.replace(" ", "")
        if is_alphabetical(unchecked_address_street):
            # Using Fore.GREEN to print the message in green to indicate valid input
            print(Fore.GREEN + "Address street is valid.")
            # .title() automatically capitalizes the first letter of each word
            # for proper street name formatting
            customerinfo['address_street'] = street_name.title()
            # Adding address street to the customerinfo dictionary
            # Using Fore.CYAN to print the message in cyan to indicate successful addition
            print(Fore.CYAN + "Address street has been added to the list.")
            break
        else:
            # If the address street is not valid it prints this error message
            # loops until a valid address street is entered
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Address street is invalid. Please enter a valid address street.")


def get_user_phone_number():
    # Allows only numbers
    while True:
        # Asking for customer phone number
        customer_number = input("Please enter your phone number: ")
        # Check if the phone number is empty
        # Using is_numeric function to check if the phone number is valid
        # Valid meaning it contains only numbers and is less than or equal to 12 characters
        if is_numeric(customer_number) and len(customer_number) <= 12:
            # Using Fore.GREEN to print the message in green to indicate valid input
            print(Fore.GREEN + "Phone number is valid.")
            customerinfo['phone'] = customer_number
            # Adding phone number to the customerinfo dictionary
            # Using Fore.CYAN to print the message in cyan to indicate successful addition
            print(Fore.CYAN + "Phone number has been added to the list.")
            break
        else:
            # If the phone number is not valid it prints this error message
            # loops until a valid phone number is entered
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Phone number is invalid. Please enter a valid phone number.")


def get_address_suburb():
    # Allows only letters, hypens, apostrophes, and spaces
    while True:
        # Asking for address suburb
        suburb_name = input("Please enter your address suburb: ")
        # Check if the address street is empty
        unchecked_address_street = suburb_name.replace(" ", "")
        if is_alphabetical(unchecked_address_street):
            # Using Fore.GREEN to print the message in green to indicate valid input
            print(Fore.GREEN + "Address suburb is valid.")
            # .title() automatically capitalizes the first letter of each word
            # for proper street name formatting
            customerinfo['address_suburb'] = suburb_name.title()
            # Adding address street to the customerinfo dictionary
            # Using Fore.CYAN to print the message in cyan to indicate successful addition
            print(Fore.CYAN + "Address suburb has been added to the list.")
            break
        else:
            # If the address street is not valid it prints this error message
            # loops until a valid address street is entered
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Address suburb is invalid. Please enter a valid address suburb.")


def order_again():
    # Function to ask the user if they want to place another order
    question = "Do you want to place another order? (yes/no): "
    while True:
        # making sure the input is stripped of leading/trailing spaces and converted to lowercase for verification
        again = input(question).strip().lower()
        # If the user wants to order again, return to the main menu
        if again in ['yes', 'y']:
            # Using Fore.MAGENTA to print the message in magenta to indicate a successful order and return to menu
            print(Fore.MAGENTA + "Returning to the main menu...")
            # Call the main function to restart the process
            main()
            return True
        # If the user does not want to order again, exit the program
        elif again in ['no', 'n']:
            # Using Fore.MAGENTA to print the message in magenta to indicate a successful order and exit
            print(Fore.MAGENTA + "Thank you for your order. Goodbye!")
            return False
        else:
            # If the input is not valid, print an error message and ask again
            # Using Fore.RED to print the error message in red to indicate an error
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")


# Main function to run the program
def main():
    welcome()  # Call the welcome function
    pickup_delivery()  # Call the pickup_delivery function
    menu()  # Call the menu function to display the sword menu
    order_again()  # Call the order_again function to ask if the user wants to order again or exit


main()  # Call the main function to start the program