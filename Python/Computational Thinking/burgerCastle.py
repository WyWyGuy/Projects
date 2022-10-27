#Wyatt Nilsson

#Initialize
validOrders = ("burger", "fries", "salad", "soda", "milkshake")
itemDescriptions = ("Half-pound burger", "Large fries", "Side salad", "Diet root beer", "Chocolate shake")
order = []
finished = False

#Begin information
print("Welcome to Burger Castle")
print("Menu:", validOrders)
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")

#Entering menu orders
while finished == False:
    item = input("Enter Item: ")
#End Order    
    if item == "" or item == "quit":
        finished = True
#Add item        
    elif item in validOrders:
        order.append(item)
#Error statement        
    else:
        print("Sorry, we don't sell", item)

#Printing output
print("")
print("Order complete; you are having:")
for x in order:
    print(itemDescriptions[validOrders.index(x)])
print("Thanks for visiting Burger Castle!")