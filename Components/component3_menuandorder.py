#import pandas as library
import pandas as pd

def weapon_list():
    
    # Create menu dictionary
    menu_dict = {}
    # Format prices as currency
    pd.set_option('display.float_format', '{:.2f}'.format)
    
    # Add category numbers and names to dictionary
    menu_dict["categoryID"] = [1, 2, 3, 4, 5]
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
    print(pd.DataFrame(menu_dict, index=range(1, len(menu_dict["categoryID"]) + 1)))
    
    # Print Europe Category
    print("\nMedieval European Swords")
    print(pd.DataFrame(menu_Europe, index=range(1, len(menu_Europe["swordType"]) + 1)))
    
    # Print Duelling Category
    print("\nRenaissance and Duelling Swords:")
    print(pd.DataFrame(menu_Duelling, index=range(1, len(menu_Duelling["swordType"]) + 1)))
    
    # Print Asia Category
    print("\nAsian and Eastern Swords")
    print(pd.DataFrame(menu_Asia, index=range(1, len(menu_Asia["swordType"]) + 1)))
    
    # Print Decor Category
    print("\nFantasy and Decorative Swords")
    print(pd.DataFrame(menu_Decor, index=range(1, len(menu_Decor["swordType"]) + 1)))
    
    # Print Practical Category
    print("\nPractical and Training Swords")
    print(pd.DataFrame(menu_Practical, index=range(1, len(menu_Practical["swordType"]) + 1)))
    
weapon_list()