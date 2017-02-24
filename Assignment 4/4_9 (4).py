import turtle

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("blue")
rua.pensize(3)


def square(r):
    for i in range(4):
        r.forward(100)
        r.left(90)

def pretty(r, n, e):
    for i in range (n):
        square(rua)
        r.lt(e)
        
print(pretty(rua,20,18))
