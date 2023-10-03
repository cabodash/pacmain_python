
import pygame
from Global import * 
from Map import *
from Player import Player
from Ghost import Ghost
from Wall import Wall
from Ball import Balls
from Live import Live

# ----------Gb variables---------- #





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




walls = walls1
angles = angles1

#Gb sounds
press_sound = pygame.mixer.Sound("sounds/menu_move.mp3")
siren_x1 = pygame.mixer.Sound("sounds/pacman-siren_x1.mp3")
siren_x2 = pygame.mixer.Sound("sounds/pacman-siren_x2.mp3")
siren_x3 = pygame.mixer.Sound("sounds/pacman-siren_x3.mp3")
siren_x4 = pygame.mixer.Sound("sounds/pacman-siren_x4.mp3")
siren = siren_x1



# -----------logic of the game----------- #

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


    # ---------- Stages of the game //  menus ---------- #

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

    #reset the Gb variables

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



        #powerup Gb timer var
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


        #Gb timer
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
