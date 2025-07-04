from turtle import Turtle, Screen
import random

is_race_on = False
#Set up screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?, Enter a color: ")


# def move_forwards():
#     tim.forward(10)
    


# def move_backwards():
#     tim.backward(10)
    

# def move_clockwise():
#     tim.left(10)
    

# def move_counter_clockwise():
#     tim.right(10)
    
    

# screen.listen()
# screen.onkey(key="w", fun=move_forwards) 
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=screen.resetscreen)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_value = -80
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle",)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_value)
    y_value += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won!, The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose!, The {winning_color} turtle is the winner!")
                
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        

screen.exitonclick()