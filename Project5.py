#Author: Alexandra Hunter
#Assignment: Project #5
#Completed (or last revision):  11/19/2018



class ItemToPurchase: #for items

    #constructor
    def __init__(this, name_item = "none", price_item = 0, quantity_item = 0, description_item = "none"):
        this.name_item = name_item
        this.price_item = price_item
        this.quantity_item = quantity_item
        this.description_item = description_item
 
    #printing iem
    def print_item_cost(this):
        string = ("{} {} @ ${} = ${}".format(this.name_item, this.quantity_item, this.price_item, (this.quantity_item * this.price_item)))
        cost = (this.quantity_item * this.price_item)
        return string, cost

    #print description
    def print_item_description(this):
        string = ("{}: {}".format(this.item_name, this.item_description))
        print(string, end='\n')
        return string

class ShoppingCart:

    #constuctor
    def __init__(this, customer_name = "none", current_date = "January 1, 2016"):
        this.customer_name = customer_name
        this.current_date = current_date
        this.cart_items = []

    #adding item
    def add_item(this, item):
        print("\nADD ITEM TO CART", end="\n")
        item_name = str(input("Enter the item name: \n"))
        item_description = str(input("Enter the item description: \n"))
        item_price = int(input("Enter the item price: \n"))
        item_quantity = int(input("Enter the item quantity: \n"))
        this.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    #removing item
    def remove_item(this):
        print("\nREMOVE ITEM FROM CART", end="\n")
        index = str(input("Enter name of item to remove: \n"))
        i = 0
        for item in this.cart_items:
            if(item.name_item == index):
                del this.cart_items[i]
                i += 1
                check = True
                break
            else:
                check = False
        if(check == False):
            print("Item not found in cart. Nothing removed.")

    #changing item
    def modify_item(this):
        print("\nCHANGE ITEM QUANTITY", end="\n")
        name = str(input("Enter the item name: \n"))
        for item in this.cart_items:
            if(item.name_item == name):
                quantity = int(input("Enter the new quantity: \n"))
                item.quantity_item = quantity
                check = True
                break
            else:
                check = False
        if(check == False):
            print("Item not found in cart. Nothing modified.")

    #return num of items
    def get_num_items_in_cart(this):
        total = 0
        for item in this.cart_items:
            total = total + item.quantity_item
        return total

    #cost
    def get_cost_of_cart(this):
        total_cost = 0
        cost = 0
        for item in this.cart_items:
            cost = (item.quantity_item * item.price_item)
            total_cost += cost
        return total_cost

    #print
    def print_total():
        total_cost = get_cost_of_cart()
        if(total_cost == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            output_cart()

    #output description
    def print_descriptions(this):
        print("\nOUTPUT ITEMS\' DESCRIPTIONS")
        print("{}\'s Shopping Cart - {}".format(this.customer_name, this.current_date), end="\n")
        print("\nItem Descriptions", end="\n")
        for item in this.cart_items:
            print("{}: {}".format(item.name_item, item.description_item), end="\n")
  
    #print cart
    def output_cart(this):
        newOutput = ShoppingCart()
        print("OUTPUT SHOPPING CART", end="\n")
        print("{}\'s Shopping Cart - {}".format(this.customer_name, this.current_date), end="\n")
        print("\nNumber of Items:", newOutput.get_num_items_in_cart(), end="\n\n")
        total_count = 0
        for item in this.cart_items:
            print("{} {} @ ${} = ${}".format(item.name_item, item.quantity_item, item.price_item, (item.quantity_item * item.price_item)), end="\n")
            total_count += (item.quantity_item * item.price_item)
        print("\nTotal: ${}".format(total_count), end="\n")
#print menu
def print_menu(ShoppingCart):
    cust_Input = newInput
    string = ""
    menu = ("\nMENU\n"
    "a - add item to cart\n"
    "r - remove item from cart\n"
    "c - change item quantity\n"
    "i - output items' description\n"
    "o - output shopping cart\n"
    "q - quit\n")
    userInput = ""
    #for whats being inputed
    while(userInput != "q"):
        string=""
        print(menu, end="\n")
        userInput = input("Choose an option: ")
        if(userInput == "a"):
            cust_Input.add_item(string)
        if(userInput == "r"):
            cust_Input.remove_item()
        if(userInput == "c"):
            cust_Input.modify_item()
        if(userInput == "i"):
            cust_Input.print_descriptions()
        if(userInput == "o"):
            cust_Input.output_cart()

customer_name = str(input("Enter customer\'s name: \n"))
current_date = str(input("Enter today\'s date: \n"))
print("Customer name:", customer_name, end="\n")
print("Today\'s date:", current_date, end="\n")
newInput = ShoppingCart(customer_name, current_date)
print_menu(newInput)
