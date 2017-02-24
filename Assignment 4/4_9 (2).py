import turtle
import math

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("hotpink")
rua.pensize(3)


def square(r,size):
    for i in range(4):
        r.forward(size)
        r.left(90)
        
size = 20
for i in range (5):
    square(rua,size)
    size = size+20
    rua.rt(135)
    rua.penup()
    rua.fd(math.sqrt(800)/2)
    rua.lt(135)
    rua.pendown()
    
