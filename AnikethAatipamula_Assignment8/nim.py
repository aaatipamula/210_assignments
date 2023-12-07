''' 
Program: EECS 210 Assignment 8
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 12/06/2023
Description: Run the main program
'''

from typing import Set, List
import random

# create a Piles class to accurately keep track of the piles and also gives helper functionality
class Piles:
    def __init__(self, first: int, second: int, third: int) -> None:
        self.first = first
        self.second = second
        self.third = third
        self.rep = (self.first, self.second, self.third)

    # make an iterable piles for compatibility with "for in"
    def __iter__(self):
        return iter(self.rep)

    # check for equality using "==" operator
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Piles):
            return set(self.rep) == set(__value.rep)
        return set(self.rep) == __value

    # indexable for compatibility with "object[int]"
    def __getitem__(self, key: int) -> int:
        if key < -3 or key > 2:
            raise IndexError
        return self.rep[key]

    # for compatibility with "for in" or "if in object"
    def __contains__(self, __value: object) -> bool:
        return __value in self.rep

    # to be used in sets
    def __hash__(self) -> int:
        return hash(self.first) + hash(self.second) + hash(self.third)

    # return a string representation
    def __str__(self) -> str:
        return f"Piles({self.first}, {self.second}, {self.third})"

    # return a string representation
    def __repr__(self) -> str:
        return f"Piles({self.first}, {self.second}, {self.third})"

    # create a copy with modified values
    def copy(self, indx: int, value: int):
        temp = list(self.rep)
        temp[indx] -= value
        if sum(temp):
            return Piles(*temp)
        return None

# Node class for our tree
class Node:
    def __init__(self, piles: Piles, is_max: bool = True) -> None:
        self.piles = piles
        self.is_max = is_max
        self.children: List[Node] = []
        self.baseval = None

    # get the last child in the children list
    @property
    def lastChild(self):
        return self.children[-1]

    # get the value in the tree
    @property
    def value(self) -> int:
        if self.baseval:
            return self.baseval
        if self.is_max:
            return max([child.value for child in self.children])
        return min([child.value for child in self.children])

    # check if there are moves beyond this one
    @property
    def hasNextMoves(self) -> bool:
        return len(self.children) != 0

    # add a node to the children
    def addNode(self, piles: Piles) -> None:
        self.children.append(Node(piles, not(self.is_max)))

    # set a basevalue for self.value, only used for leaf nodes
    def setBaseval(self) -> None:
        self.baseval = -1 if self.is_max else 1

    # get a string representation, get all the children string representations as well
    def __str__(self, level=0):
        ret = "\t"*level+repr(self.piles)+f" - Value: {self.value}"+"\n"
        ret = ret.expandtabs(tabsize=4)
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    # string representation
    def __repr__(self):
        return '<tree node representation>'

# Nim class to solve and keep track of Nim games
class Nim:
    def __init__(
        self, 
        p1: int, 
        p2: int, 
        p3: int, 
    ) -> None:
        self.piles = Piles(p1, p2, p3)
        self.root = None

    # generate a the possible next moves from a move
    @staticmethod
    def generatePiless(piles: Piles) -> Set[Piles]:
        # only keep the unique moves
        res = set()
        # generate all the possible moves
        for indx, pile in enumerate(piles):
            for num in range(1, pile + 1):
                copy = piles.copy(indx, num)
                if copy:
                    res.add(copy)
        return res

    # recursive create a gametree
    def _recSubTree(self, node: Node) -> None:
        piless = self.generatePiless(node.piles)
        # if there are no next moves
        if not piless:
            # this is a leaf node so set a baseval
            node.setBaseval()
            return
        # otherwise we iterate through all the possible moves and add them to the tree
        for p in piless:
            node.addNode(p)
            self._recSubTree(node.lastChild)

    # generate a tree if one does not exist
    def generateTree(self) -> None:
        # don't remake tree
        if self.root:
            raise Exception("Tree alread exists")
        self.root = Node(self.piles)
        # recusively generate tree
        self._recSubTree(self.root)

    # print the tree by printing the root node
    def printTree(self) -> None:
        print(self.root)

    # get the next move for player A using the gametree
    def playerANextMove(self, move: Node, is_first: bool):
        if is_first:
            return max(move.children, key=lambda x: x.value)
        return min(move.children, key=lambda x: x.value)

    # generate a random next move
    def playerBNextMove(self, move: Node, *args):
        return random.choice(move.children)

    # play a game with player A and B with a randomly chosen first player
    def play(self):
        # if there is no gametree we can't play
        if not self.root:
            raise Exception
        # decide if player A is first
        playerAFirst = bool(random.getrandbits(1))
        # grab our first move and the algorithim to use to generate our next move
        currMove = self.root
        nextMove = self.playerANextMove if playerAFirst else self.playerBNextMove
        # keep track of the current player
        currPlayer = "A" if playerAFirst else "B"
        # print our start move
        print(f"Start: {currMove.piles}")
        # keep playing until there are no valid next moves
        while currMove and currMove.hasNextMoves:
            # get our next move and swap the algorithim to the other player's
            currMove = nextMove(currMove, playerAFirst)
            nextMove = self.playerANextMove if nextMove == self.playerBNextMove else self.playerBNextMove
            # print the next move
            print(f"Player {currPlayer}: {currMove.piles}")
            # change the current player
            currPlayer = "B" if currPlayer == "A" else "A"
        # determine the winner based on who went first
        if playerAFirst:
           winner = "A" if currMove.value == 1 else "B"
        else:
            winner = "A" if currMove.value == -1 else "B"
        # print the current winner
        print(f"{winner} wins!")
        return winner

    # run self.play 100 times and get stats
    def sim(self, divsize = 30):
        # print a div
        DIV = "-"*divsize
        # keep track of how many times A and B win
        ACount = 0
        BCount = 0
        # repeat 100 times
        for _ in range(100):
            print(DIV)
            # get the winner
            winner = self.play()
            # update the count
            if winner == "A":
                ACount += 1
                continue
            BCount += 1

        # write out the stats
        stats = (
            "Stats:\n"
            f"Player A won {ACount}/100 times or {(ACount/100)*100:0.2f}%"
            f"\nPlayer B won {BCount}/100 times or {(BCount/100)*100:0.2f}%"
        )

        # print out the stats
        print(DIV)
        print(stats)

# print problem four a and b
def printFourAB(title: str, val1: int, val2: int, val3: int) -> Nim:
    print(title + ":")
    nimSolver = Nim(val1, val2, val3)
    nimSolver.generateTree()
    nimSolver.printTree()
    return nimSolver

# print problem four c
def printFourC(title: str, nim: Nim) -> None:
    print(title + ":")
    nim.sim()

