#Create Lists
my_count = [1, 2, 3, 4, 5, 6]
fruits = ['apples', 'oranges', 'banana', 'lemons']
change = [1, 'cents', 2, 'half euro', 3, 'euros']
elements = []

#Loops
for number in my_count:
    print("This is count %d" % number)
    
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
    
for i in change:
    print("I got %r" % i)
    
for i in range(0, 6):
    print("Adding %d to the list." % i)
    elements.append(i)

#Print Final
print("Element was: %d" % i)