from turtle import *


def red_on():
    penup()
    goto(0,100)
    pendown()
    color('red')
    pensize(2)
    begin_fill()
    circle(35)
    end_fill()


def red_off():
    penup()
    goto(0,100)
    pendown()
    color('red')
    pensize(2)
    circle(35)

def yellow_on():
    penup()
    goto(0,0)
    pendown()
    color('yellow')
    pensize(2)
    begin_fill()
    circle(35)
    end_fill()

def yellow_off():
    penup()
    goto(0,0)
    pendown()
    color('yellow')
    pensize(2)
    circle(35)

def green_on():
    penup()
    goto(0,-100)
    pendown()
    color('green')
    pensize(2)
    begin_fill()
    circle(35)
    end_fill()

def green_off():
    penup()
    goto(0,-100)
    pendown()
    color('green')
    pensize(2)
    circle(35)

speed(0)
answer = input('Какой горит цвет красный/жёлтый/зелёный?')
if answer == 'красный':
    red_on()
    yellow_off()
    green_off()
elif answer == 'жёлтый':
    red_off()
    yellow_on()
    green_off()
elif answer == 'зелёный':
    red_off()
    yellow_off()
    green_on()

exitonclick()
hideturtle()
