import turtle

bg = turtle.Screen()      
bg.bgcolor("light green")

rua = turtle.Turtle()
rua.speed(-1)
rua.color("blue")
rua.pensize(2)

def draw_poly(r, n, sz):
    for i in range(n):
        r.fd(sz)
        r.lt(360/n)
        
def draw_equitriangle(r,sz):
    draw_poly(rua,3,sz)
    
print(draw_equitriangle(rua, 100))
