
import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for a in range(0, 360, 3):
    t.pencolor(random_color())
    t.circle(100)
    t.setheading(a)

# for a in range(0, 360, 3):
#     t.pencolor(random_color())
#     t.penup()
#     t.forward(200)
#     t.pendown()
#     t.circle(100)
#     t.penup()
#     t.backward(200)
#     t.setheading(a)


screen = turtle.Screen()

screen.exitonclick()