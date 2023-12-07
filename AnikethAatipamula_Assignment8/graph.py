''' 
Program: EECS 210 Assignment 8
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: https://cp-algorithms.com/graph/euler_path.html
Name: Aniketh Aatipamula
Creation-Date: 12/06/2023
Description: Define a Graph class to find Euler and Hamilton circuits, 
also functions to print the graphs for the problems
'''

from typing import List, Set, Tuple
from itertools import combinations
from edge import Edge

Char = str
class InvalidGraph(BaseException): ...

class Graph:
    def __init__(
        self,
        vertices: Set[Char],
        edges: List[Tuple[Char, Char]]
    ) -> None:
        self.vertices = vertices
        self.edges = set(Edge(*vals) for vals in edges)

    # not specifically tied to this class, just convenience
    @staticmethod
    def is_odd(num: int) -> bool:
        return num % 2 != 0

    # get the number of verticies in our graph
    @property
    def num_vertices(self) -> int:
        return len(self.vertices)

    # get the vertices of odd degree
    @property
    def oddVertices(self) -> List[Char]:
        vertices = []
        # iterate through verticies to find the odd ones
        for vertex in self.vertices:
            deg = self.deg(vertex)
            # if the degree of the vertex is odd
            if self.is_odd(deg):
                vertices.append(vertex)
        # return our generated list
        return vertices

    # find if there is a Hamilton circuit using Dirac's Theorem
    @property
    def isHamiltonDirac(self) -> bool:
        # we can't use this if there are less than 3 vertices
        if self.num_vertices < 3:
            raise InvalidGraph
        # our check value is the number of vertices divided by two
        check = self.num_vertices/2
        for vertex in self.vertices:
            # it is maybe not a Hamilton circuit if the degree of the vertex is < the check
            if self.deg(vertex) < check:
                return False
        return True

    # find if there is a Hamilton circuit using Ore's Theorem
    @property
    def isHamiltonOre(self) -> bool:
        # we can't use this if there are less than 3 vertices
        if self.num_vertices < 3:
            raise InvalidGraph
        # generate all the combinations of vertices
        for comb in combinations(self.vertices, 2):
            # we don't care if they are adjacent
            if Edge(*comb) in self.edges:
                continue
            # our check value is the sum of the combo of vertices
            check = self.deg(comb[0]) + self.deg(comb[1])
            # it is maybe not a Hamilton circuit if the degree of the vertex is < the check
            if check < self.num_vertices:
                return False
        return True

    # use the algorithim to find the Euler Circuit
    # help from cp-algorithms.com
    def getEulerCircuit(self) -> List[Char]:
        # create a copy to save the state of the edges
        edgesCopy = self.edges.copy()
        # create a stack to push our vertices onto
        stack = [next(iter(self.vertices))]
        # create our final circuit
        circuit = []
        while stack:
            # while there are items on the stack grab the last one
            vertex = stack[-1]
            edges = self.edgesFor(vertex)
            # if there are no edges left we know that vertex should be added to our circuit
            if not edges:
                circuit.append(vertex)
                stack.pop()
                continue
            # otherwise we remove an edge on the vertex and add an adjacent one 
            # to our stack to keep removing from
            edge = edges.pop()
            self.edges.remove(edge) 
            vertex = edge.getOpp(vertex)
            stack.append(vertex)
        # restore the state from before this operation
        self.edges = edgesCopy
        return circuit

    # helper func to get all the edges for a given vertex
    def edgesFor(self, vertex: Char) -> Set[Edge]:
        edges = set()
        for edge in self.edges:
            if vertex in edge:
                edges.add(edge)
        return edges

    # helper func to get the degree of a given vertex
    def deg(self, vertex: Char) -> int:
        degree = 0
        for edge in self.edges:
            if vertex in edge:
                degree += 1
        return degree

# print problem one given a graph
def pproblemOne(title: str, graph: Graph): 
    print(title + ":")
    odd_vertices = graph.oddVertices
    if odd_vertices:
        print("Not a Euler Circuit, has odd vertices:",", ".join(odd_vertices))
    else:
        circuit = graph.getEulerCircuit()
        print("Has Euler circuit of:", "-".join(circuit))
    print()

# print problem two given a graph
def pproblemTwo(title: str, graph: Graph):
    print(title + ":")
    if graph.isHamiltonDirac:
        print("Is a Hamilton Circuit")
    else:
        print("Is maybe a Hamilton Circuit")
    print()

# print problem three given a graph
def pproblemThree(title: str, graph: Graph):
    print(title + ":")
    if graph.isHamiltonOre:
        print("Is a Hamilton Circuit")
    else:
        print("Is maybe a Hamilton Circuit")
    print()

