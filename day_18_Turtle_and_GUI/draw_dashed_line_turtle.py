from turtle import Turtle, Screen

trtl = Turtle()

for _ in range(15):
    trtl.forward(10)
    trtl.penup()
    trtl.forward(10)
    trtl.pendown()

screen = Screen()
screen.exitonclick()