import pygame, sys
from pygame.locals import *

pygame.init()

##Setting up screen.##
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Motion 2')
WHITE = (255, 255, 255)

##Loading ball image and converting to rect object.##
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()
##Extracting height and width from rect properties.##
ball_height = ballrect.height
ball_width = ballrect.width
##Setting starting position and velocity.##
ballx = 100
bally = 80
vel = [0, 0]

##Main game loop.##
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ##Arrow keys cause acceleration of ball.##
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            vel[0] += .05
        elif event.type == KEYDOWN and event.key == K_LEFT:
            vel[0] -= .05
        elif event.type == KEYDOWN and event.key == K_UP:
            vel[1] -= .05
        elif event.type == KEYDOWN and event.key == K_DOWN:
            vel[1] += .05
    ##Updating ball position based on velocity.##
    ballx += vel[0]
    bally += vel[1]
    ##Establishing boundaries.##
    ##ballx and bally indexed to top left corner of rect.##
    if bally + ball_height > screen_height or bally < 0:
        vel[1] = -vel[1]
    if ballx + ball_width > screen_width or ballx < 0:
        vel[0] = -vel[0]
    ##Updating screen.##
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()
