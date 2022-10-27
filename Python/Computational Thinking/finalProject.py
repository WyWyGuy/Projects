#Imports
from gpiozero import TrafficLights, Button, LED
from time import sleep
from sys import exit

#Variables
north = TrafficLights(4, 3, 2)
east = TrafficLights(14, 15, 18)
south = TrafficLights(16, 20, 21)
west = TrafficLights(13, 19, 26)
crosswalk = Button(24)
crosslight = LED(12)
errorbutton = Button(11)
offbutton = Button(23)

error = False
yellowtime = 2
waitbeforegreen = 2
greentime = 7
crossingtime = 10
initialpause = 3
walknexttime = False

#Functions
def sleepy(wait):
    global walknexttime
    global error
    for i in range(wait*100):
        sleep(0.01)
        if crosswalk.is_pressed:
            walknexttime = True
        if errorbutton.is_pressed:
            error = True
            errorlights()
        if offbutton.is_pressed:
            shutdown()

def allOff():
    north.off()
    east.off()
    south.off()
    west.off()
    
def allRed():
    north.red.on()
    east.red.on()
    south.red.on()
    west.red.on()
    
def errorlights():
    global error
    allOff()
    allRed()
    sleep(0.75)
    allOff()
    sleep(0.75)
    while error == True:
        allRed()
        for i in range(75):
            sleep(0.01)
            if errorbutton.is_pressed:
                error = False
                allRed()
                sleep(1)
                mainLoop()
        allOff()
        for i in range(75):
            sleep(0.01)
            if errorbutton.is_pressed:
                error = False
                allRed()
                sleep(1)
                mainLoop()

def shutdown():
    allOff()
    exit()
        
def checkwalk():
    global walknexttime
    if walknexttime == True:
        waitbeforegreen = 0
        sleepy(1)
        crosslight.on()
        sleepy(crossingtime)
        crosslight.off()
        walknexttime = False

def yroad():
    allOff()
    east.red.on()
    west.red.on()
    north.green.on()
    south.green.on()
    sleepy(greentime)
    
def xroad():
    allOff()
    north.red.on()
    south.red.on()
    east.green.on()
    west.green.on()
    sleepy(greentime)
    
def ytrans():
    global waitbeforegreen
    east.green.off()
    east.amber.on()
    west.green.off()
    west.amber.on()
    sleepy(yellowtime)
    east.amber.off()
    east.red.on()
    west.amber.off()
    west.red.on()
    checkwalk()
    sleepy(waitbeforegreen)
    waitbeforegreen = 2
    
def xtrans():
    global waitbeforegreen
    north.green.off()
    north.amber.on()
    south.green.off()
    south.amber.on()
    sleepy(yellowtime)
    north.amber.off()
    north.red.on()
    south.amber.off()
    south.red.on()
    checkwalk()
    sleepy(waitbeforegreen)
    waitbeforegreen = 2

def mainLoop():
    while True:
        yroad()
        xtrans()
        xroad()
        ytrans()

#Initializiation
allOff()
allRed()
sleep(initialpause)

#Core loop
mainLoop()