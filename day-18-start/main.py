from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("blue")

#square
# for _ in range (10):
#     tim.forward(100)
#     tim.right(90)

#dotted line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = [
    "medium violet red",
    "deep sky blue",
    "lime green",
    "gold",
    "hot pink",
    "turquoise",
    "orchid",
    "coral",
    "dodger blue",
    "salmon",
    "medium sea green",
    "tomato",
    "slate blue",
    "dark orange",
    "plum"
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
    
for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
    
import villains












screen = Screen()
screen.exitonclick()