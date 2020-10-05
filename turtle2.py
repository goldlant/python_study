import turtle
t=turtle.Turtle()


s=turtle.textinput("","몇각형을 원하시나요? :")
n=int(s)

for i in range(n):
    t.forward(100)
    t.lt(360/n)