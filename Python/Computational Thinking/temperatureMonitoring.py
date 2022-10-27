#Imports
import math

#Variables
temps = [50.35, 51.75, 53.08, 57.00, 59.25, 61.19, 65.10, 64.22, 58.35, 55.98, 53.50, 50.95, 50.00]

#Processing
roundedTemps = [math.floor(temp) for temp in temps]

#Outputs
print(roundedTemps)
print("Minimum temperature:", min(roundedTemps))
print("Maximum temperature:", max(roundedTemps))
print("Average temperature:", round((sum(roundedTemps))/len(roundedTemps), 2))