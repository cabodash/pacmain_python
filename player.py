# player class

import pygame
from Global import * 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.x = 288
        self.y = player_y
        self.imageSource = pygame.image.load(
            'images/player.png').convert_alpha()
        self.image = self.imageSource
        self.lives = 3
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.direction = 2
        self.walk = False
        self.walk_regist = False
        self.walk_count = 0
        self.walk_audio = False

        # sounds
        self.waka_waka = pygame.mixer.Sound("sounds/wakawaka.swf.mp3")
        self.eat_cherry = pygame.mixer.Sound("sounds/pacman-eating-cherry.mp3")
        self.eat_ghost = pygame.mixer.Sound("sounds/pacman-eating-ghost.mp3")
        self.eat_live = pygame.mixer.Sound("sounds/pacman-extra-live.mp3")
        self.dies = pygame.mixer.Sound("sounds/pacman-dies.mp3")

        # timer-dead variables
        self.died_timer = False
        self.died_timer_count = 0

    # movement for pacman
    def move(self, distance, key):
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.x += distance
            self.direction = 2
            self.walk = True
            if self.died_timer:
                self.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 360)

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.x -= distance
            self.direction = 1
            self.walk = True
            if self.died_timer:
                self.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 180)

        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.y -= distance
            self.direction = 0
            self.walk = True
            if self.died_timer:
                self.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 90)

        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.y += distance
            self.direction = 3
            self.walk = True
            if self.died_timer:
                self.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 270)

        else:
            self.walk = False

    
    # draw pacman
    def draw(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    # waka waka for pacman when eats a dot
    def waka(self):

        if self.walk_audio == True:
            self.walk_count += 1
            if self.walk_count > (self.waka_waka.get_length()*60):
                self.walk_count = 0
                self.walk_audio = False
        if self.walk and not self.walk_regist:
            self.walk_regist = True
            if not self.walk_audio:
                self.walk_audio = True
                self.waka_waka.play()

        if self.walk and self.walk_regist:
            if not self.walk_audio:
                self.walk_audio = True
                self.waka_waka.play()

        if not self.walk and self.walk_regist:
            self.walk_regist = False

    def animation_dead(self):
        
        self.x = 303 - 15
        self.y = player_y

