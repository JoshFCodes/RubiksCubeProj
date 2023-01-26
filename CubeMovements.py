# Rubik's Cube Solver version 1.1
# Joshua Frechette @JoshFCodes
# 12.28.2022

#This file contains all the moves the software can make with a rubik's cube.
#Look to the line below method declaration for individual notes.
#green_clock contains notes for movement type methods
#each movement method contains a commented "code" which is what it prints to move_list

#FIXME stores codes and all methods should print codes to it.
move_list = []

def basic_move(Cube,color1,idx1,color2,idx2,color3,idx3,color4,idx4):
    #Function takes the cube, and 4 slices to be swapped.
    #The slices are represented as the color (of the center square, of their current side)
    #Along with the indecies of each square on that side.
    #The order in which the params are passed is vital, as the order is how methods calling basic_move can determine the move made.

    #Place holder lists neccisary for the swapping process
    limbo_slice1 = ["","",""]
    limbo_slice2 = ["","",""]

    #Store colors from second slice
    for position in range(0,3):
        limbo_slice1[position] = Cube[color2][idx2[position]]
    #Replace second slice colors with first slice colors
    for position in range(0, 3):
        Cube[color2][idx2[position]] = Cube[color1][idx1[position]]
    #Store colors from third slice
    for position in range(0,3):
        limbo_slice2[position] = Cube[color3][idx3[position]]
    #Replace third slice colors with stored second slice colors.
    for position in range(0, 3):
        Cube[color3][idx3[position]] = limbo_slice1[position]
    #Store colors from fourth slice
    for position in range(0,3):
        limbo_slice1[position] = Cube[color4][idx4[position]]
    #Replace fourth slice colors with third slice colors.
    for position in range(0, 3):
        Cube[color4][idx4[position]] = limbo_slice2[position]
    #Replace first slice colors with fourth slice colors.
    for position in range(0, 3):
        Cube[color1][idx1[position]] = limbo_slice1[position]

    #Swapping is now complete.

    return Cube

def clockwise_face_shift(face, Cube):
    #The face being turned needs to shift it's squares. This is a
    #consistent and predictable mapping of one position to another
    #Therefore this method simply grabs three relevent rows, and
    #pastes them to their new homes.
    snip1 = []
    snip1.append(Cube[face][6])
    snip1.append(Cube[face][3])
    snip1.append(Cube[face][0])

    snip2 = []
    snip2.append(Cube[face][7])
    snip2.append(Cube[face][4])
    snip2.append(Cube[face][1])

    snip3 = []
    snip3.append(Cube[face][8])
    snip3.append(Cube[face][5])
    snip3.append(Cube[face][2])

    Cube[face][0] = snip1[0]
    Cube[face][1] = snip1[1]
    Cube[face][2] = snip1[2]

    Cube[face][3] = snip2[0]
    Cube[face][4] = snip2[1]
    Cube[face][5] = snip2[2]

    Cube[face][6] = snip3[0]
    Cube[face][7] = snip3[1]
    Cube[face][8] = snip3[2]

    return

def counter_face_shift(face, Cube):

    #opposite mapping of clockwise_face_shift

    snip1 = []
    snip1.append(Cube[face][2])
    snip1.append(Cube[face][5])
    snip1.append(Cube[face][8])

    snip2 = []
    snip2.append(Cube[face][1])
    snip2.append(Cube[face][4])
    snip2.append(Cube[face][7])

    snip3 = []
    snip3.append(Cube[face][0])
    snip3.append(Cube[face][3])
    snip3.append(Cube[face][6])

    Cube[face][0] = snip1[0]
    Cube[face][1] = snip1[1]
    Cube[face][2] = snip1[2]

    Cube[face][3] = snip2[0]
    Cube[face][4] = snip2[1]
    Cube[face][5] = snip2[2]

    Cube[face][6] = snip3[0]
    Cube[face][7] = snip3[1]
    Cube[face][8] = snip3[2]

    return

def face_lifter(Cube, face, slice):

    #Unexpected bevahior arises during some slice transfers. This method is implemented where needed to
    #fix this behavior. It simply swaps two of the three squares using the face color and slice sequence passed to it.

    tmp_val = ""

    tmp_val = Cube[face][slice[2]]
    Cube[face][slice[2]] = Cube[face][slice[0]]
    Cube[face][slice[0]] = tmp_val

def green_clock(Cube):
    #"Clockwise" or "Counter" is determined as if you were facing the side that is being shifted.
    #These methods have 3 steps wherever necissary. These steps are to:
    #rotate the 4 relevant slices with basic_move
    #Shift the face's squares
    #utilize face_lifter to set final positions.
    basic_move(Cube,"White",[0,1,2],"Red",[0,1,2],"Yellow",[0,1,2],"Orange",[0,1,2])

    clockwise_face_shift("Green", Cube)

    move_list.append(1)

    return

def blue_counter(Cube):

    basic_move(Cube,"White",[6,7,8],"Red",[6,7,8],"Yellow",[6,7,8],"Orange",[6,7,8])

    counter_face_shift("Blue", Cube)

    move_list.append(12)

    return

def green_counter(Cube):

    basic_move(Cube,"White",[0,1,2],"Orange",[0,1,2],"Yellow",[0,1,2],"Red",[0,1,2])

    counter_face_shift("Green", Cube)

    move_list.append(2)
    return

def blue_clock(Cube):

    basic_move(Cube,"White",[6,7,8],"Orange",[6,7,8],"Yellow",[6,7,8],"Red",[6,7,8])

    clockwise_face_shift("Blue", Cube)

    move_list.append(11)

    return

def yellow_clock(Cube):

    basic_move(Cube,"Green",[2,5,8],"Red",[0,3,6],"Blue",[2,5,8],"Orange",[2,5,8])

    clockwise_face_shift("Yellow", Cube)

    face_lifter(Cube,"Blue",[2,5,8])
    face_lifter(Cube, "Red", [0, 3, 6])

    move_list.append(9)

    return

def white_counter(Cube):

    basic_move(Cube,"Green",[0,3,6],"Red",[2,5,8],"Blue",[0,3,6],"Orange",[0,3,6])

    counter_face_shift("White", Cube)
    face_lifter(Cube, "Red", [2,5,8])
    face_lifter(Cube,"Blue", [0,3,6])

    move_list.append(6)

    return

def yellow_counter(Cube):

    basic_move(Cube,"Green",[2,5,8],"Orange",[2,5,8],"Blue",[2,5,8],"Red",[0,3,6])

    counter_face_shift("Yellow", Cube)
    face_lifter(Cube, "Green", [2,5,8])
    face_lifter(Cube, "Red", [0, 3, 6])

    move_list.append(10)

    return

def white_clock(Cube):

    basic_move(Cube,"Green",[0,3,6],"Orange",[0,3,6],"Blue",[0,3,6],"Red",[2,5,8])

    clockwise_face_shift("White", Cube)

    face_lifter(Cube,"Green", [0, 3, 6])
    face_lifter(Cube, "Red", [2, 5, 8])

    move_list.append(5)

    return

def red_counter(Cube):

    basic_move(Cube,"Green",[0,1,2],"Yellow",[2,5,8],"Blue",[6,7,8],"White",[0,3,6])

    counter_face_shift("Red", Cube)
    face_lifter(Cube, "Blue", [6,7,8])
    face_lifter(Cube, "Green", [0,1,2])

    move_list.append(8)

    return

def orange_clock(Cube):

    basic_move(Cube,"Green",[6,7,8],"Yellow",[0,3,6],"Blue",[0,1,2],"White",[2,5,8])

    clockwise_face_shift("Orange", Cube)

    face_lifter(Cube, "Green", [6,7,8])
    face_lifter(Cube, "Blue", [0, 1, 2])

    move_list.append(3)

    return

def red_clock(Cube):

    basic_move(Cube,"Green",[0,1,2],"White",[0,3,6],"Blue",[6,7,8],"Yellow",[2,5,8])

    clockwise_face_shift("Red", Cube)

    face_lifter(Cube, "White", [0,3,6])
    face_lifter(Cube, "Yellow", [2,5,8])

    move_list.append(7)

    return

def orange_counter(Cube):

    basic_move(Cube,"Green",[6,7,8],"White",[2,5,8],"Blue",[0,1,2],"Yellow",[0,3,6])

    counter_face_shift("Orange", Cube)
    face_lifter(Cube, "Yellow", [0,3,6])
    face_lifter(Cube,"White", [2,5,8])

    move_list.append(4)

    return

def get_move_list():

    return move_list

def move_list_decoder(move_list):

    for move in move_list:

        if (move % 2) == 0:

            if move == 2:

                print("Green Counter-Clockwise")

            elif move == 4:

                print("Orange Counter-Clockwise")


            elif move == 6:

                print("White Counter-Clockwise")


            elif move == 8:

                print("Red Counter-Clockwise")

            elif move == 10:

                print("Yellow Counter-Clockwise")

            elif move == 12:

                print("Blue Counter-Clockwise")



        else:

            if move == 1:

                print("Green Clockwise")


            elif move == 3:

                print("Orange Clockwise")


            elif move == 5:

                print("White Clockwise")

            elif move == 7:

                print("Red Clockwise")

            elif move == 9:

                print("Yellow Clockwise")

            elif move == 11:

                print("Blue Clockwise")



