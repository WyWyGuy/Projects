from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

buzzer = Buzzer(15)
button = Button(21)

wait = 0.5

while True:
    buzzer.on()
    sleep(wait)
    buzzer.off()
    sleep(wait)
    wait = wait - 0.01
    if button.is_pressed:
        break