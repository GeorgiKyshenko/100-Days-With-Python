from turtle import Turtle, Screen
import random

trtl = Turtle()
colors = ["hot pink", "dodger blue", "spring green", "dark turquoise", "dark slate blue", "light coral", "dark green"]


def draw_shapes_right(sides):
    angle = 360 / sides
    for _ in range(sides):
        trtl.forward(100)
        trtl.right(angle)


def draw_shapes_left(sides):
    angle = 360 / sides
    for _ in range(sides):
        trtl.forward(100)
        trtl.left(angle)


for side in range(3, 11):
    trtl.color(random.choice(colors))
    draw_shapes_right(side)
    draw_shapes_left(side)

screen = Screen()
screen.exitonclick()
