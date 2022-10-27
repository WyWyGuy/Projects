#Get information
base_price = float(input("Please enter the base price of the car you would like to buy: $"))
sales_tax = base_price*0.0825
registration = 192.00
dealer_prep = 200.00
delivery = 720.00

#Calculations
total_cost = base_price + sales_tax + registration + dealer_prep + delivery
monthly_cost = total_cost * (0.009 + (0.009/(1.009 ** 36 - 1.0)))

#Outputs
print("Base price of the car: $" + str(round(base_price, 2)))
print("Registration cost: $" + str(int(registration)))
print("Dealer preparation fee: $" + str(int(dealer_prep)))
print("Delivery fee: $" + str(int(delivery)))
print("Sales tax: $" + str(round(sales_tax, 2)))
print("")
print("Your total cost is: $" + str(round(total_cost, 2)))
print("Over a 3-year period, your monthly payment will be $" + str(int(round(monthly_cost, 2))))