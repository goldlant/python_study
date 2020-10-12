import turtle

t=turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(-200,0)
t.pendown()

for i in range(3):
    t.fd(100)
    t.lt(360/3)

t.penup()
t.goto(0,0)
t.pendown()

for i in range(6):
    t.fd(50)
    t.lt(360/6)

t.penup()
t.goto(-70,130)
t.pendown()

t.circle(50)


