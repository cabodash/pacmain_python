from Global import *
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