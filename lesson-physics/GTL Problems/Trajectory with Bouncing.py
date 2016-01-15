import pygame, sys
from pygame.locals import *

pygame.init()

##Setting up screen.##
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Trajectory with Bouncing')
WHITE = (255, 255, 255)

##Loading ball image and converting to rect object.##
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()
##Extracting height and width from rect properties.##
ball_width = ballrect.width
ball_height = ballrect.height
##Setting starting position and velocity.##
ballx = 10
bally = 80
vel = [.2, -0.1]
##Setting acceleration due to gravity.##
g = .0005

##Main game loop.##
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
    ##Increment velocity by g.##
            
    ##Update position due to velocity.##
    
    ##If side is struck, reverse x-velocity.##
    ##If top/bottom struck, reverse y-velocity.##
    
    ##Updating screen.##
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()
