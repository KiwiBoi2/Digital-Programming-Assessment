#Ask for pickup or delivery
print("Would you like to pick up your item from the store or have it be delivered? \nEnter 1 for Pickup \nEnter 2 for Delivery")

#Constants for Pickup and Delivery
PICKUP_CONSTANT = 1
DELIVERY_CONSTANT = 2

def choice_checker():
    #Checking choice
    while True:
        try:
            choice = int(input("Please enter 1 or 2\n"))
            if choice >= PICKUP_CONSTANT and  choice <= DELIVERY_CONSTANT:
                #If pickup selected
                if choice == 1:
                    print("Pickup Selected")
                    choice = 1
                    break
                #If delivery selected
                elif choice == 2:
                    print("Delivery Selected")
                    choice = 2
                    break
                else:
                    choice = int(input("Please enter 1 or 2\n"))
        except ValueError:
            print("That is not a valid number. Please enter 1 or 2")
            print("Continue")
            
choice_checker()