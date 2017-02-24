from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (3, 8):
    for j in range (i):
        trick = (i-3)%len(colors)
        color(colors(trick))
        fd(100)
        lt(360/i)
        
