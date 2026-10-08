from turtle import *
speed(20)
width(5)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(70)

#door
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200,200)
pendown()
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window left
color("black")
left(30)
forward(50)

left(90)
forward(50)

right(90)
forward(70)

right(90)
forward(50)

right(90)
forward(35)

right(90)
forward(50)

left(90)
forward(35)

left(90)
forward(25)

left(90)
forward(70)

#winfow right
penup()
goto(200,200)  
pendown()

forward(50)

right(90)
forward(50)

left(90)
forward(70)

left(90)
forward(50)

left(90)
forward(35)

left(90)
forward(50)

right(180)
forward(25)
left(90)
forward(35)
right(180)
forward(70)

exitonclick()