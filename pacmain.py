
import pygame
import random

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
#--go back--#
back = 8
#--cross--#
cross = 9

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (236,124,38)
YELLOW = (255, 255, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
PURPLE = (87,35,100)
PINK = (255,0,128)


#default wall color
wall_color = BLUE


#main menu var
menu1_selected = 1
menu1_pressed = False
menu1_option1 = WHITE
menu1_option2 = WHITE
menu1_option3 = WHITE


#options menu var
menu2_map = 1
menu2_color = BLUE
menu2_color_text = "blue"
menu2_color_option = 6
menu2_credits_color = WHITE
menu2_selected = 1
menu2_pressed1 = False
menu2_pressed2 = False
arrow_animation = 0
arrow_animation_x = 10



#intro sound timer
intro_on = False
main_song_count = 0
intro_animation = 0
y_text = 255
main_color = WHITE



# default initial game state
game_state = "menu_main"


# score atributes
score = 0
scoreX = 390
scoreY = 10


#fonts
pygame.font.init()
scoreFont = pygame.font.Font("fonts/Emulogic-zrEw.ttf", 15)
timerFont = pygame.font.Font("fonts/Emulogic-zrEw.ttf", 10)
introFont = pygame.font.Font("fonts/Pacfont-ZEBZ.ttf", 15)


# initialize the screen
pygame.init()
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



# walk =[
#        pygame.image.load("images/walk0.png").convert(),
#        pygame.image.load("images/walk1.png").convert(),
#        pygame.image.load("images/walk2.png").convert(),
#        pygame.image.load("images/walk3.png").convert(),
#        pygame.image.load("images/walk4.png").convert(),
#        pygame.image.load("images/walk5.png").convert(),
#        pygame.image.load("images/walk6.png").convert(),
#        pygame.image.load("images/walk7.png").convert(),
#        pygame.image.load("images/walk8.png").convert(),
#        pygame.image.load("images/walk9.png").convert()]


# icon game
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


# set the game clock(FPS for gamer dudes)
clock = pygame.time.Clock()


# sprite groups
all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
gate = pygame.sprite.Group()
balls_list = pygame.sprite.Group()
powerup_list = pygame.sprite.Group()
live_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()


# walls for the map1
#(walls 2 and 3, as well as angles 2 and 3 are only trial mapped zones)
# (each one of them takes time for being created, thanks for the comprehension)

        #  x, y, ↔️, ↕️
walls1 = [[0, 0, 6, 245],
         [0, 305, 6, 295],
         [0, 0, 600, 6],
         [0, 600, 606, 6],
         [600, 0, 6, 245],
         [600, 305, 6, 295],
         [300, 0, 6, 66],
         [60, 60, 186, 6],
         [360, 60, 186, 6],
         [60, 120, 66, 6],
         [60, 120, 6, 126],
         [180, 120, 246, 6],
         [300, 120, 6, 66],
         [480, 120, 66, 6],
         [540, 120, 6, 126],
         [120, 180, 126, 6],
         [120, 180, 6, 126],
         [360, 180, 126, 6],
         [480, 180, 6, 126],
         [180, 240, 6, 126],
         [180, 360, 246, 6],
         [420, 240, 6, 126],
         [240, 240, 42, 6],
         [324, 240, 42, 6],
         [240, 240, 6, 66],
         [240, 300, 126, 6],
         [360, 240, 6, 66],
         [0, 300, 66, 6],
         [540, 300, 66, 6],
         [60, 360, 66, 6],
         [60, 360, 6, 186],
         [480, 360, 66, 6],
         [540, 360, 6, 186],
         [120, 420, 366, 6],
         [120, 420, 6, 66],
         [480, 420, 6, 66],
         [180, 480, 246, 6],
         [300, 480, 6, 66],
         [120, 540, 126, 6],
         [360, 540, 126, 6]
         ]

        #  x, y,   ↔️, ↕️
walls2 = [[0, 0,   6, 245],
         [0, 305,   6, 295],
         [0, 0,   600, 6],
         [0, 600,   606, 6],
         [600, 0,   6, 245],
         [600, 305,   6, 295],
         [60, 60,   6, 66],
         [60, 60,   66, 6],
         [540, 60,   6, 66],
         [480, 60,   66, 6],
         [180, 0,   6, 126],
         [420, 0,   6, 126],
         [240, 60,   126, 6],
         [240, 60,   6, 126],
         [360, 60,   6, 126],
         [300, 120,   6, 66],
         [180, 180,   66, 6],
         [360, 180,   66, 6],
         [0, 180,   126, 6],
         [480, 180,   126, 6],
         [120, 120,   6, 66],
         [480, 120,   6, 66],
         [60, 240,   126, 6],
         [420, 240,   126, 6],
         [60, 240,   6, 186],
         [540, 240,   6, 186],
         [180, 240,   6, 126],
         [420, 240,   6, 126],
         [180, 360,   66, 6],
         [360, 360,   66, 6],
         [240, 240,   42, 6],
         [324, 240,   42, 6],
         [240, 240,   6, 66],
         [240, 300,   126, 6],
         [360, 240,   6, 66],
#         [60, 300,   66, 6],
#         [480, 300,   66, 6],
         [120, 300,   6, 186],
         [480, 300,   6, 186],
         [180, 420,   66, 6],
         [360, 420,   66, 6],
         [0, 480,   186, 6],
         [420, 480,   186, 6],
         [240, 360,   6, 66],
         [360, 360,   6, 66],
         [300, 360,   6, 126],
         [240, 480,   126, 6],
         [60, 480,   6, 66],
         [540, 480,   6, 66],
         [240, 480,   6, 66],
         [360, 480,   6, 66],
         [120, 540,   6, 66],
         [300, 540,   6, 66],
         [480, 540,   6, 66],
         [180, 540,   66, 6],
         [360, 540,   66, 6],
         ]

        #  x, y, ↔️, ↕️
walls3 = [
         #limits   
         [0, 0, 6, 245],
         [0, 305, 6, 295],
         [0, 0, 600, 6],
         [0, 600, 606, 6],
         [600, 0, 6, 245],
         [600, 305, 6, 295],

         #ghost spawn
         [240, 240, 42, 6],
         [324, 240, 42, 6],
         [240, 240, 6, 66],
         [240, 300, 126, 6],
         [360, 240, 6, 66],

         #the other walls
         [180, 0, 6, 66],
         [420, 0, 6, 66],

         [0, 60, 66, 6],
         [120, 60, 6, 66],
         [240, 60, 126, 6],
         [300, 60, 6, 66],
         [480, 60, 6, 66],
         [540, 60, 66, 6],

         [60, 120, 126, 6],
         [180, 120, 6, 126],
         [240, 120, 6, 66],
         [360, 120, 6, 66],
         [420, 120, 6, 126],
         [420, 120, 126, 6],

         [60, 180, 66, 6],
         [120, 180, 6, 126],
         [240, 180, 126, 6],
         [480, 180, 6, 126],
         [480, 180, 66, 6],

         [0, 240, 66, 6],
         [540, 240, 66, 6],

         [60, 300, 6, 126],
         [120, 300, 66, 6],
         [300, 300, 6, 54],
         [420, 300, 66, 6],
         [540, 300, 6, 126],
         [120, 300, 66, 6],

         [120, 360, 66, 6],
         [180, 360, 6, 126],
         [240, 360, 6, 66],
         [360, 360, 6, 66],
         [420, 360, 6, 126],
         [420, 360, 66, 6],

         [60, 420, 66, 6],
         [240, 420, 126, 6],
         [480, 420, 66, 6],

         [0, 480, 66, 6],
         [120, 480, 6, 66],
         [240, 480, 6, 126],
         [300, 480, 6, 66],
         [360, 480, 6, 126],
         [480, 480, 6, 66],
         [540, 480, 66, 6],

         [60, 540, 126, 6],
         [420, 540, 126, 6],
         ]


#the zones in map that ghosts can decide to change the direction
angles1 = [
    #1
    [6, 28, 7, 27, down_right],



    [247, 266, 7, 27, down_left],
    [307, 326, 7, 27, down_right],



    [549, 568, 7, 27, down_left],
    #-----------------------------------#

    #2
    [6, 28, 67, 87, right],

    [126, 148, 67, 87, down],

    [246, 268, 67, 87, up],
    [306, 328, 67, 87, up],

    [426, 448, 67, 87, down],

    [546, 568, 67, 87, left],
    #-----------------------------------#

    #3

    [68, 87, 126.6, 147, down_right],
    [126, 148, 126.6, 147, up],

    [247, 266, 126.6, 147, down_left],
    [307, 326, 126.6, 147, down_right],

    [429, 446, 126.6, 147, up],
    [489, 506, 126.6, 147, down_left],

    #-----------------------------------#

    #4

    
    [127, 147, 185.5, 206.5, down_right],
    [186, 208, 185.5, 206.5, down],
    [246, 266, 185.5, 206.5, up],
    [306, 328, 185.5, 206.5, up],
    [366, 388, 185.5, 206.5, down],
    [429, 446, 185.5, 206.5, down_left],


    #-----------------------------------#

    #5
    [6, 28, 246, 270.3, up],
    [66, 88, 246, 270.3, left],






    [486, 508, 246, 270.3, right],
    [546, 548, 246, 270.3, up],
    #-----------------------------------#

    #6
    [8, 28, 308.7, 326.2, down_right],
    [66, 88, 308.7, 326.2, up],
    [127, 147, 308.7, 326.2, left],
    [187, 207, 308.7, 326.2, up_right],


    [367, 386, 308.7, 326.2, up_left],
    [426, 448, 308.7, 326.2, right],
    [486, 508, 308.7, 326.2, up],
    [549, 568, 308.7, 326.2, down_left],
    #-----------------------------------#

    #7

    [68, 87, 368.5, 386, down_right],
    [489, 506, 368.5, 386, up],




    [426, 448, 368.5, 386, up],
    [489, 506, 368.5, 386, down_left],

    #-----------------------------------#

    #8


    [489, 506, 428.4, 448.6, down_right],




    [426, 448, 428.4, 448.6, down_left],


    #-----------------------------------#

    #9

    [66, 88, 487, 507, right],
    [126, 148, 487, 507, up],

    [247, 266, 487, 507, down_left],
    [307, 326, 487, 507, down_right],

    [426, 448, 487, 507, up],
    [486, 508, 487, 507, left],

    #-----------------------------------#

    #10
    [8, 28, 548, 567, up_right],
    [68, 87, 548, 567, up],


    [246, 266, 548, 567, up],
    [306, 326, 548, 567, up],


    [486, 506, 548, 567, up],
    [549, 568, 548, 567, up_left],
    #-----------------------------------#
    ]

angles2 = [
    #1
    [8, 28, 7, 27, down_right],
    [127, 147, 7, 27, down_left],
    [187, 207, 7, 27, down_right],
    [367, 386, 7, 27, down_left],
    [429, 446, 7, 27, down_right],
    [549, 568, 7, 27, down_left],

    #2
    [68, 87, 67, 87, down_right],
    [127, 146, 76, 87, left],
    [247, 266, 76, 87, down_right],
    [307, 326, 76, 87, down_left],
    [429, 446, 76, 87, right],
    [489, 506, 76, 87, down_left],

    #3
    [8, 28, 126.6, 147, up_right],
    [68, 87, 126.6, 147, up_left],
    [126.6, 147, 126.6, 147, right],
    [187, 207, 126.6, 147, up_left],
    [367, 386, 126.6, 147, up_right],
    [429, 446, 126.6, 147, left],
    [489, 506, 126.6, 147, up_right],
    [549, 568, 126.6, 147, up_left],

    #4
    [8, 28, 185.5, 206, down_right],
    [127, 147, 185.5, 206.5, up],
    [187, 207, 185.5, 206.5, down],
    [247, 266, 185.5, 206.5, up],
    [307, 326, 185.5, 206.5, up],
    [367, 386, 185.5, 206.5, down],
    [429, 446, 185.5, 206.5, up],
    [549, 568, 185.5, 206.5, down_left],
    
    #5
    [8, 28, 246, 270.3, left],
    [68, 87, 246, 270.3, down_right],
    [127, 147, 246, 270.3, down_left],
    [429, 446, 246, 270.3, down_right],
    [489, 506, 246, 270.3, down_left],
    [549, 568, 246, 271.3, right],

    #6
    [187, 207, 308.7, 326.2, up_right],
    [247, 266, 308.7, 326.2, down],
    [307, 326, 308.7, 326.2, down],
    [367, 386, 308.7, 326.2, up_left],

    #7
    [127, 147, 368.5, 386, right],
    [187, 207, 368.5, 386, back],
    [367, 386, 368.5, 386, back],
    [429, 446, 368.5, 386, left],

    #8
    [8, 28, 428.4, 448.6, up_right],
    [68, 87, 428.4, 448.6, up_left],
    [127, 146, 428, 448.6, up_right],
    [187, 207, 428, 448.6, down],
    [247, 266, 428, 448.6, up_left],
    [307, 326, 428, 448.6, up_right],
    [367, 386, 428, 448.6, down],
    [429, 446, 428, 448.6, up_left],
    [489, 506, 428, 448.6, up_right],
    [549, 568, 428, 448.6, up_left],
    #9
    [8, 28, 488, 508.2, back],
    [68, 87, 488, 508.2, down_right],
    [127, 146, 488, 508.2, down],
    [187, 207, 488, 508.2, up_left],
    [247, 266, 488, 508.2, down_right],
    [307, 326, 488, 508.2, down_left],
    [367, 386, 488, 508.2, up_right],
    [429, 446, 488, 508.2, down],
    [489, 506, 488, 508.2, down_left],
    [549, 568, 488, 508.2, back],

    #10
    [8, 28, 548, 567, up_right],
    [68, 87, 548, 567, up_left],
    [127, 146, 548, 568, up_right],
    [247, 266, 548, 568, up_left],
    [307, 326, 548, 568, up_right],
    [429, 446, 548, 568, up_left],
    [489, 506, 548, 568, up_right],
    [549, 568, 548, 568, up_left],
    ]

angles3 = [
    #1
    [8, 28, 7, 27, back],
    [68, 87, 7, 27, down],
    [127, 147, 7, 27, down_left],
    [187, 207, 7, 27, down_right],


    [367, 386, 7, 27, down_left],
    [427, 446, 7, 27, down_right],
    [489, 506, 7, 27, down],
    [549, 568, 7, 27, back],
    #-----------------------------------#

    #2
    [8, 28, 76, 87, down_right],
    [68, 87, 76, 87, up_left],
    [127, 147, 76, 87, up_right],
    [187, 207, 76, 87, cross],
    [247, 266, 76, 87, down_left],
    [307, 326, 76, 87, down_right],
    [367, 386, 76, 87, cross],
    [427, 446, 76, 87, up_left],
    [489, 506, 76, 87, up_right],
    [549, 568, 76, 87, down_left],
    #-----------------------------------#

    #3
    [8, 28, 126.6, 147, right],

    [127, 147, 126.6, 147, down_left],

    [247, 266, 126.6, 147, up_right],
    [307, 326, 126.6, 147, up_left],

    [427, 446, 126.6, 147, down_right],

    [549, 568, 126.6, 147, left],
    #-----------------------------------#

    #4
    [8, 28, 185.5, 206.5, up_right],
    [68, 87, 185.5, 206.5, down_left],

    [187, 207, 185.5, 206.5, right],


    [367, 386, 185.5, 206.5, left],

    [489, 506, 185.5, 206.5, down_right],
    [549, 568, 185.5, 206.5, up_left],
    #-----------------------------------#

    #5
    [8, 28, 246, 270.3, down],
    [68, 87, 246, 270.3, left],
    [127, 147, 246, 270.3, up_right],
    [187, 207, 246, 270.3, left],
   

    [367, 386, 246, 270.3, right],
    [427, 446, 246, 270.3, up_left],
    [489, 506, 246, 270.3, right],
    [549, 568, 246, 270.3, down],
    #-----------------------------------#

    #6

    [68, 87, 308.7, 326.2, right],

    [187, 207, 308.7, 326.2, cross],
    [247, 266, 308.7, 326.2, down_left],
    [307, 326, 308.7, 326.2, down_right],
    [367, 386, 308.7, 326.2, cross],

    [489, 506, 308.7, 326.2, left],
    #-----------------------------------#

    #7

    [68, 87, 368.5, 386, up_right],
    [127, 147, 368.5, 386, down_left],

    [247, 266, 368.5, 386, up_right],
    [307, 326, 368.5, 386, up_left],

    [427, 446, 368.5, 386, down_right],
    [489, 506, 368.5, 386, up_left],

    #-----------------------------------#

    #8
    [8, 28, 428.4, 448.6, up_left],
    [68, 87, 428.4, 448.6, down],
    [127, 147, 428.4, 448.6, left],
    [187, 207, 428.4, 448.6, right],
    [247, 266, 428.4, 448.6, down],
    [307, 326, 428.4, 448.6, down],
    [367, 386, 428.4, 448.6, left],
    [427, 446, 428.4, 448.6, right],
    [489, 506, 428.4, 448.6, down],
    [549, 568, 428.4, 448.6, up_left],
    #-----------------------------------#

    #9
    [8, 28, 488, 508.2, down_right],
    [68, 87, 488, 508.2, up_left],
    [127, 147, 488, 508.2, up_right],
    [187, 207, 488, 508.2, left],


    [367, 386, 488, 508.2, right],
    [427, 446, 488, 508.2, up_left],
    [489, 506, 488, 508.2, up_right],
    [549, 568, 488, 508.2, down_left],
    #-----------------------------------#

    #10
    [8, 28, 548, 567, up_right],


    [187, 207, 548, 567, up_left],
    [247, 266, 548, 567, up_right],
    [307, 326, 548, 567, up_left],
    [367, 386, 548, 567, up_right],


    [549, 568, 548, 567, up_left],
    #-----------------------------------#
    ]


walls = walls1
angles = angles1

#global sounds
press_sound = pygame.mixer.Sound("sounds/menu_move.mp3")
siren_x1 = pygame.mixer.Sound("sounds/pacman-siren_x1.mp3")
siren_x2 = pygame.mixer.Sound("sounds/pacman-siren_x2.mp3")
siren_x3 = pygame.mixer.Sound("sounds/pacman-siren_x3.mp3")
siren_x4 = pygame.mixer.Sound("sounds/pacman-siren_x4.mp3")
siren = siren_x1


# ------------ Create the Classes ------------#

# walls class
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


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




# Map live's class
class Lives(pygame.sprite.Sprite):
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




# player class
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
                player.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 360)

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.x -= distance
            self.direction = 1
            self.walk = True
            if self.died_timer:
                player.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 180)

        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.y -= distance
            self.direction = 0
            self.walk = True
            if self.died_timer:
                player.image = void
            else:
                self.image = pygame.transform.rotate(self.imageSource, 90)

        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.y += distance
            self.direction = 3
            self.walk = True
            if self.died_timer:
                player.image = void
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




# create the class ghost
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #coordinates
        self.x = 303 - 15
        self.y = 318 - 61

        # ghost images
        self.image_up = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_up.png').convert_alpha(), size=(32, 32))
        self.image_left = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_left.png').convert_alpha(), size=(32, 32))
        self.image_right = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_right.png').convert_alpha(), size=(32, 32))
        self.image_down = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_down.png').convert_alpha(), size=(32, 32))
        self.image_up_hidden = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_up_h.png').convert_alpha(), size=(32, 32))
        self.image_left_hidden = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_left_h.png').convert_alpha(), size=(32, 32))
        self.image_right_hidden = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_right_h.png').convert_alpha(), size=(32, 32))
        self.image_down_hidden = pygame.transform.scale(surface=pygame.image.load(
            'images/ghost_down_h.png').convert_alpha(), size=(32, 32))

        # ghost variables
        self.image = self.image_up
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.direction = 0
        self.new_direction = 0
        self.distance = 2.1
        self.collide = False
        self.colition = False
        self.in_angle = False
        self.angle_regist = False
        self.angle_changed = True
        self.hidding = False
        self.pause_timer = False
        self.pause_timer_count = 0

    # change the ditection of the ghosts
    def changeDirection(self):
        if self.direction == left:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = up

        if self.direction == right:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = up

        if self.direction == up:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right
        
        if self.direction == down:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right

    # move ghosts
    def move(self, ghost_distance):
        # up
        if self.direction == 0:
            self.y -= ghost_distance
            if self.hidding:
                self.image = self.image_up_hidden
            elif not self.hidding:
                self.image = self.image_up

        # left
        if self.direction == 1:
            self.x -= ghost_distance
            if self.hidding:
                self.image = self.image_left_hidden
            elif not self.hidding:
                self.image = self.image_left

        # right
        if self.direction == 2:
            self.x += ghost_distance
            if self.hidding:
                self.image = self.image_right_hidden
            elif not self.hidding:
                self.image = self.image_right

        # down
        if self.direction == 3:
            self.y += ghost_distance
            if self.hidding:
                self.image = self.image_down_hidden
            elif not self.hidding:
                self.image = self.image_down

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    # draw the ghost witout move
    def draw(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    # functions for exit the walls
    def avoid_top(self):
        self.y += self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_left(self):
        self.x += self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_right(self):
        self.x -= self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)

    def avoid_bottom(self):
        self.y -= self.distance
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        screen.blit(self.image, self.rect)


    # function that decides the direcction of the ghost when they are in an area with more 4 ways
    def cross(self):
        if self.direction == up:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = left
            
            elif angleDirection == 3:
                self.direction = right

        if self.direction == left:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = left

            elif angleDirection == 3:
                self.direction = down

        if self.direction == right:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = right

            elif angleDirection == 3:
                self.direction = down

        if self.direction == down:
            angleDirection = random.randint(1, 3)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right

            elif angleDirection == 3:
                self.direction = down


    # functions that decides the direcction of the ghost when they are in an area with 3 ways
    def angle_up(self):
        if self.direction == left:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = left

        if self.direction == right:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = right

        if self.direction == down:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right

    # functions that decides the direcction of the ghost when they are in an area with more than 2 ways
    def angle_left(self):
        if self.direction == down:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = left

        if self.direction == up:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = left

        if self.direction == right:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = down

    # functions that decides the direcction of the ghost when they are in an area with more than 2 ways
    def angle_right(self):
        if self.direction == up:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = right

        if self.direction == down:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = right

        if self.direction == left:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = up

            elif angleDirection == 2:
                self.direction = down

    # functions that decides the direcction of the ghost when they are in an area with more than 2 ways
    def angle_down(self):
        if self.direction == left:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = left

        if self.direction == right:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = down

            elif angleDirection == 2:
                self.direction = right

        if self.direction == up:
            angleDirection = random.randint(1, 2)
            if angleDirection == 1:
                self.direction = left

            elif angleDirection == 2:
                self.direction = right
    
    #functions that changes the direcction for angles with only 2 directions/ways
    def angle_down_r(self):
        if self.direction == up:
            self.direction = right
        elif self.direction == left:
            self.direction = down
    
    def angle_down_l(self):
        if self.direction == up:
            self.direction = left
        elif self.direction == right:
            self.direction = down
    
    def angle_up_r(self):
        if self.direction == down:
            self.direction = right
        elif self.direction == left:
            self.direction = up
    
    def angle_up_l(self):
        if self.direction == down:
            self.direction = left
        elif self.direction == right:
            self.direction = up

    #function that go back the ghost because the place only have 1 direction
    def go_back(self):
        if self.direction == up:
            self.direction = down
        elif self.direction == down:
            self.direction = up
        elif self.direction == right:
            self.direction = left
        elif self.direction == left:
            self.direction = right






# -----------logic of the game-----------#

# black background
screen.fill(BLACK)

# game running
while True:
    # if close window or button 'esc' is pressed the game closes
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            pygame.quit()
            exit()


    # ---------- Stages of the game //  menus ----------#

    # main menu
    if game_state == "menu_main":

        #menu graphics
        screen.fill(BLACK)
        screen.blit(scoreFont.render(
            "Play Pac-Man", 1, (menu1_option1)), (217, 263))
        screen.blit(scoreFont.render(
            "Options", 1, (menu1_option2)), (252, 303))
        screen.blit(scoreFont.render(
            "Quit Game", 1, (menu1_option3)), (235, 343))
        screen.blit(timerFont.render(
            "Use the spacebar to enter the option", 1, (WHITE)), (120, 600)) 
        
        #menu logic

        if key[pygame.K_UP] or key[pygame.K_w]:
            if not menu1_pressed:
                menu1_selected -= 1
                menu1_pressed = True
                press_sound.play()

        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            if not menu1_pressed:
                menu1_selected += 1
                menu1_pressed = True
                press_sound.play()

        else:
            menu1_pressed = False
        
        #do the pass 1_selected to 3_selected and 3_selected to 1_selected
        if menu1_selected < 1:
            menu1_selected = 3
        elif menu1_selected > 3:
            menu1_selected = 1

        
        #arrow animation
        arrow_animation += 1
        if arrow_animation < 20:
            arrow_animation_x = 0
        elif arrow_animation >= 20 and arrow_animation < 40:
            arrow_animation_x = 10
        elif arrow_animation >= 40:
            arrow_animation = 0

        if menu1_selected == 1:
            menu1_option1 = YELLOW
            menu1_option2 = WHITE
            menu1_option3 = WHITE
            screen.blit(arrow, (185 - arrow_animation_x,263))
        elif menu1_selected == 2:
            menu1_option1 = WHITE
            menu1_option2 = YELLOW
            menu1_option3 = WHITE
            screen.blit(arrow, (220 - arrow_animation_x,303))
        elif menu1_selected == 3:
            menu1_option1 = WHITE
            menu1_option2 = WHITE
            menu1_option3 = YELLOW
            screen.blit(arrow, (203 - arrow_animation_x,343))
        
        if key[pygame.K_SPACE]:
            if menu1_selected == 1:
                press_sound.play()
                game_state = "game_starting"
            elif menu1_selected == 2:
                press_sound.play()
                game_state = "menu_options"
                menu2_selected = 1
            elif menu1_selected == 3:
                press_sound.play()
                pygame.quit()
                exit()
        pygame.display.update() 
         

    


#options menu
    elif game_state == "menu_options":

        #menu graphics
        screen.fill(BLACK)
        screen.blit(scoreFont.render(
            f"Select Map: {menu2_map}", 1, (WHITE)), (205, 20))
        screen.blit(scoreFont.render(
            f"Color: {menu2_color_text}", 1, (menu2_color)), (220, 360))
        screen.blit(scoreFont.render(
            "Credits", 1, (menu2_credits_color)), (240, 410))
        screen.blit(scoreFont.render(
            "Press 'm' to go main menu", 1, (WHITE)), (110, 510))
        

        #menu logic

        #go main menu
        if key[pygame.K_m]:
            press_sound.play()
            game_state = "menu_main"

        #change the selected option up and down
        if key[pygame.K_UP] or key[pygame.K_w]:
            if not menu2_pressed1:
                press_sound.play()
                menu2_selected -= 1
                menu2_pressed1 = True
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            if not menu2_pressed1:
                press_sound.play()
                menu2_selected += 1
                menu2_pressed1 = True
        else:
            menu2_pressed1 = False

        #change the arrow position
        if menu2_selected == 1:
            screen.blit(arrow, (165 - arrow_animation_x,20))
            menu2_credits_color = WHITE
        elif menu2_selected == 2:
            screen.blit(arrow, (180 - arrow_animation_x,360))
            menu2_credits_color = WHITE
        elif menu2_selected == 3:
            screen.blit(arrow, (200 - arrow_animation_x,410))
            menu2_credits_color = YELLOW
        
        #arrow animation
        arrow_animation += 1
        if arrow_animation < 20:
            arrow_animation_x = 0
        elif arrow_animation >= 20 and arrow_animation < 40:
            arrow_animation_x = 10
        elif arrow_animation >= 40:
            arrow_animation = 0

        #change the selected option right and left
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if not menu2_pressed2:
                if menu2_selected == 1:
                    menu2_map += 1
                    press_sound.play() 
                elif menu2_selected == 2:
                    menu2_color_option += 1
                    press_sound.play() 
                menu2_pressed2 = True
               

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            if not menu2_pressed2:
                if menu2_selected == 1:
                    menu2_map -= 1
                    press_sound.play() 
                elif menu2_selected == 2:
                    menu2_color_option -= 1
                    press_sound.play() 
                menu2_pressed2 = True

        else:
            menu2_pressed2 = False

        if key[pygame.K_SPACE] and menu2_selected == 3:
            game_state = "credits"

        #do the pass 1_selected to 2_selected and 2_selected to 1_selectedv
        if menu2_selected > 3:
            menu2_selected = 1
        elif menu2_selected < 1:
            menu2_selected = 3
        
        #do the pass 1_selected to 3_selected and 3_selected to 1_selected
        if menu2_map > 3:
            menu2_map = 1
        elif menu2_map < 1:
            menu2_map = 3

        #change the map image
        if menu2_map == 1:
            screen.blit(map1,(178,65))
            walls = walls1
            angles = angles1
            player_y = 376
        elif menu2_map == 2:
            screen.blit(map2,(178,65))
            walls = walls2
            angles = angles2
            player_y = 316
        elif menu2_map == 3:
            screen.blit(map3,(178,65))
            walls = walls3
            angles = angles3
            player_y = 376
        

        #do the pass 1_selected to 8_selected and 8_selected to 1_selected    
        if menu2_color_option < 1:
            menu2_color_option = 8
        elif menu2_color_option > 8:
            menu2_color_option = 1

        if menu2_color_option == 1:
            menu2_color_text = "white"
            menu2_color = WHITE
            wall_color = WHITE
        elif menu2_color_option == 2:
            menu2_color_text = "red"
            menu2_color = RED
            wall_color = RED
        elif menu2_color_option == 3:
            menu2_color_text = "orange"
            menu2_color = ORANGE
            wall_color = ORANGE
        elif menu2_color_option == 4:
            menu2_color_text = "yellow"
            menu2_color = YELLOW
            wall_color = YELLOW
        elif menu2_color_option == 5:
            menu2_color_text = "green"
            menu2_color = GREEN
            wall_color = GREEN
        elif menu2_color_option == 6:
            menu2_color_text = "blue"
            menu2_color = BLUE
            wall_color = BLUE
        elif menu2_color_option == 7:
            menu2_color_text = "purple"
            menu2_color = PURPLE
            wall_color = PURPLE
        elif menu2_color_option == 8:
            menu2_color_text = "pink"
            menu2_color = PINK
            wall_color = PINK

        pygame.display.update()




    elif game_state == "credits":
        #credit graphics
        screen.fill(BLACK)
        screen.blit(timerFont.render(
            "Thanks to magnitopic to collaborate in this game", 1, (WHITE)), (60, 100))
        screen.blit(timerFont.render(
            "Profile: github.com/magnitopic", 1, (YELLOW)), (150, 140))
        screen.blit(mag,(175, 200))
        screen.blit(timerFont.render(
            "To go main menu, press 'm' button", 1, (BLUE)), (130, 500))
        screen.blit(timerFont.render(
            "To go options menu, press 'o' button", 1, (GREEN)), (113, 520))
        screen.blit(timerFont.render(
            "Also, my github is github.com/cabodash", 1, (PURPLE)), (107, 570))

        #credit logic
        if key[pygame.K_m]:
            game_state = "menu_main"
            menu1_selected = 1
        elif key[pygame.K_o]:
            game_state = "menu_options"
            menu2_selected = 1

        pygame.display.update()




    # game starting
    elif game_state == "game_starting":

        # main song
        if not intro_on:
            main_song = pygame.mixer.Sound("sounds/intro.wav")
            main_song.play()
            intro_on = True

        elif intro_on:
            main_song_count += 1
            if main_song_count >= (main_song.get_length()*60):
                intro_on = False
                main_song_count = 0
                game_state = "game_init"

    # intro animation
        if intro_animation < 16:
            y_text = 300
            main_color = WHITE
            intro_animation += 1
        elif intro_animation >= 16 and intro_animation < 32:
            y_text = 290
            main_color = YELLOW                      
            intro_animation += 1
        elif intro_animation >= 32:
            intro_animation = 0
        
        #intro animation
        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(introFont.render(
            "pacman", 1, (main_color)), (255, y_text))

    

    #game charging
    elif game_state == "game_init":

    #reset the global variables

        #pacman distance
        distance = 2.6

        #dots conunt
        dots_eated = 0

        #timer
        milli = 0
        sec = 0
        minutes = 0

        #siren sound clock
        siren_on = False
        siren_count = 0



        #powerup global timer var
        hidding_count = 0
        hidding_state = False


        # ---------- Create the objects in the map ----------#

        # create the list that contain all the objects that means wall in the game and posicionate the walls in the screen
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], wall_color)
            wall_list.add(wall)
            all_sprites_list.add(wall)



        # the white gate for the ghost spawn
        gate.add(Wall(282, 242, 42, 2, WHITE))
        all_sprites_list.add(gate)



        # create the list of powerups and possitionate it in the map
        powerup = [Balls(87, 87,15), Balls(507, 87,15),
                Balls(87, 507,15), Balls(507, 507,15)]
        powerup_list.add(powerup)



        # create the list of balls/dots and possitionate it in the map
        balls = [Balls(x, y, 10) for x in range(30, 600, 60)for y in range(
            30, 600, 60) if not (180 < x < 360 and 180 < y < 420)]
        balls_list.add(balls)



        # create Pacman player
        player = Player()



        # create the ghosts and the list of them
        ghost1 = Ghost()
        ghost2 = Ghost()
        ghost3 = Ghost()
        ghost4 = Ghost()
        ghosts = [ghost1,
                ghost2,
                ghost3,
                ghost4
                ]

        #start the game
        game_state = "game_playing"







    # running game / playing
    elif game_state == "game_playing":


    # -----data (lives,score,time...)-----#
        # draw score
        text = scoreFont.render(f"Your score: {score}", 1, (255, 255, 255))
        screen.blit(text, (scoreX, scoreY))
        # score's position
        if player.x > 300 and player.y < 100:
            scoreX = scoreY = 10
        else:
            scoreX, scoreY = 340, 10

        #pacman coordinates
#        cor = scoreFont.render(f"x:{player.x} y:{player.y}",1, (255,255,255))
#        screen.blit(cor,(10, 570))
        #ghost not moving, for menu image
#        for ghost in ghosts:
#            ghost.distance = 0


        #render lives
        if player.lives == 3:
            screen.blit(live_icon,(5, 613))
            screen.blit(live_icon,(22, 613))
            screen.blit(live_icon,(39, 613))
        elif player.lives == 2:
            screen.blit(live_icon,(5, 613))
            screen.blit(live_icon,(22, 613))
        elif player.lives == 1:
            screen.blit(live_icon,(5, 613))


        #global timer
        milli += 1
        if milli >= 60:
            sec += 1
            milli = 0
        if sec >= 60:
            minutes += 1
            sec = 0
        if minutes >= 5:
            game_state = "game_closed"

        timer = scoreFont.render(
            f"Min:{minutes},Sec:{sec}", 1, (255, 255, 255))
        screen.blit(timer, (100, 610))
# this is for another thing if i need to agregate, to give info (the important thing is the x and y) 
#        screen.blit(timer, (300, 610))


        #player dead timer
        if player.died_timer:
            distance = 0
            player.image = void
            for ghost in ghosts:
                ghost.distance = 0
            player.died_timer_count +=1
            if player.died_timer_count >= 120:
                distance = 2.6
                for ghost in ghosts:
                    ghost.distance = 2.1
                player.died_timer = False
                player.died_timer_count = 0
                player.image = player.imageSource



    #---------- Logic functions/algorithms ----------#

        # player trespassing side to side (like a rollercoaster, el q entendió, entendió)
        if player.x <= -32:
            player.x = 605
        elif player.x >= 606:
            player.x = -31
        # ghosts trespassing side to side (like a rollercoaster, el q entendió, entendió)
        for ghost in ghosts:
            if ghost.x <= -32:
                ghost.x = 605
            elif ghost.x >= 606:
                ghost.x = -31

        
        #ghost siren clock
        if not siren_on:
            siren.play()
            siren_on = True
        elif siren_on:
            siren_count += 1
            if siren_count >= (siren.get_length()*60):
                siren_count = 0
                siren.play()

        
        #change the siren
        if dots_eated < 22:
            siren = siren_x1
        elif dots_eated >= 22 and dots_eated < 44:
            siren = siren_x2
        elif dots_eated >= 44 and dots_eated < 66:
            siren = siren_x2
        elif dots_eated >= 66:
            siren = siren_x4


        # check if pacman eats a dot/ball
        eat_dot = pygame.sprite.spritecollide(player, balls_list, True)
        if eat_dot != []:
            score += 200
            dots_eated += 1
            player.waka_waka.play()


        # check if pacman eats a power up
        eat_powerup = pygame.sprite.spritecollide(player, powerup_list, True)
        if eat_powerup != []:
            if hidding_state:
                hidding_count = 0
            score += 600
            for ghost in ghosts:
                ghost.hidding = True
                hidding_state = True
        #hidding internal timer
        if hidding_state:
            hidding_count += 1
            if hidding_count >= 480:
                hidding_count = 0
                hidding_state = False
                for ghost in ghosts:
                    ghost.hidding = False

        # move pacman
        player.move(distance, key)


        # renderize/update the window (this need to be here, for no bugs)
        pygame.display.update()
        screen.fill(BLACK)
        wall_list.draw(screen)
        gate.draw(screen)
        balls_list.draw(screen)
        powerup_list.draw(screen)
#        live_list.draw(screen)
        player.draw()


        # pacman avoiding the walls
        pacman_colition = any([True if player.rect.colliderect(
            wall.rect) else False for wall in wall_list])
        pacman_colition_gate = any(
            [True if player.rect.colliderect(gate.rect) else False for gate in gate])
        if pacman_colition and player.direction == 0:
            player.y += distance

        if pacman_colition and player.direction == 1:
            player.x += distance

        if pacman_colition and player.direction == 2:
            player.x -= distance

        if pacman_colition and player.direction == 3:
            player.y -= distance

        if pacman_colition_gate and player.direction == 3:
            player.y -= distance
        

        #------ghost movement------#
        for ghost in ghosts:
            
            # ghost wall detection
            for wall in wall_list:
                ghost.collide = pygame.Rect.colliderect(ghost.rect, wall.rect)
                if ghost.collide:
                    break

            if not ghost.collide and not ghost.colition:
                #print("no no")
                ghost.move(ghost.distance)
            elif ghost.collide and not ghost.colition:
                #print("si no")
                ghost.colition = True
                ghost.draw()

            elif ghost.collide and ghost.colition:
                #print("si si")
                if ghost.direction == 0:
                    ghost.avoid_top()

                if ghost.direction == 1:
                    ghost.avoid_left()

                if ghost.direction == 2:
                    ghost.avoid_right()

                if ghost.direction == 3:
                    ghost.avoid_bottom()

            elif not ghost.collide and ghost.colition:
                #print("no si")
                ghost.colition = False
                ghost.changeDirection()
                ghost.move(ghost.distance)


            # loop for the ghosts (this is for the change of direction in the angles)
            for hitbox in angles:
                if hitbox[0] <= (ghost.x + 1) and hitbox[1] >= (ghost.x - 1) and hitbox[2] <= (ghost. y+ 1) and hitbox[3] >= (ghost.y  -1):
                    ghost.in_angle = True
                    break
                else:
                    ghost.in_angle = False

            if not ghost.in_angle and not ghost.angle_regist:
                print("no no")

            elif ghost.in_angle and not ghost.angle_regist:
                print("si no")
                ghost.angle_regist = True

            elif ghost.in_angle and ghost.angle_regist and not ghost.angle_changed:
                print("si si no")
                if hitbox[4] == up:
                    ghost.angle_up()
                    print("up")

                elif hitbox[4] == left:
                    ghost.angle_left()
                    print("left")

                elif hitbox[4] == right:
                    ghost.angle_right()
                    print("right")

                elif hitbox[4] == down_right:
                    ghost.angle_down_r()
                    print("down")
                
                elif hitbox[4] == down_left:
                    ghost.angle_down_l()
                
                elif hitbox[4] == up_right:
                    ghost.angle_up_r()
                
                elif hitbox[4] == up_left:
                    ghost.angle_up_l()

                elif hitbox[4] == back:
                    ghost.go_back()

                elif hitbox[4] == cross:
                    ghost.cross()

                ghost.angle_changed = True

            elif ghost.in_angle and ghost.angle_regist and ghost.angle_changed:
                pass

            elif not ghost.in_angle and ghost.angle_regist:
                print("no si")
                ghost.angle_regist = False
                ghost.angle_changed = False


            # player hit ghost
            if ghost.rect.colliderect(player.rect):

                #ghost is hidding
                if ghost.hidding:
                    player.eat_ghost.play()
                    score += 1200
                    ghost.pause_timer = True
                    ghost.x = 303 - 15
                    ghost.y = 318 - 61
                    ghost.direction = 0
                    ghost.distance = 0

                #ghost is not hidding
                elif not ghost.hidding:
                    player.dies.play()
                    player.x = 303 - 15
                    player.y = player_y
                    player.lives -= 1
                    if player.lives <= 0:
                        game_state = "game_over"
                        pygame.sprite.Group.empty(all_sprites_list)
                        pygame.sprite.Group.empty(wall_list)
                        pygame.sprite.Group.empty(gate)
                        pygame.sprite.Group.empty(balls_list)
                        pygame.sprite.Group.empty(powerup_list)
                        pygame.sprite.Group.empty(live_list)
                        pygame.sprite.Group.empty(player_list)
                    else:
                        player.died_timer = True


            # ghost respawning timer (----------to do:change the image for an eyes and go to the respawn----------)
            if ghost.pause_timer:
                ghost.pause_timer_count += 1
                if ghost.pause_timer_count >= 270:
                    # reactivate the ghost
                    ghost.pause_timer = False
                    ghost.pause_timer_count = 0
                    ghost.hidding = False
                    ghost.distance = 2.1

        
        #end of the game
        if dots_eated == 88:
            game_state = "game_ended"





    # game over
    elif game_state == "game_over":
        screen.fill(BLACK)
        screen.blit(scoreFont.render("GAME_OVER", 1, (RED)), (240, 220))
        screen.blit(timerFont.render("press the spacebar to go play another time", 1, (WHITE)), (100, 300))
        screen.blit(timerFont.render("press 'm'button to go main menu", 1, (WHITE)), (150, 320))
        screen.blit(timerFont.render("or press 'o'button to go options menu", 1, (WHITE)), (120, 340))


        if key[pygame.K_SPACE]:
            game_state = "game_init"
        elif key[pygame.K_m]:
            game_state = "menu_main"
            menu1_selected = 1
        elif key[pygame.K_o]:
            game_state = "menu_options"
            menu2_selected = 1
        pygame.display.update()



    # game closed due to inactivity or very bad skills
    elif game_state == "game_closed":
        screen.fill(BLACK)
        screen.blit(scoreFont.render(
            "You are bad at this game bruh :|", 1, (RED)), (75, 310))
        screen.blit(scoreFont.render(
            "The game ended due to inactivity", 1, (RED)), (75, 340))
        pygame.display.update()



    # game ended
    elif game_state == "game_ended":
        screen.fill(BLACK)
        screen.blit(scoreFont.render("You win :D", 1, (WHITE)), (255, 300))
        screen.blit(scoreFont.render(f"Total Score: {score}", 1, (YELLOW)), (180, 330))
        pygame.display.update()



    # set frames per second (FPS)
    clock.tick(60)
