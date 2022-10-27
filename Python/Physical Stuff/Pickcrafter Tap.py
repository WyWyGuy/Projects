from gpiozero import LED
from time import sleep

tap = LED(17)

while True:
    tap.on()
    print("ON")
    sleep(4)
    tap.off()
    print("OFF")
    sleep(4)