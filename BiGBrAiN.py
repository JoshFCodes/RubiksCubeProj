# Rubik's Cube Solver version 1.1
# Joshua Frechette @JoshFCodes
# 12.28.2022

from Pieces import *
from CubeMovements import *
from SolvingAlgorithms import *

#My Process for solving a Rubik's Cube has three steps.
#Step one is to solve the top slice,
#Step two is to solve the middle slice,
#Step three is to solve the bottom slice.
#This file goes through each of those steps distinctly,
#and each step contains patterns and algorithms inherent to it.
#Look to the line below method declarations for notes.

adj_finder_for_sides = {"White" : {1 : [3, "Green"] , 3 : [5, "Red"] , 5 : [3, "Orange"] , 7 : [3, "Blue"], "opposite" : "Yellow"},
                        "Blue" : {1 : [7, "Orange"] , 3 : [7, "White"] , 5 : [7, "Yellow"] , 7 : [7, "Red"], "opposite" : "Green"},
                        "Yellow" : {1 : [5, "Green"] , 3 : [5, "Orange"] , 5 : [3, "Red"] , 7 : [5, "Blue"], "opposite" : "White"},
                        "Orange" : {1 : [7, "Green"] , 3 : [5, "White"] , 5 : [3, "Yellow"] , 7 : [1, "Blue"], "opposite" : "Red"},
                        "Red" : {1 : [1, "Green"] , 3 : [5, "Yellow"] , 5 : [3, "White"] , 7 : [7, "Blue"], "opposite" : "Orange"}}


#To get to White from Yellow is 2 counter turns of the blue face
#To get to White from Orange is 1 counter turn of the blue face
movement_helper_bottom_band = {"White" : {"Yellow" : [2, "counter", "Blue"], "Orange" : [1, "counter", "Blue"], "Red" : [1, "clock", "Blue"]},
                               "Yellow" : {"White" : [2, "counter", "Blue"], "Orange" : [1, "clock", "Blue"], "Red" : [1, "counter", "Blue"]},
                               "Orange" : {"Red" : [2, "counter", "Blue"], "Yellow" : [1, "counter", "Blue"], "White" : [1, "clock", "Blue"]},
                               "Red" : {"Orange" : [2, "counter", "Blue"], "Yellow" : [1, "clock", "Blue"], "White" : [1, "counter", "Blue"]}}



#----------------
#Step One: Solve the top layer

def green_cross_check(Cube, can_green_turn):

    can_turn_green = can_green_turn
    green_cross_pos = [1, 3, 5, 7]
    other_color = ''
    blue_face_rots = []
    i = 0
    greens_togo = 4

    while i < 4:

        position = green_cross_pos[i]

        if Cube["Green"][position] == 'G':

#----------------------------------------------------------------------------------------

            if position == 1:
                if Cube["Red"][1] == 'R':

                    can_turn_green = False
                    greens_togo -= 1

                    i += 1

                else:
                    other_color = Cube["Red"][1]

                #Now, we will move the piece as needed, to its home faces.
                #If we can rotate green we will, if we can't, we will use some predefined movements to
                #relocate the piece.

                if other_color == 'W':

                    if can_turn_green:

                        green_counter(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["clock", 1]
                        rearange_green_side("Red", blue_face_rots, "White", Cube)

                        greens_togo -= 1

                elif other_color == 'O':

                    if can_turn_green:

                        green_counter(Cube)
                        green_counter(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["clock", 2]
                        rearange_green_side("Red", blue_face_rots, "Orange", Cube)

                        greens_togo -= 1

                elif other_color == 'Y':

                    if can_turn_green:

                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 1]
                        rearange_green_side("Red", blue_face_rots, "Yellow", Cube)

                        greens_togo -= 1


#------------------------------------------------------------------------------------------


            if position == 3:

                if Cube["White"][1] == 'W':

                    can_turn_green = False
                    greens_togo -= 1

                    i += 1

                else:

                    other_color = Cube["White"][1]

                if other_color == 'R':

                    if can_turn_green:

                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 1]
                        rearange_green_side("White", blue_face_rots, "Red", Cube)

                        greens_togo -= 1

                elif other_color == 'Y':

                    if can_turn_green:

                        green_clock(Cube)
                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 2]
                        rearange_green_side("White", blue_face_rots, "Yellow", Cube)

                        greens_togo -= 1

                elif other_color == 'O':

                    if can_turn_green:

                        green_counter(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["clock", 1]
                        rearange_green_side("White", blue_face_rots, "Orange", Cube)

                        greens_togo -= 1



#---------------------------------------------------------------------------------------------

            if position == 5:

                if Cube["Yellow"][1] == 'Y':

                    can_turn_green = False
                    greens_togo -= 1

                    i += 1

                else:

                    other_color = Cube["Yellow"][1]

                if other_color == 'O':

                    if can_turn_green:

                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 1]
                        rearange_green_side("Yellow", blue_face_rots, "Orange", Cube)

                        greens_togo -= 1

                if other_color == 'W':

                    if can_turn_green:

                        green_clock(Cube)
                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 2]
                        rearange_green_side("Yellow", blue_face_rots, "White", Cube)

                        greens_togo -= 1

                if other_color == 'R':

                    if can_turn_green:

                        green_counter(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["clock", 1]
                        rearange_green_side("Yellow", blue_face_rots, "Red", Cube)

                        greens_togo -= 1


#----------------------------------------------------------------------------------------------

            if position == 7:

                if Cube["Orange"][1] == 'O':

                    can_turn_green = False
                    greens_togo -= 1

                    i += 1

                else:

                    other_color = Cube["Orange"][1]

                if other_color == 'W':

                    if can_turn_green:

                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 1]
                        rearange_green_side("Orange", blue_face_rots, "White", Cube)

                        greens_togo -= 1


                if other_color == 'R':

                    if can_turn_green:

                        green_clock(Cube)
                        green_clock(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["counter", 2]
                        rearange_green_side("Orange", blue_face_rots, "White", Cube)

                        greens_togo -= 1

                if other_color == 'Y':

                    if can_turn_green:

                        green_counter(Cube)

                        i = 0

                    else:

                        blue_face_rots = ["clock", 1]
                        rearange_green_side("Orange", blue_face_rots, "Yellow", Cube)

                        greens_togo -= 1


        else:

            i += 1


        #FIXME
        print(i)
        print(can_turn_green, "-----", greens_togo)
    return([can_turn_green, greens_togo])

def place_green_sides(Cube, green_info):

    possible_places = [["Blue", "Orange", "Yellow", "White", "Red"], [1, 3, 5, 7]]

    can_turn_grenn = green_info[0]
    greens_togo = green_info[1]

    #when I solve a green, subtract greens_togo

    while greens_togo:

        for face in possible_places[0]:

            for pos in possible_places[1]:

                if Cube[face][pos] == 'G':

                    #FIXME
                    print("Found a green square", greens_togo)

                    other_face = adj_finder_for_sides[face][pos][1]
                    other_pos = adj_finder_for_sides[face][pos][0]
                    other_color = Cube[other_face][other_pos]

                    if face == "Blue":

                        green_facing_blue(Cube, face, pos, other_face, other_pos, other_color)

                        greens_togo -= 1

                    else:

                        home_face = square_to_face(other_color)

                        #is the green on the bottom or sides?

                        # bottom and left neighbor
                        if pos == 7 and (adj_finder_for_sides[face][3][1] == home_face):

                            movement_decider_maker(Cube, face, "clock")
                            movement_decider_maker(Cube, home_face, "counter")
                            movement_decider_maker(Cube, face, "counter")

                            greens_togo -= 1


                        # bottom and right neighbor
                        elif pos == 7 and (adj_finder_for_sides[face][5][1] == home_face):

                            movement_decider_maker(Cube, face, "counter")
                            movement_decider_maker(Cube, home_face, "clock")
                            movement_decider_maker(Cube, face, "clock")

                            greens_togo -= 1


                        #bottom and opposite
                        elif pos == 7:

                            blue_clock(Cube)
                            movement_decider_maker(Cube, adj_finder_for_sides[face][5][1], "counter")
                            movement_decider_maker(Cube, adj_finder_for_sides[face]["opposite"], "clock")
                            movement_decider_maker(Cube, adj_finder_for_sides[face][5][1], "clock")

                            greens_togo -= 1


                        #side and already at home face
                        elif pos == 3 and (adj_finder_for_sides[face][3][1] == home_face):

                            movement_decider_maker(Cube, home_face, "counter")

                            greens_togo -= 1

                        elif pos == 5 and (adj_finder_for_sides[face][5][1] == home_face):

                            movement_decider_maker((Cube, home_face, "clock"))

                            greens_togo -= 1


                        #side and opposite
                        elif pos == 3 and (square_to_face(other_color) == adj_finder_for_sides[face]["opposite"]):

                            movement_decider_maker(Cube, adj_finder_for_sides[face][pos][1], clock_counter_side_pieces(5, 7))
                            blue_counter(Cube)
                            movement_decider_maker(Cube, home_face, "clock")
                            movement_decider_maker(Cube, home_face, "clock")
                            movement_decider_maker(Cube, adj_finder_for_sides[face][pos][1], clock_counter_side_pieces(7, 5))

                        elif pos == 5 and (square_to_face(other_color) == adj_finder_for_sides[face]["opposite"]):

                            movement_decider_maker(Cube, adj_finder_for_sides[face][pos][1], clock_counter_side_pieces(3, 7))
                            blue_clock(Cube)
                            movement_decider_maker(Cube, home_face, "clock")
                            movement_decider_maker(Cube, home_face, "clock")
                            movement_decider_maker(Cube, adj_finder_for_sides[face][pos][1], clock_counter_side_pieces(7, 3))

                            greens_togo -= 1

                        elif pos == 3:

                            movement_decider_maker(Cube, face, clock_counter_side_pieces(3, 1))
                            movement_decider_maker(Cube, face, clock_counter_side_pieces(1, 5))
                            movement_decider_maker(Cube, home_face, clock_counter_side_pieces(3, 1))
                            movement_decider_maker(Cube, face, clock_counter_side_pieces(3, 1))
                            movement_decider_maker(Cube, face, clock_counter_side_pieces(1, 7))

                            greens_togo -= 1

                        elif pos == 5:

                            movement_decider_maker(Cube, face, clock_counter_side_pieces(3, 1))
                            movement_decider_maker(Cube, face, clock_counter_side_pieces(1, 5))
                            movement_decider_maker(Cube, home_face, clock_counter_side_pieces(5, 1))
                            movement_decider_maker(Cube, face, clock_counter_side_pieces(3, 1))
                            movement_decider_maker(Cube, face, clock_counter_side_pieces(1, 7))

                            greens_togo -= 1


    return

def green_corner_check_top(Cube):

    green_corners = [0, 2, 6, 8]
    i = 0
    corners_togo = 4

    while i < 4:

        pos = green_corners[i]

        if Cube["Green"][pos] == 'G':

            if pos == 2 and Cube["Yellow"][2] == 'Y':

                corner_togo -= 1
                i += 1

            elif pos == 0 and Cube["White"][0] == 'W':

                corners_togo -= 1
                i += 1

            elif pos == 6 and Cube["White"][2] == 'W':

                corners_togo -= 1
                i += 1

            elif pos == 8 and Cube["Yellow"][0] == 'Y':

                corners_togo -= 1
                i += 1

#--------------------------------------------------------------------

            elif pos == 2 and Cube["Yellow"][2] == 'R':

                red_counter(Cube)
                blue_counter(Cube)
                red_clock(Cube)
                blue_clock(Cube)
                white_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)

                i = 0
                corners_togo = 4

            elif pos == 2 and Cube["Yellow"][2] == 'W':

                red_counter(Cube)
                blue_counter(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                orange_counter(Cube)
                blue_clock(Cube)
                orange_clock(Cube)

                i = 0
                corners_togo = 4

            elif pos == 2 and Cube["Yellow"][2] == 'O':

                red_counter(Cube)
                blue_counter(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)

                i = 0
                corners_togo = 4

#----------------------------------------------------------------------------------

            elif pos == 0 and Cube["White"][0] == 'O':

                red_clock(Cube)
                blue_clock(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)

                i = 0
                corners_togo = 4

            elif pos == 0 and Cube["White"][0] == 'R':

                red_clock(Cube)
                blue_clock(Cube)
                red_counter(Cube)
                blue_counter(Cube)
                yellow_clock(Cube)
                blue_counter(Cube)
                yellow_clock(Cube)

                i = 0
                corners_togo = 4

            elif pos == 0 and Cube["White"][0] == 'Y':

                red_clock(Cube)
                blue_clock(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                orange_clock(Cube)
                blue_counter(Cube)
                orange_counter(Cube)

                i = 0
                corners_togo = 4

#-----------------------------------------------------------

            elif pos == 6 and Cube["White"][2] == 'O':

                orange_counter(Cube)
                blue_counter(Cube)
                orange_clock(Cube)
                blue_clock(Cube)
                yellow_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)

                i = 0
                corners_togo = 4

            elif pos == 6 and Cube["White"][2] == 'Y':

                orange_counter(Cube)
                blue_counter(Cube)
                orange_clock(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                red_clock(Cube)

                i = 0
                corners_togo = 4

            elif pos == 6 and Cube["White"][2] == 'Y':

                orange_counter(Cube)
                blue_counter(Cube)
                orange_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)

                i = 0
                corners_togo = 4

#---------------------------------------------------------------

            elif pos == 8 and Cube["Yellow"][0] == 'W':

                orange_clock(Cube)
                blue_clock(Cube)
                orange_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                red_counter(Cube)

                i = 0
                corners_togo = 4

            elif pos == 8 and Cube["Yellow"][0] == 'O':

                orange_clock(Cube)
                blue_clock(Cube)
                orange_counter(Cube)
                blue_counter(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)

                i = 0
                corners_togo = 4

            elif pos == 8 and Cube["Yellow"][0] == 'R':

                orange_clock(Cube)
                blue_clock(Cube)
                orange_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)

                i = 0
                corners_togo = 4

        else:

            i += 1

    return(corners_togo)

def green_corner_check_bottom(Cube, corners_togo):

    i = 0
    blue_corners = [0, 2, 6, 8]

    print('letsa go!')
    while i < 4 and corners_togo:

        pos = blue_corners[i]

        if Cube["Blue"][pos] == 'G':


            if pos == 8 and Cube["Yellow"][8] == 'W':

                white_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 8 and Cube["Yellow"][8] == 'Y':

                orange_clock(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                orange_counter(Cube)
                blue_clock(Cube)
                orange_clock(Cube)
                blue_counter(Cube)
                orange_counter(Cube)

                corners_togo -= 1

            elif pos == 8 and Cube["Yellow"][8] == 'O':

                white_clock(Cube)
                blue_clock(Cube)
                white_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 8 and Cube["Yellow"][8] == 'R':

                blue_counter(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                red_clock(Cube)

                i = 0
                corners_togo -= 1

#-------------------------------------------------------------------------------

            elif pos == 6 and Cube["White"][6] == 'W':

                orange_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                orange_clock(Cube)
                blue_counter(Cube)
                orange_counter(Cube)
                blue_clock(Cube)
                orange_clock(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 6 and Cube["White"][6] == 'R':

                white_counter(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                white_clock(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                red_counter(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 6 and Cube["White"][6] == 'Y':

                blue_counter(Cube)
                red_counter(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                red_clock(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 6 and Cube["White"][6] == 'O':

                blue_counter(Cube)
                blue_counter(Cube)
                orange_clock(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                orange_counter(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)

                i = 0
                corners_togo -= 1

#----------------------------------------------------------------

            elif pos == 2 and Cube["Yellow"][6] == 'O':

                orange_clock(Cube)
                blue_counter(Cube)
                orange_counter(Cube)
                blue_clock(Cube)
                yellow_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 2 and Cube["Yellow"][6] == 'Y':

                red_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                red_clock(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 2 and Cube["Yellow"][6] == 'W':

                white_clock(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                white_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 2 and Cube["Yellow"][6] == 'R':

                white_counter(Cube)
                blue_counter(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)
                blue_clock(Cube)
                white_clock(Cube)

                i = 0
                corners_togo -= 1

#----------------------------------------------------------------

            elif pos == 0 and Cube["White"][8] == 'W':

                red_clock(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                red_counter(Cube)
                blue_clock(Cube)
                red_clock(Cube)
                blue_counter(Cube)
                red_counter(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 0 and Cube["White"][8] == 'R':

                blue_counter(Cube)
                yellow_clock(Cube)
                blue_counter(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)

                i = 0
                corners_togo -=1

            elif pos == 0 and Cube["White"][8] == 'Y':

                yellow_counter(Cube)
                blue_clock(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)
                blue_counter(Cube)
                yellow_counter(Cube)
                blue_clock(Cube)
                yellow_clock(Cube)

                i = 0
                corners_togo -= 1

            elif pos == 0 and Cube["White"][8] == 'O':

                orange_counter(Cube)
                blue_clock(Cube)
                orange_clock(Cube)
                blue_counter(Cube)
                white_clock(Cube)
                blue_counter(Cube)
                white_counter(Cube)

                i = 0
                corners_togo -= 1

        else:

            i += 1

    return(corners_togo)

def green_corner_check_bottom_band(Cube, corners_togo):

    blue_corners = [0, 2, 6, 8]
    what_blue_maps2 = [["White", 8, "Orange", 6],
                       ["Orange", 8, "Yellow", 6],
                       ["Red", 8, "White", 6],
                       ["Yellow", 8, "Red", 6]]

    i = 0

    while i < 4 and corners_togo:

        green_square = []
        other_side = []
        bottom_square = []

        pos = blue_corners[i]

        if Cube[what_blue_maps2[i][0]][what_blue_maps2[i][1]] != 'G':
            other_side.append(Cube[what_blue_maps2[i][0]][what_blue_maps2[i][1]])


            green_square.append(Cube[what_blue_maps2[i][2]][what_blue_maps2[i][3]])
            green_square.append(what_blue_maps2[i][2])
            green_square.append(what_blue_maps2[i][3])
        else:
            other_side.append(Cube[what_blue_maps2[i][2]][what_blue_maps2[i][3]])

            green_square.append(Cube[what_blue_maps2[i][0]][what_blue_maps2[i][1]])
            green_square.append(what_blue_maps2[i][0])
            green_square.append(what_blue_maps2[i][1])


        bottom_square = Cube["Blue"][pos]

        print(bottom_square)
        print(green_square)
        print(other_side)

        if other_side[0] != 'B' and bottom_square != 'B'and green_square[0] != 'B':

            goal_face = adj_finder_for_sides[square_to_face(other_side[0])]["opposite"]



                #green in bottom left and incorrect face for placement
            if green_square[2] == 8 and goal_face != green_square[1]:

                for turn in range(movement_helper_bottom_band[goal_face][green_square[1]][0]):
                    movement_decider_maker(Cube, "Blue", movement_helper_bottom_band[goal_face][green_square[1]])

                movement_decider_maker(Cube, square_to_face(other_side[0]), "counter")
                movement_decider_maker(Cube, "Blue", "clock")
                movement_decider_maker(Cube, square_to_face(other_side[0]), "clock")
                i = 0
                corners_togo -= 1

                green_corner_check_bottom(Cube, corners_togo)



                #green in bottom left and correct face for placement
            elif green_square[2] == 8:

                movement_decider_maker(Cube, square_to_face(other_side[0]), "counter")
                movement_decider_maker(Cube, "Blue", "clock")
                movement_decider_maker(Cube, square_to_face(other_side[0]), "clock")

                i = 0
                corners_togo -= 1

                green_corner_check_bottom(Cube, corners_togo)
            elif green_square[2] == 6 and goal_face != green_square[1]:

                for turn in range(movement_helper_bottom_band[goal_face][green_square[1]][0]):
                    movement_decider_maker(Cube, "Blue", movement_helper_bottom_band[goal_face][green_square][1])

                movement_decider_maker(Cube, square_to_face(other_side[0]), "counter")
                movement_decider_maker(Cube, "Blue", "clock")
                movement_decider_maker(Cube, square_to_face(other_side[0]), "clock")
                i = 0
                corners_togo -= 1

                green_corner_check_bottom(Cube, corners_togo)

                #green in bottom right and correct face
            elif green_square[2] == 6:

                movement_decider_maker(Cube, square_to_face(other_side[0]), "clock")
                movement_decider_maker(Cube, "Blue", "counter")
                movement_decider_maker(Cube, square_to_face(other_side[0]), "counter")

                i = 0
                corners_togo -= 1

                green_corner_check_bottom(Cube, corners_togo)





        else:

            i += 1

def green_corner_check_top_band(Cube, corners_togo):

    green_corners = [0, 2, 6, 8]
    what_green_maps2 = [["White", 0, "Red", 2],
                       ["Red", 0, "Yellow", 2],
                       ["Orange", 0, "White", 2],
                       ["Yellow", 0, "Orange", 2]]

    i = 0

    while i < 4 and corners_togo:

        green_square = []
        other_side = []
        bottom_square = []

        pos = green_corners[i]

        #if green at pos is not G, Then we grab other two, so three squares tot, green and two nons
        #based off the pos of green, either 0 or 2, and

        if Cube["Green"][pos] != 'G':

            if Cube[what_green_maps2[i][0]][what_green_maps2[i][1]] != 'G':
                other_side.append(Cube[what_green_maps2[i][0]][what_green_maps2[i][1]])

                green_square.append(Cube[what_green_maps2[i][2]][what_green_maps2[i][3]])
                green_square.append(what_green_maps2[i][2])
                green_square.append(what_green_maps2[i][3])
            else:
                other_side.append(Cube[what_green_maps2[i][2]][what_green_maps2[i][3]])

                green_square.append(Cube[what_green_maps2[i][0]][what_green_maps2[i][1]])
                green_square.append(what_green_maps2[i][0])
                green_square.append(what_green_maps2[i][1])








#----------------
#Step Two: Solve the middle layer
#----------------
#Step Three: Solve the bottom layer

def clock_counter_side_pieces(pos, desired_pos):

    if (pos == 3 and desired_pos == 7) or (pos == 5 and desired_pos == 1) or (pos == 7 and desired_pos == 5) or (pos == 1 and desired_pos == 3):

        return "counter"

    elif (pos == 3 and desired_pos == 1) or (pos == 5 and desired_pos == 7) or (pos == 7 and desired_pos == 3) or (pos == 1 and desired_pos == 5):

        return "clock"



def movement_decider_maker(Cube, face, direction):

    if direction == "clock":

        if face == "Yellow":

            yellow_clock(Cube)

        elif face == "White":

            white_clock(Cube)

        elif face == "Red":

            red_clock(Cube)

        elif face == "Orange":

            orange_clock(Cube)

        elif face == "Blue":

            blue_clock(Cube)

        elif face == "Green":

            green_clock(Cube)


    else:

        if face == "Yellow":

            yellow_counter(Cube)

        elif face == "White":

            white_counter(Cube)

        elif face == "Red":

            red_counter(Cube)

        elif face == "Orange":

            orange_counter(Cube)

        elif face == "Blue":

            blue_counter(Cube)

        elif face == "Green":

            green_counter(Cube)


def square_to_face(color):

    if color == 'G':

        return "Green"

    elif color == 'O':

        return "Orange"

    elif color == 'R':

        return "Red"

    elif color == 'B':

        return "Blue"

    elif color == 'Y':

        return "Yellow"

    elif color == 'W':

        return "White"


def face_to_square(face):

    if face == "Green":

        return 'G'

    elif face == "Orange":

        return 'O'

    elif face == "White":

        return 'W'

    elif face == "Red":

        return 'R'

    elif face == "Yellow":

        return 'Y'

    elif face == "Blue":

        return 'B'






