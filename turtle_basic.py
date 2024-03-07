
"""
 1. import turtle                                   # turtle package
    tim = turtle.Turtle()                           # Turtle class
..............OR.............
    from turtle import *
    tim = Turtle()
    screen = Screen()

2.  import turtle as x
    tim = x.Turtle()
"""


import random
# 1.......
# from turtle import Turtle, Screen                    # Screen class
#
# tom = Turtle()
# print(tom)                    # tom is an object

# tom.shape("turtle")           # appear actual turtle
# tom.color("red")              # change color
# tom.forward(300)              # move 100 places
#
# my_scr = Screen()             # screen appear
# print(my_scr.canvheight)      # change height
# my_scr.exitonclick()          # hold screen



#
# # 2.....turtle move forword when space type......
# from turtle import Turtle,Screen
#
# tim = Turtle()
# screen = Screen()
# def move_forword():
#     tim.forward(20)
#
# screen.listen()                           # collect keyboard key event
# screen.onkey(key="space", fun=move_forword)           # event on type key
# screen.exitonclick()




# #.....Ludo UI......
#
# from turtle import Turtle, Screen
# t = Turtle()
# # s = Screen()
# s = t.getscreen()
#
# t.fillcolor("lightblue")
# t.begin_fill()
# t.penup()
# t.goto(200,200)
# t.pendown()
# t.backward(400)
# t.right(90)
# t.forward(400)
# t.left(90)
# t.forward(400)
# t.left(90)
# t.forward(400)
# t.right(90)
# t.penup()
# t.end_fill()
#
# t.fillcolor("red")
# t.begin_fill()
# t.goto(90,40)
# t.pendown()
# t.circle(60)
# t.penup()
# t.end_fill()
#
# t.fillcolor("green")
# t.begin_fill()
# t.goto(-90,40)
# t.pendown()
# t.circle(60)
# t.penup()
# t.end_fill()
#
# t.fillcolor("yellow")
# t.begin_fill()
# t.goto(-90,-140)
# t.pendown()
# t.circle(60)
# t.penup()
# t.end_fill()
#
# t.fillcolor("blue")
# t.begin_fill()
# t.goto(90,-140)
# t.pendown()
# t.circle(60)
# t.penup()
# t.end_fill()
# t.hideturtle()
# s.exitonclick()






# # 3......Drow Sqare......
# from turtle import *
#
# tinny = Turtle()
# screen = Screen()
#
# tinny.pencolor("blue")
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
#
# tinny.left(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
# tinny.right(90)
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.left(90)
# tinny.forward(150)
# tinny.fillcolor("red")
#
# screen.exitonclick()




# # 4 Dash Line....
# from turtle import Turtle,Screen
#
# tinny = Turtle()
# for _ in range(15):
#     tinny.forward(10)
#     tinny.penup()                 # pen pull-up from the screen
#     tinny.forward(10)
#     tinny.pendown()               # pen in the screen

# screen = Screen()
# screen.exitonclick()





# Random walk.....
import random as ra
from turtle import *
t = Turtle()

colors = ["DarkOrchid", "DeepSkyBlue", "purple", "Red", "Black", "IndianRed", "green2", "cyan2", "blue", "hot pink", "orange", "dark slate gray","Steelblue1","gold2","yellow3"]
directions = [0, 90, 180, 270]
t.pensize(12)                               # thickness of turtle
t.speed("fastest")

for _ in range(300):
    t.color(ra.choice(colors))                  # for colour
    t.forward(40)
    t.setheading(ra.choice(directions))         # for thread

s = Screen()
s.exitonclick()




# #..........make sketch............
# from turtle import Turtle,Screen
# t = Turtle()
# s = Screen()
#
# t.pensize(5)
# def move_for():
#     t.forward(10)
# def move_bac():
#     t.backward(10)
# def turn_lef():
#     new_heading = t.heading()+90
#     t.setheading(new_heading)
# def turn_rig():
#     new_heading = t.heading()-90
#     t.setheading(new_heading)
# def clearFun():
#     t.clear()
#     t.penup()
#     t.home()                            # again center in the screen
#     t.pendown()
# s.listen()
# s.onkey(move_for, "w")
# s.onkey(move_bac, "s")
# s.onkey(turn_lef, "a")
# s.onkey(turn_rig, "d")
# s.onkey(clearFun, "c")
# s.exitonclick()




#
# # turtle race...........
# import  random
# import turtle
# from turtle import *
#
# is_on = False
# s = Screen()                                # screen class object
#
# s.setup(600, 400)              # screen size
# user_bet = s.textinput(title="Make your bet", prompt="which turtle will win the race? Enter: ")        # popup input text box
# # print(user_bet)
# colors = ["purple", "Red", "Black","green", "blue", "yellow", "cyan", "pink"]
# y_position = [-140, -100, -60, -20, 20, 60, 100, 140]
# all_turtle = []
#
# for turtle_ind in range(0,8):
#     new_turtle = Turtle("turtle")                                    # turtle class object
#     new_turtle.color(colors[turtle_ind])                             # different turtle color
#     new_turtle.penup()                                               # up from the screen
#     new_turtle.goto(-285, y_position[turtle_ind])                    # turtle position(x, y)
#     all_turtle.append(new_turtle)
#
# if user_bet:
#     is_on = True
#
# while is_on:
#     for turtle in all_turtle:
#         if turtle.xcor()>280:
#             is_on = False
#             winner = turtle.pencolor()
#             if winner == user_bet:
#                 print(f"You won! {winner} reach 1st")
#             else:
#                 print(f"You lost! {winner} reach 1st")
#         random_dist = random.randint(0, 10)
#         turtle.forward(random_dist)
#
# s.exitonclick()                             # hold screen

