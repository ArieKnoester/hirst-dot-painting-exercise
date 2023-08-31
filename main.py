# colorgram.py 1.2.0 was used to extract colors from the image.jpg file
# https://pypi.org/project/colorgram.py/
# image.jpg came from http://averymccarthy.blogspot.com/2012/02/spot-paintings-by-damien-hirst.html

# import colorgram
#
# colors_from_image = colorgram.extract("image.jpg", 40)
# test_colors = []
# for color in colors_from_image:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     test_colors.append((r, g, b))
#
# print(test_colors)

# From the test_colors list above, I picked 20 that I liked and copy/pasted the values into
# the 'rgb_colors' list of tuples.
# Colors were tested at https://www.w3schools.com/colors/colors_rgb.asp

from turtle import Turtle, Screen
import random


def set_random_color():
    return random.choice(rgb_colors)


def draw_row():
    for i in range(10):
        my_turtle.dot(20, set_random_color())
        my_turtle.penup()
        if i < 9:
            my_turtle.forward(50)


# Initialize
rgb_colors = [
    (58, 106, 148), (225, 200, 109), (223, 139, 64), (196, 145, 171), (142, 179, 204), (139, 81, 105), (210, 91, 68),
    (188, 79, 118), (66, 106, 90), (135, 182, 137), (132, 134, 74), (64, 156, 90), (48, 156, 193), (7, 49, 90),
    (215, 176, 190), (20, 67, 119), (174, 203, 181), (142, 29, 41), (225, 175, 168), (30, 92, 87)]
my_turtle = Turtle()
my_turtle.speed("fastest")
screen = Screen()
screen.colormode(255)

# Set turtle starting position
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.setposition(-220, -220)
my_turtle.pendown()
my_turtle.showturtle()

# Draw the dots
for _ in range(10):
    draw_row()
    if _ < 9:
        my_turtle.setposition(-220, my_turtle.ycor() + 50)

my_turtle.hideturtle()
screen.exitonclick()
