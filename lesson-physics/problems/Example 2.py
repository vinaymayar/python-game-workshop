#Make sure you include these lines at the top of all your pygame files.
import pygame, sys
from pygame.locals import *
pygame.init()

#Setting up screen.
#These lines set how many pixels wide and tall the screen will be.
screen_width = 1500
screen_height = 250
screen = pygame.display.set_mode((screen_width, screen_height))
#This line sets the caption at the top of the screen.
pygame.display.set_caption('Example 2')
#This line creates a variable to store the RBG values for white.
WHITE = (255, 255, 255)

#These lines load the ball image and convert it to a rect object.
#Rect class stores info such as height, width, center, etc. of object.
#For more info, see pygame rect info page.
#https://www.pygame.org/docs/ref/rect.html
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()
#These lines extract height and width from rect properties.
ball_height = ballrect.height
ball_width = ballrect.width
#These lines set the starting position for the ball and starting velocity.
ballx = 100
bally = 80
vel = [0, 0]

#Main game loop.
#Write all game code in this while loop.
while True: 
    for event in pygame.event.get():
        #This conditional allows you to quit the game and exit the loop.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #For each loop, the horizontal velocity is increased to the right.
    #This makes the ball accelerate.
    vel[0] += .0001   
    #These lines update ball position based on velocity.
    ballx += vel[0]
    bally += vel[1]
    #These lines update the screen on every iteration of the loop.
    #First line fills in white, second updates ball position in the screen, third updates display.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()

#When you understand this code, try to complete Exercise 1.
