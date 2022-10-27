from gpiozero import TrafficLights
from time import sleep

north = TrafficLights(4, 3, 2)
east = TrafficLights(14, 15, 18)
south = TrafficLights(16, 20, 21)
west = TrafficLights(13, 19, 26)

north.off()
east.off()
south.off()
west.off()