''' 
Program: EECS 210 Assignment 8
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 12/06/2023
Description: Define all the graphs we have to solve for
'''

from graph import Graph

#################
# Euler  Graphs #
#################

# Debug 1
vertices = {'a', 'b', 'c', 'd', 'e'}
edges = [('a', 'e'), ('a', 'b'), ('b', 'e'), ('e', 'd'), ('e', 'c'), ('c', 'd'), ('d', 'e')]
ProblemOneG1 = Graph(vertices, edges)

# Debug 2
vertices = {'a', 'b', 'c', 'd', 'e'}
edges = [('a', 'e'), ('a', 'b'), ('b', 'e'), ('e', 'd'), ('e', 'c'), ('c', 'd'), ('d', 'e'), ('a', 'd'), ('c', 'b')]
ProblemOneG2 = Graph(vertices, edges)

# Debug 3
vertices = {'a', 'b', 'c', 'd', 'e'}
edges = [('a', 'b'), ('a', 'd'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e'), ('b', 'e')]
ProblemOneG3 = Graph(vertices, edges)

# Bridge Graph
vertices = {'a', 'b', 'c', 'd'}
edges = [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'a'), ('d', 'b')]
ProblemOneBridge = Graph(vertices, edges)

# Test Graph
vertices = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
edges = [('a', 'd'), ('a', 'b'), ('b', 'e'), ('b', 'c'), ('b', 'd'), ('c', 'f'), ('d', 'g'), ('d', 'e'), ('e', 'h'), ('e', 'f'), ('f', 'i'), ('g', 'h'), ('h', 'i'), ('h', 'f')]
ProblemOneTest = Graph(vertices, edges)

####################
# Hamilton  Graphs #
####################

# Debug 1
vertices_g1 = {'a', 'b', 'c', 'd', 'e'}
edges_g1 = [('a', 'e'), ('a', 'b'), ('a', 'c'), ('b', 'e'), ('b', 'c'), ('c', 'e'), ('c', 'd'), ('e', 'd')]
ProblemTwoThreeG1 = Graph(vertices_g1, edges_g1)

# Debug 2
vertices_g2 = {'a', 'b', 'c', 'd'}
edges_g2 = [('a', 'b'), ('b', 'd'), ('b', 'c'), ('c', 'd')]
ProblemTwoThreeG2 = Graph(vertices_g2, edges_g2)

# Debug 3
vertices_g3 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
edges_g3 = [('a', 'b'), ('b', 'c'), ('b', 'g'), ('e', 'g'), ('d', 'c'), ('c', 'e'), ('e', 'f')]
ProblemTwoThreeG3 = Graph(vertices_g3, edges_g3)

# Test Graph
vertices = {'a', 'b', 'c', 'd', 'e', 'f'}
edges = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'f'), ('d', 'e'), ('d', 'f'), ('e', 'f')]
ProblemTwoThreeTest = Graph(vertices, edges)

