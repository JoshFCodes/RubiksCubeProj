# Rubik's Cube Solver version 1.1
# Joshua Frechette @JoshFCodes
# 12.28.2022

from CubeMovements import *

def rearange_green_side(starting, blue_face_rots, ending, Cube):

    if starting == "Red":

        red_clock(Cube)
        red_clock(Cube)

        if blue_face_rots[0] == "clock":
            for i in range(0, blue_face_rots[1]):
                blue_clock(Cube)

        else:
            for i in range(0, blue_face_rots[1]):
                blue_counter(Cube)

        if ending == "Orange":

            orange_clock(Cube)
            orange_clock(Cube)

        elif ending == "White":

            white_clock(Cube)
            white_clock(Cube)

        elif ending == "Yellow":

            yellow_clock(Cube)
            yellow_clock(Cube)

#------------------------------------------------------------------------

    elif starting == "White":

        white_clock(Cube)
        white_clock(Cube)

        if blue_face_rots[0] == "clock":
            for i in range(0, blue_face_rots[1]):
                blue_clock(Cube)

        else:
            for i in range(0, blue_face_rots[1]):
                blue_counter(Cube)

    if ending == "Orange":

        orange_clock(Cube)
        orange_clock(Cube)

    elif ending == "Red":

        red_clock(Cube)
        red_clock(Cube)

    elif ending == "Yellow":

        yellow_clock(Cube)
        yellow_clock(Cube)

#----------------------------------------------------------------------

    elif starting == "Yellow":

        yellow_clock(Cube)
        yellow_clock(Cube)

        if blue_face_rots[0] == "clock":
            for i in range(0, blue_face_rots[1]):
                blue_clock(Cube)

        else:
            for i in range(0, blue_face_rots[1]):
                blue_counter(Cube)

        if ending == "Orange":

            orange_clock(Cube)
            orange_clock(Cube)

        elif ending == "White":

            white_clock(Cube)
            white_clock(Cube)

        elif ending == "Red":

            red_clock(Cube)
            red_clock(Cube)
#-----------------------------------------------------------------------

    elif starting == "Orange":

        orange_clock(Cube)
        orange_clock(Cube)

        if blue_face_rots[0] == "clock":
            for i in range(0, blue_face_rots[1]):
                blue_clock(Cube)

        else:
            for i in range(0, blue_face_rots[1]):
                blue_counter(Cube)

        if ending == "Yellow":

            yellow_clock(Cube)
            yellow_clock(Cube)

        elif ending == "White":

            white_clock(Cube)
            white_clock(Cube)

        elif ending == "Red":

            red_clock(Cube)
            red_clock(Cube)



def green_facing_blue(Cube, face, pos, other_face, other_pos, other_color):


    if other_color == "Orange":

        if other_face == "Orange":

            orange_clock(Cube)
            orange_clock(Cube)

        elif other_face == "White":

            blue_clock(Cube)
            orange_clock(Cube)
            orange_clock(Cube)

        elif other_face == "Red":

            blue_clock(Cube)
            blue_clock(Cube)
            orange_clock(Cube)
            orange_clock(Cube)

        elif other_face == "Yellow":

            blue_counter(Cube)
            orange_clock(Cube)
            orange_clock(Cube)

#---------------------------------------------------------------------

    elif other_color == "White":

        if other_face == "Orange":

            blue_counter(Cube)
            white_clock(Cube)
            white_clock(Cube)

        elif other_face == "White":

            white_clock(Cube)
            white_clock(Cube)

        elif other_face == "Red":

            blue_clock(Cube)
            white_clock(Cube)
            white_clock(Cube)

        elif other_face == "Yellow":

            blue_clock(Cube)
            blue_clock(Cube)
            white_clock(Cube)
            white_clock(Cube)

#------------------------------------------------------

    elif other_color == "Red":

        if other_face == "Orange":

            blue_clock(Cube)
            blue_clock(Cube)
            red_clock(Cube)
            red_clock(Cube)

        elif other_face == "White":

            blue_counter(Cube)
            red_clock(Cube)
            red_clock(Cube)

        elif other_face == "Red":

            red_clock(Cube)
            red_clock(Cube)

        elif other_face == "Yellow":

            blue_clock(Cube)
            red_clock(Cube)
            red_clock(Cube)

#------------------------------------------------------------

    elif other_color == "Yellow":

        if other_face == "Orange":

            blue_clock(Cube)
            yellow_clock(Cube)
            yellow_clock(Cube)

        elif other_face == "White":

            blue_clock(Cube)
            blue_clock(Cube)
            yellow_clock(Cube)
            yellow_clock(Cube)

        elif other_face == "Red":

            blue_counter(Cube)
            yellow_clock(Cube)
            yellow_clock(Cube)

        elif other_face == "Yellow":

            yellow_clock(Cube)
            yellow_clock(Cube)


    return