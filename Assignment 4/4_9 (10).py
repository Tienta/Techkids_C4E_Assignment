import turtle

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("hotpink")
rua.pensize(3)


def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

for i in range (5):
    drawFivePointStar(rua)
    rua.penup()
    rua.fd(350)
    rua.rt(144)
    rua.pendown()
