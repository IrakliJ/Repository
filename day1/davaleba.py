from turtle import *
import math
begin_fill()
color("purple")
for i in range(4) :
    left(90)
    forward(200)
end_fill()
back(75)
color("yellow")
begin_fill()
for i in range(4) :
    left(90)
    if i % 2 == 0 :
        forward(120)
    else :
        forward(46)
end_fill()    
color("purple")
left(90)
forward(200)
right(90)
forward(75)
begin_fill()
color("red")
for i in range(2) :
    left(120)
    forward(200)
end_fill()
color("purple")
left(30)
forward(30)
left(90)
forward(60)
color("brown")
begin_fill()
for i in range(2) :
    if i % 2 == 1 :
        color("purple")
        forward(110)
        color("brown")
    for j in range(4) :
        right(90)
        forward(30)
end_fill()
        
