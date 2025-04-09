#import pandas as library
import pandas as pd
#import colorama as library
from colorama import Fore, Back, Style, init

# Cost format function
def format_cost_column(df):
    df["cost"] = df["cost"].apply(lambda x: f"${x:,.2f}")
    return df

# Weapon list display function
def weapon_list():
    
    # Create menu dictionary
    menu_dict = {}
        
    # Add category numbers and names to dictionary
    menu_dict["categoryName"] = ["Medieval European", "Renaissance and Duelling", "Asian and Eastern",
                                 "Fantasy and Decorative", "Practical and Training"]
    
    # Create new menu for each weapon category
    menu_Europe = {
        "swordType": ["Arming Sword", "Longsowrd", "Bastard sword", "Claymore", "Falchion"],
        "cost" : [1000, 1500, 1500, 2000, 1000]
    }
    
    menu_Duelling = {
        "swordType": ["Rapier", "Sabre", "Estoc"],
        "cost" : [1500, 1200, 1500]
    }
    
    menu_Asia = {
        "swordType": ["Katana", "Wakizashi", "Dao", "Jian"],
        "cost" : [15000, 7000, 1500, 1000]
    }
    
    menu_Decor = {
        "swordType": ["Replicas", "Custom Blades"],
        "cost" : [500, 1500]
    }
    
    menu_Practical = {
        "swordType": ["Training Blades", "Feder Blades", "Wooden Blades"],
        "cost" : [700, 1000, 200]
    }
    
    # Print all dictionaries
    # Print Menu Categories
    print("Menu Categories:")
    print(pd.DataFrame(menu_dict, index=range(1, len(menu_dict["categoryName"]) + 1)).to_string(col_space=10))
    
    print("\nMedieval European Swords:")
    df = pd.DataFrame(menu_Europe, index = range(1, len(menu_Europe["swordType"]) + 1))
    df = format_cost_column(df)
    print(df.to_string(col_space=15))
    
    print("\nRenaissance and Duelling Swords:")
    df = pd.DataFrame(menu_Duelling, index = range(1, len(menu_Duelling["swordType"]) + 1))
    df = format_cost_column(df)
    print(df.to_string(col_space=15))
    
    print("\nAsian and Eastern Swords:")
    df = pd.DataFrame(menu_Asia, index = range(1, len(menu_Asia["swordType"]) + 1))
    df = format_cost_column(df)
    print(df.to_string(col_space=15))
    
    print("\nFantasy and Decorative Swords:")
    df = pd.DataFrame(menu_Decor, index = range(1, len(menu_Decor["swordType"]) + 1))
    df = format_cost_column(df)
    print(df.to_string(col_space=15))
    
    print("\nPractical and Training Swords:")
    df = pd.DataFrame(menu_Practical, index = range(1, len(menu_Practical["swordType"]) + 1))
    df = format_cost_column(df)
    print(df.to_string(col_space=15))
    
weapon_list()