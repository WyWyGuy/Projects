from gpiozero import LED
from time import sleep

r = LED(18)
g = LED(23)
b = LED(24)

def red():
    r.off()
    g.on()
    b.on()

def green():
    r.on()
    g.off()
    b.on()

def blue():
    r.on()
    g.on()
    b.off()

def yellow():
    r.off()
    g.off()
    b.on()

def cyan():
    r.on()
    g.off()
    b.off()

def purple():
    r.off()
    g.on()
    b.off()

def white():
    r.off()
    g.off()
    b.off()

def off():
    r.on()
    g.on()
    b.on()

red()
sleep(1)
green()
sleep(1)
blue()
sleep(1)
yellow()
sleep(1)
cyan()
sleep(1)
purple()
sleep(1)
white()
sleep(1)
off()