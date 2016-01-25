import pygame, sys
from pygame.locals import *

pygame.init()

#Setting up screen.
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Trajectory 2')
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

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
            sys.exit
    #Tracking time.
    clock.tick()
    #**In each loop, increase the y-velocity by g.**
    
    #**Update ball x- and y-positions based on x- and y-velocity.**

    #**Establish boundaries.**
    #In Trajectory 1, the ball bounced back with the same speed.
    #In the real world, the ball loses speed when it strikes something.
    #**This time, if the ball hits an edge, reverse the direction and multiply the speed by .9.**
    
    #Updating screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()

#**When you've completed this exercise, try Acceleration in Velocity.**
