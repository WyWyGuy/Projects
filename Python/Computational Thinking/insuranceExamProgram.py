#Get information
space = "------------------------"
name = input("Please enter your name: ")
months = int(input("How many months would you like a quote for? "))
if (months > 12 or months < 3):
    print("Please enter between 3 and 12 months")
    months = int(input("How many months would you like a quote for? "))
    #This will allow a different number the second time. "Repeat until 12>months>3"?
umbrella = input("Would you like to purchase a 1-time umbrella policy? ")
carInsurance = 124.99
houseInsurance = 174.99
boatInsurance = 29.99
umbrellaCost = 79.99

#Calculate
oneMonth = carInsurance + houseInsurance + boatInsurance
totalMonths = oneMonth * int(months)
if (umbrella == 'yes' or umbrella == 'Yes' or umbrella == "y" or umbrella == "Y"):
    totalMonths = totalMonths + umbrellaCost
discount = totalMonths * 0.1
insuranceTotal = totalMonths - discount

#Output
print("")
print("")
print("")
print("")
print("")
print("Hello", name + "!")
print("")
print(space)
print("")
print("Car insurance: $" + str(round(carInsurance, 2)))
print("House insurance: $" + str(houseInsurance))
print("Boat insurance: $" + str(boatInsurance))
if (umbrella == 'yes' or umbrella == 'Yes' or umbrella == "y" or umbrella == "Y"):
    print("Umbrella policy: $" + str(umbrellaCost))
print("")
print(space)
print("")
print("Your insurance cost for", str(months), "months is:")
print("")
print("Subtotal: $" + str(round(totalMonths, 2)))
print("Discount: 10%")
print("Total: $" + str(round(insuranceTotal, 2)))