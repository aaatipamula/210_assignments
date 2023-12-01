''' 
Program: EECS 210 Assignment 6
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: Nabeel Ahmad
Name: Aniketh Aatipamula
Creation-Date: 11/08/2023
Description: Solve a sudoku puzzle, this will be stored in a class
'''

# typing stuff
from typing import List, Tuple

# type hints for coordinate objects
Coord = Tuple[int, int]

# Create a set of all the unique numbers 1-9
NUMS = set(num for num in range(1, 10))

# Indicator to end recursion
class EndRecursion(RecursionError): ...

class Board:
    def __init__(self, board: List[List[int]], name: str) -> None:
        # Store the board name and the board itself (a 2D list)
        self.board = board
        self.name = name

    # Create a Board class from a filename
    @classmethod
    def from_file(cls, file_name: str):
        "Create a board from a filename"
        # empty board
        board = []
        try: 
            # open the file
            with open(file_name) as file:
                # for every line in the file
                for line in file:
                    # remove newlines and whitespace
                    line = line.strip()
                    # split by space
                    line = line.split(" ")
                    # convert each item in the line of a file (row) to an integer
                    row = [int(char) if char.isdigit() else 0 for char in line]
                    #add to our board
                    board.append(row)
            # return the completed board
            return cls(board, file_name)
        # if the file isn't found exit the program
        except FileNotFoundError:
            print(file_name, "does not exist")
            exit(1)

    # set the value at some coordinate
    def _set_val(self, index: Coord, val: int) -> None:
        self.board[index[0]][index[1]] = val

    # get the value at some coordinate
    def _val(self, index: Coord) -> int:
        return self.board[index[0]][index[1]]

    # check if the value at an index has been filled
    def _is_empty(self, index: Coord) -> bool:
        return self._val(index) == 0

    # generate the next value to calculate unless we are past the end
    def _next(self, index: Coord) -> Coord:
        # increment by column
        indx = (index[0], index[1] + 1)
        # if the column is outside the board, we move to the next row
        if indx[1] > 8:
            indx = (indx[0] + 1, 0)
        # if the row is outside the board we end the recursion
        if indx[0] > 8:
            raise EndRecursion
        return indx

    # return the values in a row at an index
    def _row(self, index: Coord) -> set[int]:
        # get the row on the board the index corresponds with
        return set(self.board[index[0]])

    # return the values in a column at an index
    def _col(self, index: Coord) -> set[int]:
        # get the value of the column index for every row on the board
        return set(row[index[1]] for row in self.board)

    # return the values in a grid that the index is in
    def _grid(self, index: Coord) -> set[int]:
        # get the grid row we are in
        row = 3 * (index[0] // 3)
        # get the grid column we are in
        col = 3 * (index[1] // 3)
        # collect all the values in the 3x3 grid area
        grid_vals = set()
        for i in range(3):
            for j in range(3):
                grid_vals.add(self.board[row + i][col + j])
        return grid_vals

    # recursive solve
    def _solve(self, index: Coord) -> bool:
        # if we need to fill the value
        if self._is_empty(index):
            # get all the possible values we can fill
            vals = NUMS - self._col(index).union(self._row(index)).union(self._grid(index))
            # if there are no values we have filled something wrong
            if not vals:
                return False
            # check all the possible values
            for val in vals:
                # temporarily set the value at our current index
                self._set_val(index, val)
                # check to see if that is correct
                if self._solve(self._next(index)):
                    return True
                # if its not we set it back to what it was
                self._set_val(index, 0)
            # nothing worked so we go back
            return False
        # move to the next value if we don't need to fill it
        return self._solve(self._next(index))

    # print the board
    def print(self) -> None:
        "Print the state of the board."
        # print name
        print(self.name)
        # print each row
        for row in self.board:
            print(row)

    # public method
    def solve(self) -> None:
        "Use a recursive algorithim to solve the board, this will also print the finished result."
        # try to solve the board
        try:
            self._solve((0, 0))
            # we haven't solved the board if we haven't reached the end
            print(f"Cannot solve {self.name}")
        # if we encounter the end of the board we have solved it
        except EndRecursion:
            self.print()

