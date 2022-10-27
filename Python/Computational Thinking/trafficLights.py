from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

time = 5

lights.off()

while True:
    if button.is_pressed:
        time = 10
    else:
        time = 5
    lights.off()
    lights.green.on()
    sleep(5)
    if button.is_pressed and time == 5:
        time = 10
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    if time == 10:
        buzzer.on()
        sleep(0.05)
        buzzer.off()
    sleep(time)