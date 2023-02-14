#Thomas Farrell
#CS175L - Gil Eckert
#Stop Sign

import turtle

window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_x = -5
text_y = -10


turtle.setup(window_width, window_height)


turtle.penup()
turtle.goto(50,100)
turtle.pendown()
turtle.pensize(3)
turtle.color("black",'red')
turtle.begin_fill()


for x in range(num_sides):
    turtle.right(angle)
    turtle.forward(length)

turtle.end_fill()


turtle.penup()
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(5)
turtle.left(180)
turtle.pendown()
turtle.color('white')
length = 90
turtle.pensize(5)
for x in range(num_sides):
    turtle.right(angle)
    turtle.forward(length)


RADIUS = 100
FONTSIZE = int(RADIUS / 2)
FONT = ("Arial", FONTSIZE, "bold")
turtle.penup()
turtle.goto(-90,-60)
turtle.pendown()
turtle.write("STOP", align= "left", font=FONT)


