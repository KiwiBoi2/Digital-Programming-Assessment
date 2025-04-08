#import pandas as library
import pandas as pd

def weapon_list():
    #create menu dictionary
    menu_dict = {}
    #format prices as currency
    pd.set_option('display.float_format','{:.2f}'.format)
    #add category numbers to dictionary
    menu_dict ["categoryID"] = [1,2,3,4,5]
    #add weapon categories to dictionary 
    menu_dict ["categoryName"] = ["Medieval European","Renaissance and Duelling","Asian and Eastern","Fantasy and Decorative","Practical and Training"]
    #create new dictionaries for weapon categories
    menu_Europe = {}
    menu_Duelling = {}
    menu_Asia = {}
    menu_Decor = {}
    menu_Practical = {}
    #add entries to Europe dictionary
    menu_Europe ["swordTypes"] = ["Arming Sword","Longsword","Bastard Sword","Claymore","Falchion"]
    menu_Europe ["cost"] = [1000, 1500, 1500, 2000, 1000]
    #add entries to Duelling dictionary
    menu_Duelling ["swordTypes"] = ["Rapier","Sabre","Estoc"]
    menu_Duelling ["cost"] = [1500, 1200, 1500]
    #add entries to Asia dictionary
    menu_Asia = ["swordTypes"] = ["Katana", "Wakizashi", "Dao", "Jian",]
    menu_Asia = ["cost"] = [15000, 7000, 1500, 1000]
    #add entries to Decor dictionary
    menu_Decor = ["swordTypes"] = ["Replicas", "Custom Blades"]
    menu_Decor = ["cost"] = [500, 1500]
    #add entries to Practical dictionary
    menu_Practical = ["swordTypes"] = ["Training Blades", "Feder Blades", "Wooden Blades"]
    menu_Practical = ["cost"] = [700, 1000, 200]
    
    print(weapon_list)
    
weapon_list()