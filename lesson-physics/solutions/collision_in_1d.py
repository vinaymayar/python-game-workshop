import pygame, sys
from pygame.locals import *

pygame.init()

#Setting up screen.
screen_width = 1000
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collision in 1D')
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

#Loading ball images.
ball = pygame.image.load('ball.gif')
ball2 = pygame.image.load('ball.gif')
#Converting to rect objects, extracting height and width from rect properties.
ballrect = ball.get_rect()
ball_width = ballrect.width
ball_height = ballrect.height
ball2rect = ball.get_rect()
ball2_width = ballrect.width
ball2_height = ballrect.height
#Setting starting positions and velocity.
ballx = 10
bally = 50
ball2x = 840
ball2y = 50
vel = [.2, 0]
vel2 = [-.3, 0]

#Main game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Tracking time.
    clock.tick()
    #Updating positions based on velocity.
    ballx += vel[0] * clock.get_time()
    bally += vel[1] * clock.get_time()
    ball2x += vel2[0] * clock.get_time()
    ball2y += vel2[1] * clock.get_time()
    #If sides are struck or balls collide,, x-velocities are reversed.
    if ballx + ball_width > screen_width or ballx < 0 or ballx + ball_width > ball2x:
        vel[0] = -vel[0]
    if ball2x + ball2_width > screen_width or ball2x < 0 or ball2x < ballx + ball_width:
        vel2[0] = -vel2[0]
    #Updating screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    screen.blit(ball2, (ball2x, ball2y))
    pygame.display.flip()
