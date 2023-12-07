''' 
Program: EECS 210 Assignment 8
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 12/06/2023
Description: Define an Edge class to satisfy my needs for the proper representation of an edge
'''

class Edge:
    def __init__(self, x: str, y: str) -> None:
        self.x = x
        self.y = y

    # define the equal to operator to check for equivalence
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Edge):
            # if Edge object
            return {self.x, self.y} == {__value.x, __value.y}
        return {self.x, self.y} == __value

    # so I can use "for val in Edge" or "if in Edge"
    def __contains__(self, __value: object) -> bool:
        return __value == self.x or __value == self.y

    # so this can be used in a set/dictionary
    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    # string representation of an edge
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # return a string representation of an edge
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    # get the opposing vertex of a given vertex
    def getOpp(self, vertex: str) -> str:
        if self.x == vertex:
            return self.y
        return self.x
