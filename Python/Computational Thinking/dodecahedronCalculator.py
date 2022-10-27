#Get the length of the edge
print("Type the edge of the dodecahedron")
edge = float(input())

#Calculate the volume
firstPart = 7.66311896062
edgeCubed = edge ** 3
volume = firstPart * edgeCubed

#Output answer
print(volume)