def confirm_order():
    question = "Do you want to confirm the order? (yes/no): "
    while True:
        confirmation = input(question).strip().lower()
        if confirmation in ['yes', 'y']:
            print("Order confirmed.")
            return True
        elif confirmation in ['no', 'n']:
            print("Order not confirmed.")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def order_again():
    question = "Do you want to place another order? (yes/no): "
    while True:
        again = input(question).strip().lower()
        if again in ['yes', 'y']:
            print("Returning to the main menu...")
            return True
        elif again in ['no', 'n']:
            print("Thank you for your order. Goodbye!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
          
confirm_order()
order_again()
