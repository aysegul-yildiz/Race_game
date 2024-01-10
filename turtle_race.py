from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500,400)
user_guess = screen.textinput(title="Bet on a turtle!", prompt="Enter the color of the turtle you think is gonna win: ")
is_race_on = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -90, -30, 30, 90, 150 ]
all_racers = []

for index in range(0,6):
    my_turtle= Turtle("turtle")
    my_turtle.penup()
    my_turtle.color(colors[index])
    my_turtle.goto(x=-230, y=y_position[index])
    all_racers.append(my_turtle)

while is_race_on:
    for turtle in all_racers:
        if turtle.xcor() >= 230:
            winning_turtle = turtle.fillcolor()
            is_race_on = False
            if user_guess == winning_turtle:
                print(f"You have won! The winning turtle is the {winning_turtle} one.")
            else:
                print(f"You have lost! The winning turtle is the {winning_turtle} one.")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()