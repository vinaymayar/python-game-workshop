import pygame, sys
from pygame.locals import *

pygame.init()

#Setting up screen.
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Acceleration in Gravity')
WHITE = (255, 255, 255)

#Loading ball image and converting to rect object.
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()
#Extracting height and width from rect properties.
ball_width = ballrect.width
ball_height = ballrect.height
#Setting starting position and velocity.
ballx = 10
bally = 80
vel = [.2, -0.1]
#Setting acceleration due to gravity.
g = .0005

#Main game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #**Implement conditionals such that pressing an arrow key increments velocity in that direction by .05.**
        #If right arrow key is pressed, increase velocity in the x-direction by .1.

        #If left arrow key is pressed, decrease velocity in x-direction by .1.

        #If down arrow key is pressed, increase velocity in y-direction by .1.

        #If up arrow key is pressed, decrease velocity in y-direction by .1.

    #Updating y-velocity due to gravity.
    vel[1] += g
    #Updating position due to velocity.
    ballx += vel[0]
    bally += vel[1]
    #If side is struck, x-velocity direction is reversed and magnitude is multiplied by .9.
    #If top/bottom struck, y-velocity direction is reversed and magnitude is multiplied by .9.
    if bally + ball_height > screen_height or bally < 0:
        vel[1] = -.9*vel[1]
    if ballx + ball_width > screen_width or ballx < 0:
        vel[0] = -.9*vel[0]
    #Updating screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()

#**When you've completed this exercise, try Collision in 1D.**
