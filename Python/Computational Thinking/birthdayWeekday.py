#Imports
import datetime

#Assign variables
myBirthday = datetime.date(2003, 12, 11)

#Prints
print(myBirthday.strftime("Your birthday is: %Y/%m/%d"))
print(myBirthday.strftime("You were born on a %A"))