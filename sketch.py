from turtle import *
import random

screen = Screen()
screen.title('Turtle Sketcher')
screen.bgcolor('grey')

yoko = Turtle()
yoko.color('black')
yoko.pensize(2)
yoko.speed(0)
yoko.shape('circle')

def go_up():
	yoko.setheading(90)
	yoko.forward(10)

def go_down():
	yoko.setheading(270)
	yoko.forward(10)

def go_left():
	yoko.setheading(180)
	yoko.forward(10)

def go_right():
	yoko.setheading(0)
	yoko.forward(10)

def draw_star():
	yoko.color("red")
	for x in range(5):
		yoko.forward(50)
		yoko.left(144)
	yoko.color("black")

def clear_screen(x,y):
	screen.reset()
	yoko.color('black')
	yoko.pensize(2)
	yoko.speed(0)
	yoko.shape('circle')

def penup():
	yoko.penup()

def pendown():
	yoko.pendown()

def drawTriangle():
	for x in range(3):
		yoko.forward(100)
		yoko.left(120)

def color_change():
	yoko.color("purple")

def color_black():
	yoko.color('black')	

def drawCircle():
	yoko.circle(100)

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(draw_star,"z")
screen.onkeypress(penup,"o")
screen.onkeypress(pendown,"p")
screen.onkeypress(drawTriangle,"t")
screen.onkeypress(color_change,'c')
screen.onkeypress(color_black,"b")
screen.onkeypress(drawCircle,'q')

screen.onclick(clear_screen)

screen.listen()

mainloop()