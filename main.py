# from colorgram import extract

# colors_extracted = extract("hirst_color.jpg", 20)
# colors = []
# for color in colors_extracted:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors.append(new_color)

colors = [
    (219, 173, 5),
    (4, 135, 195),
    (238, 127, 48),
    (228, 116, 155),
    (9, 149, 98),
    (128, 160, 202),
    (30, 19, 65),
    (240, 162, 190),
    (229, 83, 111),
    (234, 201, 52),
    (200, 29, 49),
    (6, 172, 120),
    (69, 13, 65),
    (196, 18, 39),
    (83, 30, 21),
    (183, 74, 45),
]

from turtle import Turtle, Screen
from random import choice


# def turn(angle) : # Faz zigzag
#     color = choice(colors)
#     jimmy.color(color)
#     jimmy.dot(20)
#     jimmy.setheading(90)
#     jimmy.forward(50)
#     if angle == 0 :
#         jimmy.setheading(180)
#     else :
#         jimmy.setheading(0)


def move(y) :
    jimmy.goto(-200, y)
    for _ in range(10) :
        color = choice(colors)
        jimmy.color(color)
        jimmy.dot(20)
        jimmy.forward(50)
    # turn(jimmy.heading())


jimmy = Turtle()
jimmy.speed(0)
jimmy.penup()
jimmy.hideturtle()
jimmy.screen.colormode(255)
y = -200
jimmy.goto(-200, y)

for _ in range(10) :
    move(y)
    y += 50

screen = Screen()
screen.exitonclick()