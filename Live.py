import pygame

# Map live's class
class Live(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #img
        self.imageSource = pygame.image.load('images/live.png').convert_alpha()
        self.image = pygame.transform.scale(self.imageSource, (26, 24))

        #hitbox
        self.rect = self.image.get_rect()
        self.rect.top = x
        self.rect.left = y

        #timer
        self.timer = False
        self.timer_count = 0
#lives = Lives(300,300)
#live_list.add(lives)



