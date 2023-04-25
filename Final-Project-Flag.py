#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle 
import time 

screen = turtle.getscreen()

screen.bgcolor("white")
screen.title("American Flag")

t = turtle.Turtle()
t.speed(100)
t.penup()

t.shape("turtle")

flag_height = 250
flag_width = 475

start_x = -237
start_y = 125

stripe_height = flag_height/13
stripe_width = flag_width

star_size = 10

def draw_rectangle(x, y, height, width, color):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()
    
def draw_star(x,y,color,length):
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range (0,5):
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup
    
def draw_stripes():
    x = start_x
    y = start_y
    
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_rectangle(x,y, stripe_height, stripe_width, color)
            y = y - stripe_height
            
            
    draw_rectangle(x, y, stripe_height, stripe_width, 'red')
    y = y - stripe_height
    
def draw_square():
    square_height = (7/13) * flag_height 
    square_width = (0.76) * flag_height
    draw_rectangle(start_x, start_y, square_height, square_width, 'navy')
    
def draw_six_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 112 
    
    for row in range(0,5):
        x = -222
        for star in range (0,6):
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars 
        y = y - gap_between_lines
        
def draw_five_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6 
    y = 100 
    for row in range(0,4):
        x = -206
        
        for star in range (0,5):
            draw_star(x,y, 'white', star_size)
            x = x + gap_between_stars
        y = y-gap_between_lines
        
time.sleep(5)
draw_stripes()
draw_square()
draw_six_stars_rows()
draw_five_stars_rows()
t.hideturtle()
screen.mainloop()


# In[ ]:




