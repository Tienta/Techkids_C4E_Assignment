from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (5):
    color(colors[i])
    begin_fill()
    for j in range (2):
        fd(50)
        lt(90)
        fd(100)
        lt(90)
    end_fill()
    fd(50)
