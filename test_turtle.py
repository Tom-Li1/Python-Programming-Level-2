import turtle

# screensize(width, height, "background_color")
turtle.screensize(500, 500, "white") 

# setup(wdith, height, horizontal position, vertical position)
turtle.setup(600,600,100,100)

# speed(<1 - 10>)
turtle.speed(1)

# shape(shape)
turtle.shape("turtle")

# color(pen_color, fill_color)
# fill_color works with begin_fill() and end_fill()
turtle.color("blue", "red")

turtle.begin_fill()
for i in range(10):
    turtle.forward(i * 5)
    turtle.right(90)
turtle.end_fill()

turtle.left(180)
turtle.seth(180)
turtle.circle(50, steps = 6)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

# circle(radius, degree)
# +radius: center at the left side
# -radius: center at the right side
turtle.begin_fill()
turtle.circle(50, 360)
turtle.circle(-50, 360)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

turtle.color("red", "yellow")
turtle.begin_fill()
for i in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()



# end drawing and keep the window
turtle.done()