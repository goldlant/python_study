import turtle
import random

t=turtle.Turtle()


for i in range(30):
    length = random.randrange(1,100)
    t.fd(length)
    angle = random.randrange(-180,180)
    t.right(angle)
