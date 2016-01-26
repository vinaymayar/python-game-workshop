import pygame, sys
import random

# initialize pygame
pygame.init()

# set constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 360
HEIGHT = 720
NUMBER_OF_LANES = 2

# create screen and clock for the game.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# load necessary images
CAR_IMG = pygame.image.load("images/car.png").convert()

CAR_WIDTH = CAR_IMG.get_rect().width
CAR_HEIGHT = CAR_IMG.get_rect().height

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity = 0.1):
        pygame.sprite.Sprite.__init__(self)
        self.image = CAR_IMG
        self.rect = CAR_IMG.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity

    def move_horizontally(self, delta_x):
        new_x = self.rect.x + delta_x
        if new_x <= WIDTH and new_x >= 0:
            self.rect.x = new_x
        print(self.rect.x)

    def get_y(self):
        return self.rect.y

    def get_x(self):
        return self.rect.x

    def key_pressed(self, key):
        if key == pygame.K_RIGHT:
            self.move_horizontally(WIDTH / NUMBER_OF_LANES)
        elif key == pygame.K_LEFT:
            self.move_horizontally(- WIDTH / NUMBER_OF_LANES)

    def update(self, timestep):
        self.rect.y += self.velocity * timestep


my_car = Car((WIDTH / NUMBER_OF_LANES - CAR_WIDTH) / 2, HEIGHT - 200, 0)
enemy_cars = []

enemy_cars_group = pygame.sprite.Group()
my_car_group = pygame.sprite.GroupSingle(my_car)


def add_new_enemy(enemy):
    enemy_cars.append(enemy)
    enemy_cars_group.add(enemy)

def generate_enemy_car():
    lane = random.randint(0, NUMBER_OF_LANES - 1)
    pos_x = lane * WIDTH / NUMBER_OF_LANES + (WIDTH / NUMBER_OF_LANES - CAR_WIDTH) / 2
    new_enemy = Car(pos_x, 0)
    # if there are no enemies in the board
    if not enemy_cars:
        add_new_enemy(new_enemy)
        return

    last_car = enemy_cars[-1]
    # threshold so user can still pass.
    if last_car.get_y() > 2.5 * CAR_HEIGHT:
        # randomly adds enemy
        if random.randint(0, 1) > 0:
            add_new_enemy(new_enemy)

def print_text(text):
    font = pygame.font.SysFont('ComicSans', 20)
    rendered_text = font.render(text, True, BLACK, WHITE)
    screen.blit(rendered_text, (200, 200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            my_car.key_pressed(event.key)

    # update clock
    clock.tick(30)

    # clear screen and redraw cars
    screen.fill(WHITE)
    enemy_cars_group.update(clock.get_time())
    enemy_cars_group.draw(screen)
    my_car_group.update(clock.get_time())
    my_car_group.draw(screen)
    pygame.display.flip()

    # check if hit another car
    if pygame.sprite.spritecollideany(my_car, enemy_cars_group):
        print_text("You lose.")
        break;


    # possibly generate a new enemy car
    generate_enemy_car()




