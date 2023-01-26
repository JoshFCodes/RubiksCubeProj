# Rubik's Cube Solver version 1.1
# Joshua Frechette @JoshFCodes
# 12.28.2022

#This file manages the intake of cube parameters,
#Aswell as performing all necissary input verification.
#See the lines below method declaration for notes on
#Implementation and functionality


#Blank Rubik's Cube
Cube = {"White": ["", "", "", "", "", "", "", "",""],
          "Green": ["", "", "", "", "", "", "", "",""],
          "Orange": ["", "", "", "", "", "", "", "",""],
          "Blue": ["", "", "", "", "", "", "", "",""],
          "Red": ["", "", "", "", "", "", "", "",""],
          "Yellow": ["", "", "", "", "", "", "", "",""]}

#List of valid inputs for color intake
validColors = ["G", "W", "R", "O", "Y", "B"]

def color_input_checker(color):
    #Check user input when user should be inputting a square's color

    for valid in validColors:
        if color == valid:
            return color

    return -1

def face_intake(face, code):

    #populates one face at a time by collecting input at each index.
    #contains input validation to ensure center color matches "face" color
    #on a rubik's cube, these are interchangable terms, therefore any discrepency
    #could hint to user input error...

    for position, square in enumerate(Cube[face]):

        quick_wish = color_input_checker(input())

        while quick_wish == -1:
            print("Please re-enter that square as the Capital first letter of it's color.")
            quick_wish = color_input_checker(input())

        if position == 4 and quick_wish != code:
            print(f'The center square should be {face}. Would you like to try re-entering this face?')
            print("Or just the previous square?")
            print("Enter '1' or '2' respectively")
            #FIXME implement way to reset face, and start from the beginning.
            #FIXME break to end, store a code, check the code, and send to appropriate spot.
            #FIXME implement way to rest square and start from the beginning.
            print("---CENTER COLOR ERROR---")

        Cube[face][position] = quick_wish

def init_Cube():

    #Welcomes and instructs user, calls face_intake 6 total times for the 6 faces.
    #Uses "quick_wish" to take user input at every step.

    quick_wish = ""

    print()
    print("Welcome to the Rubik's Cube Solver version 1.1")
    print("First, you will need to input the orientation of your cube.")
    print("Then, I will solve the cube and relay the steps.")

    while quick_wish != "OK":
        print("Enter 'OK' to continue")
        quick_wish = input()

    quick_wish = ""

    print()
    print("To input your cube, begin by facing the white center square towards you.")
    print("Ensure that the green center square is on the top. And keep it there until the last face.")
    print("Now, as if you were reading a book (left to right, top to bottom)")
    print("Input the color as the capital first letter. I.E. 'G' for green")

    face_intake("White", 'W')
    print("Now face the red center square towards you and begin entering colors.")
    face_intake("Red", 'R')
    print("Now face the yellow cetner square towards you and begin entering colors.")
    face_intake("Yellow", 'Y')
    print("Now face the Orange cetner square towards you and begin entering colors.")
    face_intake("Orange", 'O')
    print("With the orange center square still facing you, enter the colors on top.")
    face_intake("Green", 'G')
    print("Now, with the orange center square on top, face the blue center square towards you and enter the colors.")
    face_intake("Blue", 'B')

    print("Thank you! Sorry that took so long! Let's solve this thing.")

    print()
    print()
    print()
    return Cube





def print_hi(name):

    #FIXME Method to ensure nothing is broken in either this file or main file. NOT A PART OF THE FUNCTIONALITY
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.