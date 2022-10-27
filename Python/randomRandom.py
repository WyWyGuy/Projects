#How random is computer random?
#Make a list of x amount of numbers
#We will shuffle this list using computer randomization
#The program will shuffle the list and then determine how "in order" it ended up
#This means it will look at the first index and see if the number matches
#If so, it will continue down the list
#If not, it will document how far it got
#This, of course, means most randoms won't even have the first number correct
#However, this will repeat until it does end up randomizing the list in the correct order
#The program will then document how many times it ran until that occurred
#Interesting fact I learned while testing this:
#The second to last number in 'documentation' will always be 0
#This is because if the list is ordered correctly except the last 2 numbers,
#It will have the third to last number update by 1
#But if the second to last number is correcet,
#The last number must also be correct
#It is why factorials always end in *1 even though it doesn't change the number
#(1 divided by the length of 'numbers' factorial)*100
#Is the percent chance it will be correct

#Set up
import random
import math
counter = 0
fails = 0
trials = 0
chance = 0
score = 0
numbers = []
documentation = []

#Select a length
length = int(input("Input how many numbers you would like. "))
for i in range(1, length+1):
    numbers.append(i)

#Create a documentation of appropriate length
for i in numbers:
    documentation.append(0)

#Calculate percent chance of success
chance = (1/(math.factorial(len(numbers))))*100
print("Chance of success: " + str(chance) + "%")
print("This is a 1 in " + str(math.factorial(len(numbers))) + " chance")
print("--------------------------------------------")

#Begin trials
while True:
    #Set up the trial
    counter = 0
    random.shuffle(numbers)
    
    #Test how far the shuffle made it
    for i in range(1, len(numbers)+1):
        if i == numbers[i-1]:
            counter += 1
        else:
            break
    
    #Test if it's a new high score
    if counter > score:
        score = counter
        print("Score has reached " + str(score))
    
    #Update the documentation
    if counter != 0:
        documentation[counter-1] += 1
    
    #If no numbers were accurate
    if counter == 0:
        fails += 1
    
    #Update trial counter
    trials += 1
    
    #Determine if the list was shuffled correctly
    if counter == len(numbers):
        break

#Output
print("--------------------------------------------")
print("Chance of success was: " + str(chance) + "%")
print("This was a 1 in " + str(math.factorial(len(numbers))) + " chance")
print("--------------------------------------------")
print("Counter reached " + str(counter))
print("Total trials: " + str(trials))
print("Total fails: " + str(fails))
print("The 'shuffled' list: " + str(numbers))
print("Documentation: " + str(documentation))