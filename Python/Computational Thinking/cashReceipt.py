#Get Items
storeName = "ALBERTSONS"
theBreak = "------------------------------------------"
item1 = "Marionberry Yogurt"
item2 = "Raspberry Yogurt"
item3 = "Peach Yogurt"
item4 = "Blackberry Yogurt"
item5 = "Huckleberry Yogurt"
price1 = 0.39
price2 = 0.39
price3 = 0.39
price4 = 0.39
price5 = 0.39

#Calculations
subTotal = price1 + price2 + price3 + price4 + price5
total = subTotal * 1.06

#Print
print(storeName)
print(theBreak)
print(item1 + "..........$" + str(round(price1, 2)))
print(item2 + "..........$" + str(round(price2, 2)))
print(item3 + "..........$" + str(round(price3, 2)))
print(item4 + "..........$" + str(round(price4, 2)))
print(item5 + "..........$" + str(round(price5, 2)))
print(theBreak)
print("Subtotal: $" + str(round(subTotal, 2)))
print("Tax: $" + str(round(total - subTotal, 2)))
print("Total: $" + str(round(total, 2)))
print(theBreak)
print("Thank you for visiting " + storeName + "!")