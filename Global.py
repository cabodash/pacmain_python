import pygame
# ----------global variables---------- #

# measures,distance...
screen_width = 606
screen_height = 636
distance = 2.6
player_y = 376

#angles 
#--3 ways--#
up = 0
left = 1
right = 2
down = 3
#--2 ways--#
down_right = 4
down_left = 5
up_right = 6
up_left = 7
#--go back--#2
back = 8
#--cross--#
cross = 9


# initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PA C- MAN")


# images
img = pygame.image.load("images/walk.png").convert()
live_icon = pygame.transform.scale(surface=pygame.image.load(
            'images/player.png').convert_alpha(), size=(16, 16))
void = pygame.transform.scale(surface=pygame.image.load(
            'images/void.png').convert_alpha(), size=(16, 16))
map1 = pygame.transform.scale(surface=pygame.image.load(
            'images/map1.png').convert(), size=(250, 250))
map2 = pygame.transform.scale(surface=pygame.image.load(
            'images/map2.png').convert(), size=(250, 250))
map3 = pygame.transform.scale(surface=pygame.image.load(
            'images/map3.png').convert(), size=(250, 250))
arrow = pygame.transform.scale(surface=pygame.image.load(
            'images/arrow.png').convert(), size=(20, 20))
mag = pygame.transform.scale(surface=pygame.image.load(
            'images/mag.png').convert(), size=(250, 250))
