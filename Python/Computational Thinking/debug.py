from gpiozero import TrafficLights, Button, LED
from time import sleep

north = TrafficLights(4, 3, 2)
east = TrafficLights(14, 15, 18)
south = TrafficLights(16, 20, 21)
west = TrafficLights(13, 19, 26)
crosswalk = Button(24)
crosslight = LED(12)
errorbutton = Button(11)
offbutton = Button(23)

north.green.on()
sleep(1)
north.amber.on()
sleep(1)
north.red.on()
sleep(1)
north.off()

east.green.on()
sleep(1)
east.amber.on()
sleep(1)
east.red.on()
sleep(1)
east.off()

south.green.on()
sleep(1)
south.amber.on()
sleep(1)
south.red.on()
sleep(1)
south.off()

west.green.on()
sleep(1)
west.amber.on()
sleep(1)
west.red.on()
sleep(1)
west.off()

crosslight.on()
sleep(1)
crosslight.off()

print("Press the crosswalk button")
crosswalk.wait_for_press()

print("Press the error button")
errorbutton.wait_for_press()

print("Press the off button")
offbutton.wait_for_press()