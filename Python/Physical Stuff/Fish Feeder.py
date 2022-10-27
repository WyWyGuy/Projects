#2048 phases per 1 full rotation
#512 full steps per rotation
#A 10-slot container needs 51 repeats then
#Smallest wait time possible is 0.0018 seconds or so
#0.002 seconds is optimal

#Use this in sudo crontab -e at the bottom to start it on reboot
#Also copy the file to the desktop so it isn't running off the USB.
#@reboot python /home/pi/Desktop/Fish\ Feeder.py &

from gpiozero import LED
from time import sleep
from datetime import datetime
time = 0.002

#Plug 5V in and Ground out, and these 4 pins to the 4 phase pins
phase1 = LED(17)
phase2 = LED(27)
phase3 = LED(22)
phase4 = LED(23)

def spin(steps):
    for i in range(0, steps):
        phase1.on()
        sleep(time)
        phase1.off()
        phase2.on()
        sleep(time)
        phase2.off()
        phase3.on()
        sleep(time)
        phase3.off()
        phase4.on()
        sleep(time)
        phase4.off()

def stop():
    phase1.off()
    phase2.off()
    phase3.off()
    phase4.off()

#Initial spin to show boot up
spin(51)

while True:
    now = datetime.now()
    if now.strftime("%H") == "08" and now.strftime("%M") == "00":
        spin(51)
        stop()
        sleep(120)
    sleep(10)