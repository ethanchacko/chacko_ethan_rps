# This file was created by:Ethan Chacko

# Importing the turtle module so that we can use turtle
import turtle
from turtle import *
# Importing the os mdule so that we can access our files and directories
import os

print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint
from time import sleep
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')



# Setting the width and height for the window, and for the rock paper and scissor objects
WIDTH, HEIGHT = 1000, 500

rock_w, rock_h = 256, 280

paper_w, paper_h = 220, 220

scissors_w, scissors_h = 200, 200

player_choice = ""

cpu_choice = ""

# Setting up the Screen class using the turtle module, and giving it a color
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="white")


# canvas object
cv = screen.getcanvas()
# Making sure that the window cannot be resized
cv._rootwindow.resizable(False, False)

# Setting up the images of rock paper and scissors, for both user and cpu using Turtle

rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
# rock_instance.hideturtle()

cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()
# cpu_rock_instance.hideturtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
# paper_instance.hideturtle()

cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()
# cpu_paper_instance.hideturtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
# scissors_instance.hideturtle()

cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()
# cpu_scissors_instance.hideturtle()

''' 
Defining each item in our game by making a function for each on of them, 
To help the computer show each item properly, 
and we can call these functions later when needed
    
'''

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)

text = turtle.Turtle()

# Making a text that we can use to write in our window

def write_text(message, x, y):
    text.hideturtle()
    text.color('blue')
    text.penup()
    text.clear()
    text.setpos(x,y)
    text.write(message, False, "center", ("Arial", 25, "normal"))
  
        
# This function helps the computer select a random option between rock paper and scissors
def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, to see if is being clicked on or not
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# This is to tell the computer where to keep the options rock paper and scissors when the game starts
show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)

# function that passes through wn onlick
def mouse_pos(x, y):
    print(cpu_select())
    cpu_picked = cpu_select()
    ''' This tells the computer what to do in each possible scenario of rock paper scissors '''
    if collide(x,y,rock_instance,rock_w,rock_h):
        write_text("You picked Rock!", 0, 150 )
        if cpu_picked == "rock":
            write_text("The computer chose Rock too!", 0, 150)
            show_scissors(0,-600)
            show_paper(0,-600)
            cpu_show_rock(300,0)
            show_rock(-300,0)
            write_text("It's a Tie!", 0, 150 )
        if cpu_picked == "paper":
            write_text("The computer chose Paper!", 0, 150)
            show_scissors(0,-600)
            show_paper(0,-600)
            cpu_show_paper(300,0)
            show_rock(-300,0)
            write_text("You Lose!", 0, 150 )
        if cpu_picked == "scissors":
            write_text("The computer chose Scissors!", 0, 150)
            show_scissors(0,-600)
            show_paper(0,-600)
            cpu_show_scissors(300,0)
            show_rock(-300,0)
            write_text("You Win!", 0, 150 )
    elif collide(x,y,paper_instance,paper_w,paper_h):
        write_text("You picked Paper!", 0, 150 )
        if cpu_picked == "rock":
            write_text("The computer chose Rock!", 0, 150)
            show_scissors(0,-600)
            show_rock(0,-600)
            cpu_show_rock(300,0)
            show_paper(-300,0)
            write_text("You Won!", 0, 150 )
        if cpu_picked == "paper":
            write_text("The computer chose Paper too!", 0, 150)
            show_scissors(0,-600)
            show_rock(0,-600)
            cpu_show_paper(300,0)
            show_paper(-300,0)
            write_text("It's a Tie!", 0, 150 )
        if cpu_picked == "scissors":
            write_text("The computer chose Scissors!", 0, 150)
            show_scissors(0,-600)
            show_rock(0,-600)
            cpu_show_scissors(300,0)
            show_paper(-300,0)
            write_text("You Lose!", 0, 150 )
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        write_text("You picked Scissors!", 0, 150 )
        if cpu_picked == "rock":
            write_text("The computer chose Rock!", 0, 150)
            show_rock(0,-600)
            show_paper(0,-600)
            cpu_show_rock(300,0)
            show_scissors(-300,0)
            write_text("You Lose!", 0, 150 )
        if cpu_picked == "paper":
            write_text("The computer chose Paper too!", 0, 150)
            show_rock(0,-600)
            show_paper(0,-600)
            cpu_show_paper(300,0)
            show_scissors(-300,0)
            write_text("You Won!", 0, 150 )
        if cpu_picked == "scissors":
            write_text("The computer chose Scissors!", 0, 150)
            show_rock(0,-600)
            show_paper(0,-600)
            cpu_show_scissors(300,0)
            show_scissors(-300,0)
            write_text("It's a Tie!", 0, 150 )
    # If the user did not click anything, we tell the computer to let them know that they need to choose something
    else:
        write_text("You clicked on NOTHING!", 0, 150 )

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last  
write_text("Let's Play Rock, Paper, Scissors!", 0, 150 )


screen.mainloop()

