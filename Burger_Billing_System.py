# #defining the menu items
# menu = {
#     "Aloo Tikki": 5,
#     "Maharaja": 10,
#     "Mac Special": 15
# }

# #function to display the menu items to user
# def display_menu():
#     print("Welcome to the Burger Shop!")
#     print("Here is our menu:")
#     print("SrNo.  ITEM\t\t PRICE")
#     for index, (item, price) in enumerate(menu.items(), start=1):
#         print(f"{index}.  {item}\t\t {price}$")

# #function to handle user input regarding their order
# def get_order_details():
#     order = {}
#     item_name = input("Please select an item from the menu: ")
    
#     if item_name not in menu:
#         print("Invalid item selected. Please try again.")
#         return None
    
#     quantity = int(input("How many quantity? "))
#     is_student = input("Are you a student? (yes/no): ").strip().lower() == 'yes'
#     delivery = input("Do you want delivery? (yes/no): ").strip().lower() == 'yes'
#     tip = int(input("Do you want to give a tip? (2$, 5$, 10$ or 0$ for no tip): "))
    
#     order['item_name'] = item_name
#     order['quantity'] = quantity
#     order['is_student'] = is_student
#     order['delivery'] = delivery
#     order['tip'] = tip
    
#     return order

# #function to calculate the total bill
# def calculate_bill(order):
#     item_price = menu[order['item_name']]
#     total_price = item_price * order['quantity']
    
#     # Apply student discount if applicable
#     student_discount = 0.2 * total_price if order['is_student'] else 0
    
#     # Calculate delivery charge if applicable
#     delivery_charge = 0.05 * total_price if order['delivery'] else 0
    
#     # Calculate final total
#     final_total = total_price - student_discount + delivery_charge + order['tip']
    
#     return total_price, student_discount, delivery_charge, final_total

# #function to print the final bill
# def print_bill(order, total_price, student_discount, delivery_charge, final_total):
#     print("\n****************** Final Bill ***********************")
#     print(f"sr.  name\t\tprice\tquantity\t\ttotal_price")
#     print(f"1.  {order['item_name']}\t\t\t\t {menu[order['item_name']]}$\t\t\t\t  {order['quantity']}\t\t\t\t\t  {total_price}$")
#     print("-----------------------------------------------------")
#     print(f"\t\t\t\t\t {total_price}$")
#     print(f"Student discount 20%\t\t\t -{student_discount}$")
#     print(f"Delivery charge 5%\t\t\t +{delivery_charge}$")
#     print(f"Tip\t\t\t\t\t+{order['tip']}$")
#     print("-----------------------------------------------------")
#     print(f"Total bill\t\t\t\t {final_total}$")
#     print("Thank you and come again >>>>>>>>>>>>>>>>>>>>>>>>>>\n")

# #main function to run the program
# def main():
#     while True:
#         display_menu()
#         order = get_order_details()
        
#         if order:
#             total_price, student_discount, delivery_charge, final_total = calculate_bill(order)
#             print_bill(order, total_price, student_discount, delivery_charge, final_total)
        
#         another_order = input("Do you want to place another order? (yes/no): ").strip().lower()
#         if another_order != 'yes':
#             break

# if __name__ == "__main__":
#     main()


def display_menu():
    print("*************** Burger Menu ***************")
    print("sr.  name             price")
    print("1.   Aloo Tikki       5$")
    print("2.   Maharaja         10$")
    print("3.   Mac Special      15$")
    print("********************************************")

def calculate_discount(price, is_student):
    if is_student:
        return price * 0.20  # 20% discount
    return 0

def calculate_delivery_charge(price, wants_delivery):
    if wants_delivery:
        return price * 0.05  # 5% delivery charge
    return 0

def get_tip():
    tip_options = [2, 5, 10]
    tip_response = input("Do you want to give a tip? (yes/no): ").strip().lower()
    if tip_response == 'yes':
        while True:
            tip_amount = input("Choose tip amount: 2$, 5$, 10$: ").strip()
            if tip_amount in map(str, tip_options):
                return int(tip_amount)
            else:
                print("Invalid amount. Please choose from 2$, 5$, or 10$")
    return 0

def main():
    while True:
        display_menu()
        orders = []
        
        while True:
            choice = int(input("Select the burger (1-3) or 0 to finish ordering: "))
            if choice == 0:
                break
            if choice in [1, 2, 3]:
                quantity = int(input("How many quantity? "))
                orders.append((choice, quantity))
            else:
                print("Invalid selection. Please try again.")
        
        if not orders:
            print("No items selected. Please start over.\n")
            continue
        
        is_student = input("Are you a student? (yes/no): ").strip().lower() == 'yes'
        wants_delivery = input("Do you want delivery? (yes/no): ").strip().lower() == 'yes'
        
        # Prices based on selection
        prices = {1: 5, 2: 10, 3: 15}
        burger_names = {1: "Aloo Tikki", 2: "Maharaja", 3: "Mac Special"}
        
        total_price = 0
        
        # Calculate total price for all orders
        for choice, quantity in orders:
            total_price += prices[choice] * quantity
        
        discount = calculate_discount(total_price, is_student)
        delivery_charge = calculate_delivery_charge(total_price, wants_delivery)
        tip = get_tip()
        
        final_amount = total_price - discount + delivery_charge + tip
        
        # Print the final bill
        print("\n****************** Final Bill ***********************")
        print(f"sr.\tname\t\tprice\tquantity\ttotal_price")
        
        for choice, quantity in orders:
            price_per_item = prices[choice]
            print(f"{choice}.\t{burger_names[choice]}\t{price_per_item}$\t{quantity}\t\t{price_per_item * quantity}$")
        
        print("------------------------------------------------------")
        print(f"Total Price:                          {total_price}$")
        print(f"Student Discount 20%:                 -{discount}$")
        print(f"Delivery Charge 5%:                   +{delivery_charge}$")
        print(f"Tip:                                   +{tip}$")
        print("------------------------------------------------------")
        print(f"Total Bill:                          {final_amount}$")
        print("Thank you and come again >>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        
        another_order = input("Do you want to place another order? (yes/no): ").strip().lower()
        if another_order != 'yes':
            break

if __name__ == "__main__":
    main()