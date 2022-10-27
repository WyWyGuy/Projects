#Get input
distance = float(input("How many miles would you like to travel? "))

#Determine best travel
if distance < 3:
    travel = "walk"
elif distance >= 3 and distance < 300:
    travel = "drive"
elif distance > 300:
    travel = "fly"
else:
    print("INVALID INPUT")

#Print output
print("You should", travel)