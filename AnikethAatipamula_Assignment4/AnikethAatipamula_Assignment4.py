''' 
Program: EECS 210 Assignment 3
Inputs: No inputs to file required.
Outputs: Whether each relation/set combo follows the rules for certain set properties
Collaborators/Sources: Arnav Jain, ChatGPT
Name: Aniketh Aatipamula
Creation-Date: 9/12/2023
Description: This program checks each set for given properties and how they are satisfied.
'''
Relation = set[tuple[int, int]]
Symmetry = tuple[bool, bool]

# Checks if a Relation (given a set part of the relation) is reflexive
def is_reflexive(R: Relation, A: set) -> bool:
    # for every value in the given Set
    for a in A:
        # if a point where both values are the value in the Set does not exist in the set it is not reflexive
        if (a, a) not in R: # concept taken from lecture and simplified using propositional logic
            return False
    return True

# generates the reflexive closure for a given relation and set
def reflexive_closure(R: Relation, A: set) -> Relation:
    # similar to checking for reflexivity
    for a in A:
        # if the pair doesn't exist just add it
        if (a, a) not in R:
            R.add((a, a))
    # return the completed relation that meets reflexive closure
    return R

# use the previously defined functions to print the results for an arbitary set and relation
def resolveProblemOne(R: Relation, A: set) -> None:
    print(f"1. a) R = {R}")
    # If its reflexive we don't have to find the closure
    if is_reflexive(R, A):
        print("1. b) R is reflexive")
        print("1. c) R* is not required")
    # We have to find the closure if its reflexive
    else:
        print("1. b) R is not reflexive")
        print(f"1. c) R* = {reflexive_closure(R, A)}")

# define the related relations and sets and print problem one
def ProblemOne() -> None:
    # Define relation and set one
    R1 = {(1,1), (4,4), (2,2), (3,3)}
    S1 = {1,2,3,4}

    # Define relation and set two
    R2 = {('a','a'), ('c','c')}
    S2 = {'a', 'b', 'c', 'd'}

    # resolve each pair relation/set
    resolveProblemOne(R1, S1)
    resolveProblemOne(R2, S2)

# Checks if a Relation (given a set part of the relation) is symmetric
def is_symmetric(R: Relation, A: set) -> bool:
    # Create a second copy of the set
    B = A.copy()
    # Generate pairs of a and b that and unique
    for a in A:
        for b in B:
            if (a, b) in R and (b, a) not in R: # concept take from lecture and simplified using propositional logic
                return False
        B.remove(a) # makes sure no overlapping pairs are made
    return True

# return the symmetric closure of a given Relation and Set
def symmetric_closure(R: Relation) -> Relation:
    R_copy = R.copy()

    # Arnav helped with this
    for pair in R:
        # if the pair that makes the relation reflextive doesn't exist just add it
        if (pair[::-1]) not in R:
            R_copy.add(pair[::-1])
    return R_copy

# print and calculate the 
def resolveProblemTwo(R: Relation, A: set) -> None:
    print(f"2. a) R = {R}")
    # If its symmetric we don't have to find the closure
    if is_symmetric(R, A):
        print("2. b) R is symmetric")
        print("2. c) R* is not required")
    # We have to find the closure if its not symmetric
    else:
        print("2. b) R is not symmetric")
        print(f"2. c) R* = {symmetric_closure(R)}")

# Define the given set/relations and resolve problem two
def ProblemTwo() -> None:
    # Define the set used for both relations
    S = {1,2,3,4}

    # Define the two relations to be evaluated
    R1 = {(1,2), (4,4), (2,1), (3,3)}
    R2 = {(1,2), (3,3)}

    # Resolve each problem for each set/relation pair
    resolveProblemTwo(R1, S)
    resolveProblemTwo(R2, S)

# Checks if relation is transitive (given a set part of the relation) 
def is_transitive(R: Relation, A: set) -> bool:
    # For every possible permutation of a, b, c
    for a in A:
        for b in A:
            for c in A:
                # checks if there are three "points" in the relation that are transitive
                # concept taken from lecture slides and simplified using propositional logic
                if (a, b) in R and (b, c) in R and (a, c) not in R:
                    return False
    return True

def transitive_closure(R: Relation, A: set) -> Relation:
    # create a n x n matrix the size of the set full of 0
    matrix = [[0 for _ in range(len(A))] for _ in range(len(A))] 

    # enter 1 where all the pair in the relation exist
    for pair in R:
        matrix[pair[0] - 1][pair[1] - 1] = 1

    print(matrix)

    # for each row, col pair (i.e. row 1, col2, then row2 col2)
    for index, row in enumerate(matrix):
        # grab the indicies where there is a 1 in the rows and cols
        col = [index for index, val in enumerate(row) if val == 1]
        row = [index for index, val in enumerate([row[index] for row in matrix]) if val == 1]

        # cross the indicies, generating where new pairs should be added to the matrix
        for a in col:
            for b in row:
                matrix[a][b] = 1

    # convert the matrix back into a relation
    relation = set()
    for r_indx, row in enumerate(matrix):
        for c_indx, val in enumerate(row):
            # generate a pair where each value in the matrix is 1
            if val == 1:
                relation.add((r_indx + 1, c_indx + 1))
    
    return relation

# Evaluate a given set/relation for reflexivity and obtain the reflexive closure if needed
def resolveProblemThree(R: Relation, A: set) -> None:
    print(f"3. a) R = {R}")
    # If its transitive we don't have to find the closure
    if is_transitive(R, A):
        print("3. b) R is transitive")
        print("3. c) R* is not required")
    # We have to find the closure if its not transitive
    else:
        print("3. b) R is not transitive")
        print(f"3. c) R* = {transitive_closure(R, A)}")

# Define the set/relation pairs and evaluate each of them for reflexivity and reflexive closure
def ProblemThree() -> None:
    # define set/relation pair one
    R1 = {('a','b'), ('d','d'), ('b','c'), ('a','c')}
    S1 = {'a', 'b', 'c', 'd'}

    # define set/relation pair two
    R2 = {(1,1),(1,3),(2,2),(3,1),(3,2)}
    S2 = {1, 2, 3}

    # evaluate each set/relation pair
    resolveProblemThree(R1, S1)
    resolveProblemThree(R2, S2)

# Checks for equivalence
# A set/relation pair is equivalent if they are reflexive, symmetric and transitive
def resolveProblemFour(R: Relation, A: set) -> None:
    # Show the relation
    print(f"4. a) R = {R}")

    reasons = ""
    is_equivalence = True

    # check for reflexivity, not equivalence if not
    if is_reflexive(R, A):
        reasons += " is reflexive"
    else:
        reasons += " is not reflexive"
        is_equivalence = False

    # check for symmetry, not equivalence if not
    if is_symmetric(R, A):
        reasons += " is symmetric"
    else:
        reasons += " is not symmetric"
        is_equivalence = False

    # check for transitivity, not equivalence if not
    if is_transitive(R, A):
        reasons += " is transitive"
    else:
        reasons += " is not transitive"
        is_equivalence = False

    # Print the result of our checks, with reasoning
    print(f"4. b) R is{' an' if is_equivalence else ' not a'} equivalence relation")
    print("4. c) This is because R" + reasons)

# Define and evaluate set/relation pairs for equivalence
def ProblemFour() -> None:

    # define set/relation pair one
    R1 = {(1,1),(2,2),(2,3)}
    S1 = {1,2,3}

    # define set/relation pair two
    R2 = {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')}
    S2 = {'a','b','c'}

    # evaluate each set/relation pair
    resolveProblemFour(R1, S1)
    resolveProblemFour(R2, S2)

# Checks if a Relation (given a set part of the relation) is symmetric
# Almost exactly the same as is_symmetric but checks if there is no value of b,a for a,b
def is_antisymmetric(R: Relation, A: set) -> bool:
    # Create a second copy of the set
    B = A.copy()
    # Generate pairs of a and b that and unique
    for a in A:
        for b in B:
            if (a, b) in R and (b, a) in R and a != b: # Help from Arnav and ChatGPT used here
                return False
        B.remove(a) # makes sure no overlapping pairs are made
    return True

# resolve an arbitrary set/relation pair for poset
def resolveProblemFive(R: Relation, A: set) -> None:
    # show the relation and set
    print(f"5. a) S = {A}")
    print(f"5. b) R = {R}")

    reasons = ""
    is_poset = True

    # check for reflexivity, not poset if not
    if is_reflexive(R, A):
        reasons += " is reflexive"
    else:
        reasons += " is not reflexive"
        is_poset = False

    # check for antisymmetry, not poset if not
    if is_antisymmetric(R, A):
        reasons += " is antisymmetric"
    else:
        reasons += " is not antisymmetric"
        is_poset = False

    # check for transivity, not poset if not
    if is_transitive(R, A):
        reasons += " is transitive"
    else:
        reasons += " is not transitive"
        is_poset = False

    # print if a poset or not and the reasons for so
    print(f"5. c) (S/R) is{'' if is_poset else ' not'} a poset")
    print("5. d) This is because R" + reasons)

# define the set/relation pairs and resolve them for poset
def ProblemFive() -> None:
    # define set/relation one
    R1 = {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)}
    S1 = {1, 2, 3, 4}

    # define set/relation two
    R2 = {(0, 0), (0, 1), (0, 2), (0, 3), (1,0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}
    S2 = {0, 1, 2, 3}

    # evaluate each set/relation pair for poset
    resolveProblemFive(R1, S1)
    resolveProblemFive(R2, S2)

# main program
def main() -> None:
    # Print the results of each question
    ProblemOne()
    print()
    ProblemTwo()
    print()
    ProblemThree()
    print()
    ProblemFour()
    print()
    ProblemFive()

if __name__ == "__main__":
    main()

