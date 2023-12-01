''' 
Program: EECS 210 Assignment 6
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: Nabeel Ahmad
Name: Aniketh Aatipamula
Creation-Date: 11/08/2023
Description: Run the main program
'''

# import necessary libraries/modules
from typing import List
from solve import Board

# set the div size
DIV_SIZE = 30

# list of all the puzzle files
puzzles = [
    'puzzle1.txt',
    'puzzle2.txt',
    'puzzle3.txt',
    'puzzle4.txt',
    'puzzle5.txt'
]

# main program
def main(filenames: List[str]) -> None:
    # for all the files given define a board, solve, and print it
    for name in filenames:
        board = Board.from_file(name)
        board.solve()
        print('-'*DIV_SIZE)

# run main
if __name__ == '__main__':
    main(puzzles)

