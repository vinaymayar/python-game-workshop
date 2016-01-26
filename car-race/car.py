import pygame

CAR_IMG = pygame.image.load("images/car.png").convert()

class Car(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__()
    self.image = CAR_IMG
    self.x = x
    self.y = y

  def update():
    pass
