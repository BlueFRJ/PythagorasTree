import turtle	
import math
import random	

def fractal(aturt, depth, maxdepth):
		if depth > maxdepth:
				return		 
		length = 180*((math.sqrt(2)/2)**depth)	
		anotherturt = aturt.clone()	
		aturt.forward(length)	
		aturt.left(45)	
		fractal(aturt, depth+1, maxdepth)	
		anotherturt.right(90)	
		anotherturt.forward(length)	
		anotherturt.left(90)	
		anotherturt.forward(length)	
		if depth != maxdepth:
			color = random.choice(["#FF0000","#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8F00FF"])
			aturt.color(color)
			anotherturt.color(color)
			turt3 = anotherturt.clone()	
			turt3.left(45)	
			turt3.forward(180*((math.sqrt(2)/2)**(1+depth)))	
			turt3.right(90)	
			fractal(turt3, depth+1, maxdepth) 
			aturt.color(color)
			anotherturt.color(color)

def draw_fractal():
	window = turtle.Screen()	
	turt = turtle.Turtle()	
	turt.hideturtle()
	turt.penup() 
	turt.color("#614126")	
	turt.goto(-75, -225)	
	turt.pendown()	
	turt.speed(10)	
	turt.left(90)	
	fractal(turt, 1, 12)	
	ts = turt.getscreen()
	ts.getcanvas().postscript(file="holi.eps")
	window.exitonclick()	

color = "green"	
draw_fractal()	
