##
## Arkenoid/Breakout Version 1
##
## You can use this as a starting point for your
## Assignment 8 extension to the game

from random import randint, random
from time import sleep


from SimpleGraphics import *
setAutoUpdate(False)

## define the graphics window
setWindowTitle("BreakOut 2016!")
w,h = 600,425
bottom = 400
resize(w,h)
background('midnightblue')
setFont("Arial", "16", "bold")

gap = 3

## paddle class
class Paddle:
	""" A Paddle represents a paddle in the game """
	length,width,help_width,height = w/7,w/7,2*w/7,h/20
	help = False
	x,y = 10, bottom-height-gap
	dx,dy = 1,0
	c = 'green'

# ball class
class Ball: 
	""" A Ball represents a ball in the game """
	size  = 20
	x, y  = w/2,bottom/3
	dx,dy = random()*1-.2, random()*1+0.5
	c = 'yellow'
	count = 3
class Block:
        """ A Blocks represent blocks in the game """
        sizew = 40
        sizeh = 20
        x,y = 0, 0
        colour = 'red'
        newc = 'black'
        value = 1
        hits = 3
        broken = True
	
def drawThings(paddle, ball, box):
	# paddle
	setColor(paddle.c)
	rect(paddle.x, paddle.y, paddle.length, paddle.height)
	# ball
	setColor(ball.c)
	ellipse(ball.x-ball.size//2, ball.y-ball.size//2, ball.size, ball.size)
        # blocks
	for i in box:
		setColor(i.colour)
		rect(i.x, i.y, i.sizew, i.sizeh)

def  drawScore(ball, score):
	global w, h
	## update score
	setColor('black')
	text(20,h-12, "Balls left " + str(ball.count), 'w')
	text(w-textWidth("Score = XXXXXXXXXX"), h-12, "Score = " + str(score), 'w')
	
	
def updateThings(paddle, ball, box, keys):
	global w, h, bottom

	for i in box:		
		if broken(ball, i) == Block.broken:
			i.colour = i.newc
		else:
			i.colour = i.noc
                                                
	
	
	# check if help key is pressed
	if 'h' in keys and paddle.help == False:
		paddle.help = True
		paddle.length = paddle.help_width
		paddle.x = paddle.x - (paddle.help_width-paddle.width)/2
	elif 'h' not in keys and paddle.help == True:
		paddle.help = False
		paddle.length = paddle.width
		paddle.x = paddle.x + (paddle.help_width-paddle.width)/2
		
	# move left and right	
	if "Left" in keys and "Right" not in keys:
		paddle.x = max(paddle.x - paddle.dx,gap)
	elif "Right" in keys and "Left" not in keys:
		paddle.x = min(paddle.x + paddle.dx, w-paddle.length-gap)
		
	if paddle.x <= 0 :
		paddle.x = 0
	elif paddle.x >= w - paddle.width:
		paddle.x = w - paddle.width
	
	## update ball
	ball.x += ball.dx
	ball.y += ball.dy
	if ball.x <= ball.size/2:
		ball.x = ball.size/2
		ball.dx = -ball.dx
	elif ball.x >= w-ball.size/2:
		ball.x = w-ball.size/2
		ball.dx = -ball.dx
	
	if ball.y <= 0:
		ball.y = 0
		ball.dy = -ball.dy

	elif (ball.y + ball.size/2 >= paddle.y and paddle.x <= ball.x + ball.size/2 <= paddle.x + paddle.length):
		ball.y = paddle.y - ball.size
		ball.dy = -ball.dy
	elif ball.y + ball.size/2 >= h:
		ball.count -= 1
		ball.x, ball.y  = w/2,h/3
		ball.dx,ball.dy = random()*1-.2, random()*1+0.5

	## allow for user to change speed of ball
	## this is just to help test the game (we can slow the up/down motion up)
	if "Down" in keys:
		ball.dy = 0.95*ball.dy
	elif "Up" in keys:
		ball.dy = 1.05*ball.dy
	
def broken(ball, Block):
	if ball.x > Block.x and ball.x < Block.x + Block.sizew:
				if ball.y > Block.y and ball.y < Block.y + Block.sizeh:
					return Block.broken
	else:
		return False       	
def main():
	# create a paddle and a ball for the game
	paddle = Paddle()
	ball = Ball()
	box =[]

	score = 0

	for row in range(5):
		for col in range(12):
			bl = Block()
			bl.x = (col * 50) + 5
			bl.y = (row * 25)
			
			if row == 0: 
				bl.noc = 'purple'
				bl.value = 10
				bl.hits = 3
	
			elif row == 1:
				bl.noc = 'lightblue'
				bl.value = 8
				bl.hits = 2

				
			elif row == 2:
				bl.noc = 'green'
				bl.value = 6
				bl.hits = 2

				
			elif row == 3:
				bl.noc = 'orange'
				bl.value = 4
				bl.hits = 1
				
			elif row == 4:
				bl.noc = 'pink'
				bl.value = 2
				bl.hits = 1
			box.append(bl)



	## main loop of the game	
	while not closed():
		clear()

		# check where we are in the game
		if ball.count == 0:
			# game is over
			text(w/2,h/2,"Game Over")
		
		else:
			# draw the elements in the game
			drawThings(paddle, ball, box)
	
			# get the keys currently held
			keys = getHeldKeys()
	
			# update ball and paddle, checking for collisions
			updateThings(paddle, ball, box, keys)
	
			#sleep(0.01)

		
		# always draw text box at bottom of screen
		setColor('azure1')
		rect(0,bottom,w,h-bottom)
		
		#draw blocks
##		for i in range (0, len(box)+1):
##			rect(box[i-1].x,box[i-1].y,box[i-1].sizew,box[i-1].sizeh)
##			setColor(bl.noc)
		drawScore(ball, score)
		

                                                 

		
if __name__ == "__main__":
	main()
