# import colorgram
#
# colors = colorgram.extract('OIP (1).jpeg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module
import random

tin = turtle_module.Turtle()
tin.speed("fastest")
tin.hideturtle()
tin.penup()
turtle_module.colormode(255)
color_list = [(228, 226, 224), (228, 223, 226), (220, 227, 222), (223, 226, 231), (194, 173, 123), (155, 104, 57),
              (183, 157, 53), (124, 36, 24), (7, 52, 78), (53, 30, 26), (105, 68, 85), (24, 118, 166), (8, 62, 43),
              (116, 160, 174), (84, 136, 64), (72, 34, 41), (125, 37, 42), (66, 152, 132), (181, 98, 81),
              (208, 201, 152), (178, 202, 188), (142, 172, 157), (172, 149, 155), (214, 182, 175), (20, 77, 96),
              (145, 117, 125), (94, 140, 157), (170, 198, 208), (203, 187, 191), (35, 75, 61)]

tin.setheading(225)
tin.forward(250)
tin.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tin.dot(20, random.choice(color_list))
    tin.forward(50)
    if dot_count % 10 == 0:
        tin.setheading(90)
        tin.forward(50)
        tin.setheading(180)
        tin.forward(500)
        tin.setheading(0)

screen = turtle_module.Screen()

screen.exitonclick()
