from turtle import*

#1 step make a box for the outline for the house
shape("turtle")
#speed(30)
width(7)
color("red")
forward(200)
left(90)

forward(200)#lenght of the box
left(90)

forward(200)
left(90)

forward(200)
left(90)
#2 step make a door
forward(70)
color("lime")
begin_fill()
left(90)
forward(100) #hight of the door
right(90)
forward(70) #width of the door
right(90)
forward(100)
end_fill()
#3 step make a roof
penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#4 step windows]
right(-30)
color("red")
forward(30)
left(90)
color("brown")
begin_fill()
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()
penup()
goto(200,200)
pendown()
right(-90)
color("red")
forward(30)
right(90)
color("brown")
begin_fill()
forward(70)
left(90)
forward(50)
left(90)
forward(70)
end_fill()







exitonclick()
