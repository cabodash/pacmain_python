from Global import *
import random


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

