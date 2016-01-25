import pygame, sys
from pygame.locals import *
pygame.init()

#Setting up screen.
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Motion 2')
WHITE = (255, 255, 255)

#Loading ball image and converting to rect object.
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()
#Extracting height and width from rect properties.
ball_height = ballrect.height
ball_width = ballrect.width
#Setting starting position and velocity.
ballx = 100
bally = 80
vel = [0, 0]

#Main game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #**Implement conditionals such that pressing an arrow key increments velocity in that direction by .05.**
        #If right arrow key is pressed, increase velocity in the x-direction by .05.

        #If left arrow key is pressed, decrease velocity in x-direction by .05.

        #If down arrow key is pressed, increase velocity in y-direction by .05.

        #If up arrow key is pressed, decrease velocity in y-direction by .05.
    #Updating ball position based on velocity.
    ballx += vel[0]
    bally += vel[1]
    #**Establish boundaries.**
    #If ball strikes side walls, reverse x-velocity.
    
    #If ball strikes top or bottom, reverse y-velocity.
    
    #Updating screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()

#**Once you've finished, try Trajectory 1.**
