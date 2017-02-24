import turtle

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("hotpink")
rua.pensize(3)


def draw_poly(t, n, sz) :
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

print(draw_poly(rua, 8, 50)) 
