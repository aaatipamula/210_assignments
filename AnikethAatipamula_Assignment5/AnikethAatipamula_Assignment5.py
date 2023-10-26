''' 
Program: EECS 210 Assignment 5
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 10/23/2023
Description: This program prints out if relations are functions and their type for some defined relations, 
and the gcd and bezouts coefficents for some defined numbers.
'''

# Import the necessary functions from another module
from ext import (
    Relation,
    bezouts,
    bezoutsTwo,
    is_function,
    inverse_func,
    func_type,
    gcd
)

# how many characters the bar seprating questions 
DIV_SIZE = 15

# resolve problem one for any two given sets and a relation
def resolveProblemOne(A: set, B: set, relation: Relation) -> None:
    # check if the set is a function
    if is_function(A, B, relation):
        # find the function type
        function_type = func_type(B, relation)
        print("a) Is a function")
        print(f"b) Is {function_type}")
        # get the inverse if bijective
        if function_type == 'bijective':
            print(f"c) {inverse_func(relation)}")
        else:
            print("c) N/A")
    # if not then we don't have to find anything
    else:
        print("a) Not a function")
        print("b) N/A")
        print("c) N/A")

    # seperate individual problems
    print('-'*len(str(relation)))

# resolve problem two for any two given integers
def resolveProblemTwo(a: int, b: int) -> None:
    # find the gcd
    common_denom = gcd(a, b)
    # print the gcd
    print(f"gcd({a}, {b}) = {common_denom}")
    print('-'*DIV_SIZE)

# resolve problem three for any two given integers
def resolveProblemThree(a: int, b: int) -> None:
    # find the coefficents using method 1
    s, t = bezouts(a, b)
    # print the coefficents in an equation
    print(f"gcd({a}, {b}) = ({s} * {a}) + ({t} * {b})")
    print('-'*DIV_SIZE)

# resolve problem three for any two given integers
def resolveProblemFour(a: int, b: int) -> None:
    # find the coefficents using method 2
    s, t = bezoutsTwo(a, b)
    # print the coefficents in an equation
    print(f"gcd({a}, {b}) = ({s} * {a}) + ({t} * {b})")
    print('-'*DIV_SIZE)

# print the result of problem one for all the provided cases
def printProblemOne() -> None:
    print("1) Problem One\n")
    
    # case one
    A = {'a','b','c','d'}
    B = {'v','w','x','y','z'}
    f = {('a','z'),('b','y'),('c','x'),('d','w')}
    resolveProblemOne(A, B, f)

    # case two
    A = {'a','b','c','d'}
    B = {'x','y','z'}
    f = {('a','z'),('b','y'),('c','x'),('d','z')}
    resolveProblemOne(A, B, f)

    # case three
    A = {'a','b','c','d'}
    B = {'w','x','y','z'}
    f = {('a','z'),('b','y'),('c','x'),('d','w')}
    resolveProblemOne(A, B, f)

    # case four
    A = {'a','b','c','d'}
    B = {1,2,3,4,5}
    f = {('a',4),('b',5),('c',1),('d',3)}
    resolveProblemOne(A, B, f)

    # cause five
    A = {'a','b','c'}
    B = {1,2,3,4}
    f = {('a',3),('b',4),('c',1)}
    resolveProblemOne(A, B, f)
    
    # cause six
    A = {'a','b','c','d'}
    B = {1,2,3}
    f = {('a',2),('b',1),('c',3),('d',2)}
    resolveProblemOne(A, B, f)
    
    # case seven
    A = {'a','b','c','d'}
    B = {1,2,3,4}
    f = {('a',4),('b',1),('c',3),('d',2)}
    resolveProblemOne(A, B, f)

    # case eight
    A = {'a','b','c','d'}
    B = {1,2,3,4}
    f = {('a',2),('b',1),('c',2),('d',3)}
    resolveProblemOne(A, B, f)

    # case nine
    A = {'a','b','c'}
    B = {1,2,3,4}
    f = {('a',2),('b',1),('a',4),('c',3)}
    resolveProblemOne(A, B, f)

# print the result of problem two for each case
def printProblemTwo() -> None:
    print("2) Problem Two\n")

    # case one
    resolveProblemTwo(414, 662)
    # case two
    resolveProblemTwo(6, 14)
    # case three
    resolveProblemTwo(24, 36)
    # case four
    resolveProblemTwo(12, 42)
    # case five
    resolveProblemTwo(252, 198)

# print the result of problem three for each case
def printProblemThree() -> None:
    print("3) Problem Three\n")

    # case one
    resolveProblemThree(414, 662)
    # case two
    resolveProblemThree(6, 14)
    # case three
    resolveProblemThree(24, 36)
    # case four
    resolveProblemThree(12, 42)
    # case five
    resolveProblemThree(252, 198)

# print the result of problem four for each case
def printProblemFour() -> None:
    print("4) Problem Four\n")

    # case one
    resolveProblemFour(414, 662)
    # case two
    resolveProblemFour(6, 14)
    # case three
    resolveProblemFour(24, 36)
    # case four
    resolveProblemFour(12, 42)
    # case five
    resolveProblemFour(252, 198)

# the main function to run
# print the result of all cases for problems 1-4
def main() -> None:
    printProblemOne()
    printProblemTwo()
    printProblemThree()
    printProblemFour()

# run the main program
if __name__ == "__main__":
    main()
