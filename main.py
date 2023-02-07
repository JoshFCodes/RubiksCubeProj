# Rubik's Cube Solver version 1.1
# Joshua Frechette @JoshFCodes
# 12.28.2022

from CubeIntake import init_Cube
from CubeMovements import *
from Pieces import *
from BiGBrAiN import *



if __name__ == '__main__':

    #Cube = init_Cube()


    # Cube = {"White": ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W','W'],
    #            "Green": ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G','G'],
    #            "Orange": ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O','O'],
    #            "Blue": ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B','B'],
    #            "Red": ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R','R'],
    #            "Yellow": ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y','Y'],}
    #
    # yellow_clock(Cube)
    # green_clock(Cube)
    # orange_counter(Cube)
    # white_counter(Cube)
    # blue_clock(Cube)
    # red_clock(Cube)
    # white_clock(Cube)
    # orange_clock(Cube)
    # yellow_clock(Cube)
    # green_counter(Cube)
    # yellow_counter(Cube)
    # blue_counter(Cube)
    # red_counter(Cube)
    # orange_counter(Cube)
    # orange_counter(Cube)
    # blue_counter(Cube)
    # white_counter(Cube)
    # orange_clock(Cube)


    #Jarbled cube
    Cube = {'White': ['Y', 'Y', 'R', 'G', 'W', 'O', 'B', 'B', 'W'],
            'Green': ['R', 'R', 'G', 'O', 'G', 'G', 'B', 'G', 'Y'],
            'Orange': ['Y', 'W', 'G', 'G', 'O', 'O', 'O', 'W', 'Y'],
            'Blue': ['B', 'R', 'O', 'W', 'B', 'R', 'R', 'B', 'W'],
            'Red': ['W', 'B', 'G', 'Y', 'R', 'Y', 'O', 'O', 'W'],
            'Yellow': ['O', 'R', 'R', 'W', 'Y', 'B', 'B', 'Y', 'G']}

    #Cube with one green corner missing in pos 8 of red face
    # Cube = {'White': ['W', 'W', 'W', 'R', 'W', 'W', 'O', 'B', 'B'],
    #         'Green': ['G', 'G', 'G', 'G', 'G', 'G', 'O', 'G', 'G'],
    #         'Orange': ['B', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'R'],
    #         'Blue': ['Y', 'R', 'Y', 'W', 'B', 'Y', 'W', 'O', 'W'],
    #         'Red': ['R', 'R', 'R', 'R', 'R', 'W', 'R', 'Y', 'G'],
    #         'Yellow': ['Y', 'Y', 'Y', 'O', 'Y', 'Y', 'B', 'B', 'B']}


    #green_cross_check(Cube, True)
    #place_green_sides(Cube, green_cross_check(Cube, True))

    #green_corner_check_top(Cube)

   # red_counter(Cube)
    #blue_counter(Cube)
    #blue_counter(Cube)
    #red_clock(Cube)

    #print(green_corner_check_bottom(Cube, 3))

    green_info = green_cross_check(Cube, True)
    place_green_sides(Cube, green_info )
    green_corners_togo = green_corner_check_top(Cube)
    green_corners_togo = green_corner_check_bottom(Cube,green_corners_togo)
    green_corners_togo = green_corner_check_bottom_band(Cube, green_corners_togo)
    green_corners_togo = green_corner_check_top_band(Cube, green_corners_togo)
    green_corner_check_bottom_band(Cube, green_corners_togo)




    move_list_decoder(get_move_list())

    #Check green cross
    #Place green sides
    #corners on top
    #corners on bottom
    #corners on bottom band
    #corners on top band
    #corners on bottom band





    print(Cube)
    #print_hi('Josh')
