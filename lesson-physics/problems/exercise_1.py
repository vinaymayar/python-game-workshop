import pygame, sys
from pygame.locals import *
pygame.init()

#Setting up screen and clock.##
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Motion 1')
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

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

##Main game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #If right arrow is pressed, velocity is set to .2 to the right.
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            vel = [.2, 0]
        #***Insert conditionals for remaining three arrow keys.***
        #If left arrow is pressed, set velocity to .2 to the left.

            
        #If up pressed, set velocity to .2 up.
            
            
        #If down presses, set velocity to .2 down.

    #Tracking time through loop.
    clock.tick()    
    #Updating ball position based on velocity.
    ballx += vel[0] * clock.get_time()
    bally += vel[1] * clock.get_time()
    #Establishing boundaries; ball reverses if it hits edge.
    #ballx and bally indexed to top left corner of rect.
    if bally + ball_height > screen_height or bally < 0:
        vel[1] = -vel[1]
    if ballx + ball_width > screen_width or ballx < 0:
        vel[0] = -vel[0]
    #Updating screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()

#***When you complete this exercise, continue to Exercise 2.***
