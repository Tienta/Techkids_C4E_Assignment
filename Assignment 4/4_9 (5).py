import turtle

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("blue")
rua.pensize(2)

def drawSpiral(r, angle):
    length = 1
    for i in range(80):
        r.forward(length)
        r.right(angle)
        length = length + 2

rua.penup()
rua.backward(110)
rua.pendown()

# hinh 1 
drawSpiral(rua, 90)

# hinh 2
rua.penup()
rua.home()
rua.forward(90)
rua.pendown()

drawSpiral(rua, 89)
