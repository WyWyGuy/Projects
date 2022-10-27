#Imports
import turtle
import random

#Get User Input
userFlakeCount = input("How many snowflakes would you like? (Leave blank for a random number) ")
if userFlakeCount == "":
    flakeCount = random.randint(30, 1000)
else:
    flakeCount = int(userFlakeCount)
userSpeed = input("How fast would you like your snowflakes to appear? (1-100) ")
if userSpeed == "":
    speed = 1;
else:
    speed = float(int(userSpeed)/10)

#Initialize
turtle.bgcolor('#000022')

#Set up basic flake
flake = turtle.Turtle()
flake.up()
flake.shape("circle")
flake.speed(0)
flake.goto(0, 300)
flake.rt(90)

#Custiomize basic flake
flake.shapesize(0.3, 0.3, 0.3)
flake.pen(pencolor="#ffffff", fillcolor="#ffffff", pensize=1, speed=speed)

#Duplicate flake
for i in range (flakeCount):
    ranX = random.uniform(-335, 330)
    ranY = random.uniform(-275, 280)
    flake.goto(ranX, ranY)
    flake.clone()

flake.ht()