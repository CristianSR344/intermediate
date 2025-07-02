from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

tim = Turtle()

tim.shape("turtle")
tim.color("blue")

# square
# for _ in range (10):
#     tim.forward(100)
#     tim.right(90)

# dotted line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


#Random Walk
# flag = True
# speed = 0
# pensize = 1

# while flag:
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(50)
#     tim.speed(speed)
#     speed +=1
#     tim.pensize(pensize)
#     pensize +=0.1

tim.speed(0)
#Spirograph
def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
