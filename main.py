import turtle

import colorgram
from turtle import Screen,Turtle
import random

# rgb_color=[]
# color=colorgram.extract("spot.jpg",30)
# for i in color:
#     red=i.rgb.r
#     green = i.rgb.g
#     blue = i.rgb.b
#     new_color=(red,green,blue)
#     rgb_color.append(new_color)
# print(rgb_color)

color_list=[(229, 141, 53), (241, 234, 88), (25, 42, 69), (172, 151, 48), (125, 166, 184), (236, 116, 130), (62, 110, 93), (175, 94, 51), (16, 83, 159), (206, 68, 150), (227, 235, 6), (130, 196, 84), (240, 94, 83), (38, 43, 42), (169, 68, 135), (24, 63, 118), (42, 42, 42), (118, 198, 53), (232, 165, 182), (227, 174, 168), (172, 212, 152), (173, 198, 205), (111, 124, 150), (181, 191, 208)]

sam=Turtle()
sam.shape("classic")
sam.penup()
sam.hideturtle()

turtle.colormode(255)

sam.setheading(225)
sam.forward(250)
sam.setheading(0)

no_of_dots=100
for spot_count in range(1,no_of_dots+1):
    sam.dot(20,random.choice(color_list))
    sam.forward(50)
    if spot_count %10 == 0:
        sam.setheading(90)
        sam.forward(50)
        sam.setheading(180)
        sam.forward(500)
        sam.setheading(0)
#10 x 10
#size=20
#space=50



screen=Screen()
screen.exitonclick()