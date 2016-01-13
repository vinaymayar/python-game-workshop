import pygame, sys
from pygame.locals import *

pygame.init()

##Setting up screen.##
screen_width = 1000
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collision in 1D')
WHITE = (255, 255, 255)

##Loading ball images.##
ball = pygame.image.load('ball.gif')
ball2 = pygame.image.load('ball.gif')
##Converting to rect objects, extracting height and width from rect properties.##
ballrect = ball.get_rect()
ball_width = ballrect.width
ball_height = ballrect.height
ball2rect = ball.get_rect()
ball2_width = ballrect.width
ball2_height = ballrect.height
##Setting starting positions and velocity.##
ballx = 10
bally = 50
ball2x = 840
ball2y = 50
vel = [.1, 0]
vel2 = [-.2, 0]

##Main game loop.##
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ##Update positions based on velocity.##

    ##If sides are struck or balls collide, reverse x-velocities.##
    ##Hint: compare edge positions of balls.##
            
    ##Updating screen.##
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    screen.blit(ball2, (ball2x, ball2y))
    pygame.display.flip()
