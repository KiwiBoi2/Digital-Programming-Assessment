# Pickup and Delivery constants
PICKUP_CONSTANT = 1
DELIVERY_CONSTANT = 2

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

# Function to ask the user if they would like to pick up their item from the store or have it delivered
def pickup_delivery():
    #This function will ask the user if they would like to pick up their item from the store or have it be delivered
    #Ask for pickup or delivery
    print("Would you like to pick up your item from the store or have it be delivered? \nEnter 1 for Pickup \nEnter 2 for Delivery")
    # Call the choice_checker function to validate the user's choice
    choice_checker()

# Call the pickup_delivery function to start the process
pickup_delivery()
