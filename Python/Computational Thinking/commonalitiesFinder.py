#Assign Variables
samAnswers = ['MTNDEW', 'ACTION', 'GAMING', 'DORITOS', 'HISTORY', 'GRAVEYARD', 'DISGUSTED', 'SILVER', 0, 'Sam']
wyattAnswers = ['APPLEJUICE', 'COMEDY', 'GAMING', 'CHOCOLATE', 'PROGRAMMING', 'GRAVEYARD', 'UNDECIDED', 'YELLOW', 0, 'Wyatt']
rileyAnswers = ['DRPEPPER', 'ACTION', 'DRIVING', 'DONUTS', 'HISTORY', 'GRAVEYARD', 'WEIRD', 'BLUE', 0, 'Riley']
kylaAnswers = ['CHOCOLATEMILK', 'HORROR', 'DRAWING', 'DONUTS', 'SCIENCE', 'FOREST', 'COOL', 'YELLOW', 0, 'Kyla']

people = [samAnswers, wyattAnswers, rileyAnswers, kylaAnswers]

questions = ('What is your favorite drink? ', 'What is your favorite genre of movie? ', 'What is your favorite hobby? ', 'What is your favorite junk food? ', 'What is your favorite school subject? ', 'Where do you want to be buried or have your ashes scattered? ', 'How do you feel about ostriches? ', 'What is your favorite color? ')

index = 0

#Introduce User
print('Answer these 8 questions to find out who you have the most in common with')
print('Your answers should be one word, with no spaces or special characters')
print('Type your answer and press enter to submit it')

#For loop running through questions
for question in questions:
    answer = input(question).upper()     #Capitalize everything for better matches
    for person in people:
        if (answer == person[index]):
            person[8] = person[8] + 1     #Update score for matching answer
    index = index + 1

#Determine winner
scores = [samAnswers[8], wyattAnswers[8], rileyAnswers[8], kylaAnswers[8]]
names = ['Sam', 'Wyatt', 'Riley', 'Kyla']

winnerScore = max(scores)
winnerName = names[scores.index(winnerScore)]

#Print output
if sum(scores) == 0:
    print("You have nothing in common with Sam, Wyatt, Riley, or Kyla")
else:
    print("You have the most in common with " + winnerName + ", with a total score of " + str(winnerScore) + " things in common!")