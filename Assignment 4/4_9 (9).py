import turtle

rua = turtle.Turtle()
rua.speed(-1)
rua.pensize(3)

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.rt(144)

print(drawFivePointStar(rua))
