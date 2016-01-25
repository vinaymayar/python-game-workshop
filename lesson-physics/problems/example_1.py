#Make sure you include these lines at the top of all your pygame files.
import pygame, sys
from pygame.locals import *
pygame.init()

#Setting up screen.
#These lines set how many pixels wide and tall the screen will be.
screen_width = 1000
screen_height = 250
screen = pygame.display.set_mode((screen_width, screen_height))
#This line sets the caption at the top of the screen.
pygame.display.set_caption('Example 1')
#This line creates a variable to store the RBG values for white.
WHITE = (255, 255, 255)
#This line initializes the clock.
clock = pygame.time.Clock()

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
        #Include this in all your code.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Pressing any key will cause the ball to move to the right.
        elif event.type == KEYDOWN:
            vel = [.5, 0]
    #This line makes sure the clock tracks the time during this pass through the loop.
    clock.tick()
    #These lines update ball position based on velocity.
    #clock.get_time() finds time between the previous two calls of clock.tick()
    ballx += vel[0] * clock.get_time()
    bally += vel[1] * clock.get_time()
    #These lines establish boundaries.
    #At the sides of the screen, the ball will reverse directions.
    #ballx and bally indexed to top left corner of rect.
    if ballx + ball_width > screen_width or ballx < 0:
        vel[0] = -vel[0]
    #These lines update the screen on every iteration of the loop.
    #First line fills the screen in white, second updates ball position in the screen, third updates display to show the screen.
    screen.fill(WHITE)
    screen.blit(ball, (ballx, bally))
    pygame.display.flip()
