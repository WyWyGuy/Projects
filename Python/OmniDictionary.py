#Imports
from time import sleep
from sys import exit



#Alphabet options
Binary = ['0', '1']
Trinary = ['0', '1', '2']
Base10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
Music = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
English = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Alphanumeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Keyboard = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '\\', '|', '/', '_', '+', '-', '=', ';', ':', '"', "'", '`', '~', ' ']



#Initial variables
indexes = [0]
thingtoprint = ""
position = 0
numbersPrinted = 0
alphabets = [Binary, Trinary, Base10, Hexadecimal, Music, English, Alphanumeric, Keyboard]
alphabetList = ["Binary", "Trinary", "Base10", "Hexadecimal", "Music", "English", "Alphanumeric", "Keyboard"]



#User input
print(str(alphabetList).replace("[", "").replace("]", "").replace("'", ""))     #Print options without extra list syntax
alphabet = input("What alphabet would you like to use? ")
speed = input("How many seconds between prints? ")
stopCount = input("How many numbers would you like to print? (Blank for infinity) ")
stopItem = input("What number would you like to end on?(Blank for infinity) ")
stopLength = input("How many digits would you like to stop at? (Blank for infinity) ")



#Adjusting start variables
if alphabet in alphabetList:     #If typed out correctly
    alphabet = alphabets[alphabetList.index(alphabet)]
elif alphabet.isdigit():     #If given a number as a position
    alphabet = alphabets[int(alphabet) - 1]
else:     #Otherwise default to Base 10
    alphabet = Base10

if speed == "":
    speed = 0.1
else:
    speed = float(speed)

if alphabet[0] == "0":
        includeFirst = False
else:
    includeFirst = True



#Core loop
print("")
while True:
    sleep(speed)     #Delay for readability
    if stopLength != "":     #If the user added a limit for characters
        if len(indexes) > int(stopLength):     #If we reach the limit for characters
            exit()     #End the program
    if stopCount != "":     #If the user added a limit for prints
        if numbersPrinted >= int(stopCount):     #If we reach the limit for prints
            exit()     #End the program
    for i in range(0, len(indexes)):     #For each item in indexes
        thingtoprint = thingtoprint + str(alphabet[indexes[i]])     #Creating the thing to print
    thingtoprint = thingtoprint[::-1]     #Reversing the string because it is created backwards
    print(thingtoprint)     #Print the current number
    numbersPrinted += 1     #Update the counter
    if stopItem != "":     #If the user added a last item
        if thingtoprint == str(stopItem):     #If we printed the last user-requested item
            exit()     #End the program
    thingtoprint = ""     #Reset printer
    position = 0     #Reset position
    
    for i in indexes:     #Run through the numbers
        if i < len(alphabet) - 1:     #Is the number less than max?
            (indexes[position]) += 1     #Increment it
            break     #And start over
        if i >= len(alphabet) - 1:     #Is the number max?
            indexes[position] = 0     #Reset it
        try:     #Check
            indexes[(position + 1)]     #if the next number exists
        except:     #If no number exists...
            indexes.append(0)     #Create it
            if includeFirst == True:     #Check if alphabet includes first character
                break     #If so, skip the repetition
        position += 1     #Update position for next number