#Imports
import turtle
from time import sleep
import random

#Initialize
turtle.bgcolor('#000000')
flakeCount = random.randint(30, 200)

#Set up basic flake
flake = turtle.Turtle()
flake.up()
flake.shape("circle")
flake.speed(0)
flake.goto(0, 300)
flake.rt(90)

#Custiomize basic flake
flake.shapesize(0.3, 0.3, 0.3)
flake.pen(pencolor="#ffffff", fillcolor="#ffffff", pensize=1, speed=0.2)

#Duplicate flake
def generate():
    ranX = random.randint(-335, 330)
    ranSleep = random.uniform(0, 15)
    
    i = flake.clone()
    i.goto(ranX, 300)
    
    sleep(ranSleep)
    while True:
        i.pen(speed=0.2)
        i.fd(600)
        i.speed(0)
        i.rt(90)
        i.fd(700)
        i.rt(90)
        i.fd(600)
        i.rt(90)
        i.fd(700)
        i.rt(90)