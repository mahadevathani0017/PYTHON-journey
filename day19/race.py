from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="make your bet:", prompt="which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'green', 'blue', 'indigo', 'violet']
for i in range(len(colors)):
    tin = Turtle(shape='turtle')
    tin.penup()
    tin.goto(x=-238, y=-100 + i * 40)
    tin.color(colors[i])

screen.exitonclick()
