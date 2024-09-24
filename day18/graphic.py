from turtle import Turtle, Screen

tinny_the_turtle = Turtle()
tinny_the_turtle.shape("turtle")
# tinny_the_turtle.color("red")
# tinny_the_turtle.forward(78)
lst = ["Blue", "red", "green", "yellow", "Blue", "red", "green", "yellow", "Blue", "red", "green", "yellow", "Blue",
       "red", "green", "yellow", "Blue", "red", "green", "yellow", "Blue", "red", "green", "yellow", "Blue", "red",
       "green", "yellow", "Blue", "red", "green", "yellow",
       "Blue", "red", "green", "yellow", "Blue", "red", "green", "yellow",
       ]
n = len(lst)
for i in range(n):
    tinny_the_turtle.color(lst[i])
    tinny_the_turtle.forward(i * 10)
    tinny_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
