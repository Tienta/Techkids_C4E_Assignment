import turtle

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("hotpink")
rua.pensize(3)


def square(t):
    for i in range(4):
        t.forward(20)
        t.left(90)
for i in range (5):
    square(rua)
    rua.penup()
    rua.fd(40)
    rua.pendown()
    
    
