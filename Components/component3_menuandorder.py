# import pandas as library
import pandas as pd
# import colorama as library
from colorama import Fore, Style, init
# Auto reset colorama
init(autoreset=True)

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
        print(f"\nTotal: ${total:.2f}")

    else:
        print("You didn't order anything.")
    confirm_order(order)

menu()
