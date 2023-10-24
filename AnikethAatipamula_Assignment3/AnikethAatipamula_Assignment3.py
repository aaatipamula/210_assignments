# Type annotation alias for Relations, and Symmetric
Relation = set[tuple[int, int]]
Symmetric = tuple[bool, bool]

def rComposition(S: Relation, R: Relation) -> Relation:
    # Create a map of all the values of the "inbetween" set to the end set
    hashmap = {}
    for key, val in S:
        # If a key is mapped to a value add it to the list of possible values
        if key in hashmap:
            hashmap.get(key, []).append(val)
        # Map a key to a value if not already mapped.
        else:
            hashmap[key] = [val]
    
    # Create a new relation and all all the possible key value pairs
    newRelation: Relation = set()
    for key, val in R:
        vals = hashmap.get(val, []) # Get a value from the map
        for val in vals:
            newRelation.add((key, val)) # Add a new "point" to the final relation

    return newRelation

# Generate a set from the negative to positive index of a number
def generateSet(n: int) -> set:
    if n < 0:
        n = -n # Convert to positive integer if negative
    return {n for n in range(-n, n+1)} # use a set composition to create a set from -n to n

# A set builder function following {(x,y) | x+y=0}
def generateRelation(A: set) -> Relation:
    return {(x,-x) for x in A if -x in A} # Use a set comprehension to build the relation

# Checks if a Relation (given a set part of the relation) is reflexive
def is_reflexive(R: Relation, A: set) -> bool:
    for a in A:
        # for every value in the given Set
        # if a point where both values are the value in the Set does not exist in the set it is not reflexive
        if (a, a) not in R: # concept taken from lecture and simplified using propositional logic
            return False
    return True

# Checks if a Relation (given a set part of the relation) is symmetric
def is_symmetric(R: Relation, A: set) -> bool:
    # Create a second copy of the set
    B = A.copy()
    # Generate pairs of a and b that and unique
    for a in A:
        for b in A:
            if (a, b) in R and (b, a) not in R: # concept take from lecture and simplified using propositional logic
                return False
        B.remove(a) # makes sure no overlapping pairs are made
    return True

# Checks if a Relation (given a set part of the relation) is symmetric
# Almost exactly the same as is_symmetric but checks if there is no value of b,a for a,b
def is_antisymmetric(R: Relation, A: set) -> bool:
    # Create a second copy of the set
    B = A.copy()
    # Generate pairs of a and b that and unique
    for a in A:
        for b in A:
            if (a, b) in R and (b, a) in R: # concept take from lecture and simplified using propositional logic
                return False
        B.remove(a) # makes sure no overlapping pairs are made
    return True

# A helper function
# Takes the logic from the lecture and applies it to a function
def symmetry(R: Relation, A: set) -> Symmetric:
    # If the relation is symmetric then it is not antisymmetric
    if is_symmetric(R, A):
        return True, False

    # If the relation is Antisymmetric is is not symmetric
    if is_antisymmetric(R, A):
        return False, True

    # It can be neither
    return False, False

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

# Helper function to print the results of problem one
def printProblemOne(ROne: Relation, RTwo: Relation) -> None:
    print(f"R1 = {ROne}")  # print relation one
    print(f"R2 = {RTwo}")  # print relation one
    print("\n1. a) Union of R1 and R2")
    # Builtin
    # Takes the Union (combining the values of two Relation into one Relation)
    print(ROne.union(RTwo))
    print("\n1. b) Intersection of R1 and R2")
    # Builtin
    # Takes the Intersection (values that appear in R1 and R2)
    # Returns a new Relation
    print(ROne.intersection(RTwo))
    print("\n1. c) R1 minus R2")
    # Builtin
    # Takes the intersection of R1 and R2
    # Removes the values present in the intersection from R1
    print(ROne - RTwo)
    print("\n1. c) R2 minus R1")
    # Builtin
    # Takes the intersection of R1 and R2
    # Removes the values present in the intersection from R2
    print(RTwo - ROne, "\n\n")

# Helper function to print the results of problem two
def printProblemTwo(S: Relation, R: Relation) -> None:
    print(f"S = {S}")  # print S
    print(f"R = {R}")  # print R
    newRelation = rComposition(S, R) # create the compositon of S and R
    print("\n2. Composite of S and R") # print the title
    print(newRelation, "\n\n") # print the new relation

# Helper function to print the results of problem three
def printProblemThree(R: Relation) -> None:
    print(f"R = {R}")  # print R
    newRelation = rComposition(R, R) # create the composition of R with itself, i.e. R^2
    print("\n3. R^2") # print the title
    print(newRelation, "\n\n") # print R^2

# Helper function to print the results of problem four
def printProblemFour(n: int) -> None:
    A = generateSet(n) # generate a set from -n to n
    R = generateRelation(A) # generate a relation following {(x,y) | x+y=0}
    print("4. a) R as a Set of Ordered Pairs") # print title
    print(f"R = {R}")  # print the generated relation
    print("\n4. b) Is R Reflexive:") # print the title
    print(is_reflexive(R, A)) # calculate if the relation is reflexive and print
    symmetric, antisymmetric = symmetry(R, A) # calculate if the relation is symmetric/antisymmetric
    print("\n4. b) Is R Symmetric:") # print title
    print(symmetric) # print if the relation is symmetric
    print("\n4. b) Is R Antisymmetric:") # print title
    print(antisymmetric) # print if the relation is antisymmetric
    print("\n4. b) Is R Transitive:") # print title
    print(is_transitive(R, A), "\n\n") # calculate and print if the relation is transitive


def main() -> None:

    # Print problem one with the relations given to us
    printProblemOne(
        {(1,1), (2,2), (3,3)},
        {(1,1), (1,2), (1,3), (1,4)}
    )

    # Print problem two with the relations given to us
    printProblemTwo(
        {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)},
        {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
    )

    # Print problem three with the relation given to us
    printProblemThree(
        {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}        
    )

    # Print problem four with a set ranging from -10 to 10
    printProblemFour(10)

if __name__ == "__main__":
    main()
