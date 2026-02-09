from turtle import *
speed(5)
width(5)

#box
forward(200); left(90); forward(200); left(90); forward(200); left(90); forward(200); left(90); forward(70)
#door
color("purple");begin_fill();left(90); forward(120); right(90); forward(60); right(90); forward(120); end_fill()
color("black"); penup(); goto(200,200); pendown()
#roof
color("blue"); begin_fill(); right(150); forward(200); left(120); forward(200); end_fill()


exitonclick()