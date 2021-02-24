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

for i in range(4):
    t.fd(90)
    t.lt(360/4)

t.penup()
t.goto(-50,130)
t.pendown()

t.circle(50)


