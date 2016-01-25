import pygame
import sys
from pygame.locals import *

# Define constants
width = 480
height = 480
white = (255, 255, 255)
black = (0, 0, 0)

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((width, height))

# Create a clock
clock = pygame.time.Clock()

# Load images
x_img = pygame.image.load('x.png').convert()
o_img = pygame.image.load('o.png').convert()

# Draw background
pygame.draw.rect(screen, white, (0, 0, width, height))
pygame.draw.line(screen, black, (width/3, 0), (width/3, height), 5)
pygame.draw.line(screen, black, (2*width/3, 0), (2*width/3, height), 5)
pygame.draw.line(screen, black, (0, height/3), (width, height/3), 5)
pygame.draw.line(screen, black, (0, 2*height/3), (width, 2*height/3), 5)

# Update screen with background
pygame.display.flip()

turn = 1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def change_player():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

def add_image_to_screen(v_idx, h_idx):
    global turn
    if turn == 1:
        img = x_img
    else:
        img = o_img

    position = (h_idx * width / 3 + 5, v_idx * height / 3 + 5)
    
    screen.blit(img, position)

def check_for_victory():
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] != 0:
            return row[0]
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    return 0

def check_for_draw():
    for row in board:
        for square in row:
            if square == 0:
                return False
    return True

def print_text(text):
    font = pygame.font.SysFont('Arial', 20)
    rendered_text = font.render(text, True, black, white)
    screen.blit(rendered_text, (200, 200))

def print_winner(winner):
    print_text("Player {} won!".format(winner))

def print_draw():
    print_text("Draw!")

def click(x, y):
    print(y)
    print(x)
    vertical_idx = y / (height/3)
    horizontal_idx = x / (width/3)
    print(vertical_idx)
    print(horizontal_idx)
    
    if board[vertical_idx][horizontal_idx] > 0:
        return
    
    board[vertical_idx][horizontal_idx] = turn
    
    add_image_to_screen(vertical_idx, horizontal_idx)
    
    winner = check_for_victory()
    if winner > 0:
        print_winner(winner)
        return

    draw = check_for_draw()
    if draw:
        print_draw()
        return
    
    change_player()
    return

while True:
    # Process events that happened since the last iteration
    for event in pygame.event.get():
        # Process quitting
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Process a mouse click
        elif event.type == MOUSEBUTTONUP:
            x, y = event.pos
            click(x, y)
            pygame.display.flip()
            clock.tick(30)
