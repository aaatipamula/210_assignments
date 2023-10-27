''' 
Program: EECS 210 Assignment 5
Inputs: No inputs to file required.
Outputs: Function relation types, and GCD for sets of numbers using different methods
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 10/23/2023
Description: This program defines algorithms and types to find properties of relations
and determine the gcd of two numbers, and bezouts coefficents in various ways.
'''

# import typing stuff for my sake
from typing import Generator, Literal, Tuple, List, Set

# define what a relation is
Relation = Set[Tuple[int | str, int | str]]
# define what values the func_type function can return
FuncType = Literal['injective', 'surjective', 'bijective', 'neither injective nor surjective']
# define what the _gcd generator yields
GCDGen = Generator[List[int], None, None]

# determine if relation a function
def is_function(A: set, B: set, relation: Relation) -> bool:
    # if the relation is not equal in length to the number of inputs it cannot be a function relation
    if len(relation) != len(A):
        return False
    # we will create a sets of all the inputs and outputs from the relation
    inputs = set()
    outputs = set()
    for _input, output in relation:
        inputs.add(_input)
        outputs.add(output)
    # if the input set matches A and outputs belong to B we have a functino
    if inputs == A and outputs.issubset(B):
        return True
    # otherwise not a function
    return False

# determine type of function, assumes relation is a function
def func_type(B: set, relation: Relation) -> FuncType:
    # Get all the outputs not elimination the unique ones
    outputs = tuple(output for _, output in relation)
    # get all the unique outputs
    unique_outputs = set(outputs)
    # if the number of unique outputs are equal in length to the number of all outputs the function is injective
    # does not necessarily mean that the outputs contain every value in B
    injective = len(outputs) == len(unique_outputs)
    # if the number of unique outputs is the same as B there is a one-one mapping of inputs or outputs
    # this indicates surjective
    surjective = unique_outputs == B
    # definition of bijective
    if surjective and injective:
        return 'bijective'
    # if its not bijective and is surjective
    elif surjective:
        return 'surjective'
    elif injective:
        return 'injective'
    # otherwise nothing
    return 'neither injective nor surjective'

# find the inverse of a function relation
def inverse_func(relation: Relation) -> Relation:
    # just iterate through the relation and invert each pair
    return set((output, _input) for _input, output in relation)

# a generator that returns all the steps for a gcd of any two numbers
def _gcd(a: int, b: int) -> GCDGen:
    # get the min/max to normalize the process
    x = max(a, b)
    y = min(a, b)
    # just defining the remainder
    r = 0
    # while the divisor isn't zero
    while y != 0:
        # the remainder is the mod of x and y
        r = x % y 
        # yield the current values
        yield [x, y, x//y, r]
        # shift the dividend and divisor to continue
        x = y
        y = r

# find the GCD using euclid's method
def gcd(a: int, b: int) -> int:
    # x is arbitrarily defined
    y = 0
    # using the gcd generator print out all the values 
    for x, y, q, r in _gcd(a, b):
        print(f"{x}/{y} = {q} R {r}")
        x = y
    # return the last dividend (x) which should be the gcd
    return y

# find the bezouts coefficents for the two numbers using the euclidean algorithim
def bezouts(A: int, B: int) -> Tuple[int, int]:
    steps = []
    # generate the steps needed using the euclidean algo
    for step in _gcd(A, B):
        # keep track of the step
        steps.append(step)
        # print the step
        print(f"{step[0]} = {step[1]} * {step[2]} + {step[3]}")

    # we don't need the last step and we have to reverse the order of euclidean steps
    steps.pop()
    steps.reverse()

    # grab the previous step to modify throughout the number of steps, add a coefficent to keep track of (s)
    _a, _b, _t, gcd = steps[0]
    s = 1

    # loop through the steps
    for a, b, t, r in steps[1:]:
        # print the current state of the equation
        print(f"{gcd} = {s} * {_a} - {_t} * {_b}")

        # if the remainder is equal to the first value (a)
        if r == _b:
            # print r subbed in for a
            print(f"{gcd} = {s} * {_a} - {_t} * ({a} - {t} * {b})")
            # calculate the value of t (because of how we factor in r)
            s = _t*t + s
            # set b equal to whatever a is (because of how we subbed in r)
            _b = a 

        # if the remainder is equal to the second value (b)
        elif r == _a:
            # print r subbed in for b
            print(f"{gcd} = {s} * ({a} - {t} * {b}) - {_t} * {_b} ")
            # calculate the value of t (because of how we factor in r)
            _t = s*t + _t
            # set a or b equal to whatever a is (because of how we subbed in r)
            _a = a 

    # print the final equation that gives us the coefficents
    print(f"{gcd} = {s} * {_a} - {_t} * {_b}")

    # match each coefficent to the proper input value
    if A == _a:
        return s, -_t
    # s and t are flipped if A does not map to _a
    return -_t, s

def bezoutsTwo(_a: int, _b: int) -> Tuple[int, int]:

    # create 3 lists to keep track of all the values fo s, t, and q
    s = [1, 0] # s0 and s1 will always be 1, 0 respectively
    t = [0, 1] # t0, t1 will always be 0, 1 respectively
    q = [] 

    for indx, step in enumerate(_gcd(_a, _b), 2):
        # keep track of q
        q.append(step[2])
        # use the extended euclidean formula to calculate s at index 2-j
        # akin to s(j-2) - q(j-1) * s(j-1)
        s.append(s[indx-2] - step[2] * s[indx-1])
        # use the extended euclidean formula to calculate t at index 2-j
        # akin to t(j-2) - q(j-1) * t(j-1)
        t.append(t[indx-2] - step[2] * t[indx-1])

    # we don't need the last two values of s and t
    s.pop()
    t.pop()

    # print the quotients that we found
    for index, val in enumerate(q):
        print(f"q{index} = {val}", end=", ")

    print("")
    
    # print each sub value of s and how we calculated that subvalue
    for index, val in enumerate(s):
        if index not in (0, 1):
            # print each value and how we calculated that value for s
            print(f"s{index} = {s[index-2]} - {q[index-2]} * {s[index-1]} = {val}", end=", ")
        else:
            # we don't need to calculate the value of s0 and s1
            print(f"s{index} = {val}", end=", ")

    print("")

    # print each sub value of t and how we calculated that subvalue
    for index, val in enumerate(t):
        if index not in (0, 1):
            # print each value and how we calculated that value for s
            print(f"t{index} = {t[index-2]} - {q[index-2]} * {t[index-1]} = {val}", end=", ")
        else:
            # we don't need to calculate the value of s0 and s1
            print(f"t{index} = {val}", end=", ")

    print("")

    # if the number inputted first is greater its coefficent is s
    if _a > _b:
        return s[-1], t[-1]
    # if the number inputted second is greater its coefficent is s
    return t[-1], s[-1],

