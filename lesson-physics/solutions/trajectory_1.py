import pygame, sys
from pygame.locals import *

pygame.init()

#Setting up screen.
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Trajectory 1')
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
    #Updating velocity due to gravity.
    vel[1] += g * clock.get_time()
    #Updating position due to velocity.
    ballx += vel[0] * clock.get_time()
    bally += vel[1] * clock.get_time()
    #Ball bounces when it hits the screen boundary.
    if bally + ball_height > screen_height:
        vel[1] = -vel[1]
    if ballx <0 or ballx + ball_width > screen_width:
        vel[0] = -vel[0]
    #Updating screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()
