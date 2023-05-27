from turtle import Turtle, Screen

trtl = Turtle()
trtl.shape("turtle")
trtl.color("blue")
trtl.forward(100)
trtl.right(90)
trtl.forward(100)
trtl.right(90)
trtl.forward(100)
trtl.right(90)
trtl.forward(100)

# or

for _ in range(4):
    trtl.forward(100)
    trtl.left(90)

screen = Screen()
screen.exitonclick()
