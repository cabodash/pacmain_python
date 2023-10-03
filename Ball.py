import pygame
# dots and power up's class
class Balls(pygame.sprite.Sprite):
    def __init__(self, x, y,size):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.imageSource = pygame.image.load('images/ball.png').convert_alpha()
        self.image = pygame.transform.scale(self.imageSource, (size, size))

        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.top = x
        self.rect.left = y

