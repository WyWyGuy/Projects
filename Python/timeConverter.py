#Get Hours/Minutes/Seconds
minutes = 0
hours = 0
days = 0
seconds = int(input("Please enter the number of seconds to be converted: "))

#Get Minutes
while seconds >= 60:
    minutes = minutes + 1
    seconds = seconds - 60

#Get Hours
while minutes >= 60:
    hours = hours + 1
    minutes = minutes -60

#Get Days
while hours >= 24:
    days = days + 1
    hours = hours - 24

#Output
print(str(days) + " Days, " + str(hours) + " Hours, " + str(minutes) + " Minutes, and " + str(seconds) + " Seconds.")