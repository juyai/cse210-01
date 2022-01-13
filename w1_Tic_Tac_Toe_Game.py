"""
Assignment: Tic-Tac-Toe
Author name: Yurinii Fuentes
"""

from turtle import position


def main():
    print()
    print('"Tic-Tac-Toe" Game')
    print('Welcome!')
    print()
    print('Intructions:')
    print("Alternate turns to complete a row, a column")
    print("or a diagonal with either three x's or three")
    print("o's drawn in the spaces of the grid of nine squares.")
    print()

    numbers = {"one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9}

    def grid():
        print(numbers["one"], "|", numbers["two"], "|", numbers["three"])
        print('-+-+-+-+-')
        print(numbers["four"], "|", numbers["five"], "|", numbers["six"])
        print('-+-+-+-+-')
        print(numbers["seven"], "|", numbers["eight"], "|", numbers["nine"])

    grid()

    def play_x():
        x_movement = int(input("X's turn to choose a square (1-9): "))
        if x_movement == 1:
            numbers["one"] = "X"
            grid()

        elif x_movement == 2:
            numbers["two"] = "X"
            grid()

        elif x_movement == 3:
            numbers["three"] = "X"
            grid()

        elif x_movement == 4:
            numbers["four"] = "X"
            grid()

        elif x_movement == 5:
            numbers["five"] = "X"
            grid()

        elif x_movement == 6:
            numbers["six"] = "X"
            grid()

        elif x_movement == 7:
            numbers["seven"] = "X"
            grid()

        elif x_movement == 8:
            numbers["eight"] = "X"
            grid()

        elif x_movement == 9:
            numbers["nine"] = "X"
            grid()
   
    def play_O():
        O_movement = int(input("O's turn to choose a square (1-9): "))
        if O_movement == 1:
            numbers["one"] = "O"
            grid()

        elif O_movement == 2:
            numbers["two"] = "O"
            grid()

        elif O_movement == 3:
            numbers["three"] = "O"
            grid()

        elif O_movement == 4:
            numbers["four"] = "O"
            grid()

        elif O_movement == 5:
            numbers["five"] = "O"
            grid()

        elif O_movement == 6:
            numbers["six"] = "O"
            grid()

        elif O_movement == 7:
            numbers["seven"] = "O"
            grid()

        elif O_movement == 8:
            numbers["eight"] = "O"
            grid()

        elif O_movement == 9:
            numbers["nine"] = "O"
            grid()

    play_x()
    play_O()

    while not ((numbers["one"] == "X" and numbers["two"] == "X" and numbers["three"] == "X") or \
        (numbers["one"] == "O" and numbers["two"] == "O" and numbers["three"] == "O") or \
        (numbers["four"] == "X" and numbers["five"] == "X" and numbers["six"] == "X") or \
        (numbers["four"] == "O" and numbers["five"] == "O" and numbers["six"] == "O") or \
        (numbers["seven"] == "X" and numbers["eight"] == "X" and numbers["nine"] == "X") or \
        (numbers["seven"] == "O" and numbers["eight"] == "O" and numbers["nine"] == "O") or \
        (numbers["one"] == "X" and numbers["four"] == "X" and numbers["seven"] == "X") or \
        (numbers["one"] == "O" and numbers["four"] == "O" and numbers["seven"] == "O") or \
        (numbers["two"] == "X" and numbers["five"] == "X" and numbers["eight"] == "X") or \
        (numbers["two"] == "O" and numbers["five"] == "O" and numbers["eight"] == "O") or \
        (numbers["three"] == "X" and numbers["six"] == "X" and numbers["nine"] == "X") or \
        (numbers["three"] == "O" and numbers["six"] == "O" and numbers["nine"] == "O") or \
        (numbers["one"] == "X" and numbers["five"] == "X" and numbers["nine"] == "X") or \
        (numbers["nine"] == "O" and numbers["five"] == "O" and numbers["nine"] == "O") or \
        (numbers["three"] == "X" and numbers["five"] == "X" and numbers["seven"] == "X") or \
        (numbers["three"] == "O" and numbers["five"] == "O" and numbers["seven"] == "O")):

        play_x()
        play_O()

    print('Thanks for playing')

if __name__ == "__main__":
    main()

