from typing import Generator, Literal, Tuple, List, Set

Relation = Set[Tuple[int | str, int | str]]
FuncType = Literal['injective', 'surjective', 'bijective']
GCDGen = Generator[List[int], None, None]

# determine if relation a function
def is_function(A: set, B: set, relation: Relation) -> bool:
    if len(relation) != len(A):
        return False
    inputs = set()
    outputs = set()
    for _input, output in relation:
        inputs.add(_input)
        outputs.add(output)
    if inputs == A and outputs.issubset(B):
        return True
    return False

# determine type of function, assumes relation is a function
def func_type(B: set, relation: Relation) -> FuncType:
    outputs = tuple(output for _, output in relation)
    unique_outputs = set(outputs)
    injective = len(outputs) == len(unique_outputs)
    surjective = unique_outputs == B
    if surjective and injective:
        return 'bijective'
    elif surjective:
        return 'surjective'
    return 'injective'

# find the inverse of a function relation
def inverse_func(relation: Relation) -> Relation:
    return set((output, _input) for _input, output in relation)

def _gcd(a: int, b: int) -> GCDGen:
    x = max(a, b)
    y = min(a, b)
    r = 0
    while y != 0:
        r = x % y 
        yield [x, y, x//y, r]
        x = y
        y = r

# find the GCD using euclid's method
def gcd(a: int, b: int) -> int:
    x = 0
    for x, y, q, r in _gcd(a, b):
        print(f"{x}/{y} = {q} R {r}")
        x = x
    return x

# find the bezouts coefficents for the two numbers using the euclidean algorithim
def bezouts(_a: int, _b: int) -> Tuple[int, int]:
    # generate the steps needed using the euclidean algo
    steps = [pair for pair in _gcd(_a, _b)]

    # we don't need the last step and we have to reverse the order of euclidean steps
    steps.pop()
    steps.reverse()

    # grab the previous step to modify throughout the number of steps, add a coefficent to keep track of (s)
    previous = steps[0]
    s = 1

    # loop through the steps
    for a, b, t, r in steps[1:]:
        # print the current state of the equation
        print(f"{previous[3]}={s}*{previous[0]}-{previous[2]}*{previous[1]}")

        # find where the remainder is equal to another value in the equation
        indx = previous.index(r) 

        # if the remainder is equal to the first value (a)
        if indx == 1:
            # print r subbed in for a
            print(f"{previous[3]}={s}*{previous[0]}-{previous[2]}*({a}-{t}*{b})")
            # calculate the value of t (because of how we factor in r)
            s = previous[2]*t + s

        # if the remainder is equal to the second value (b)
        elif indx == 0:
            # print r subbed in for b
            print(f"{previous[3]}={s}*({a}-{t}*{b})-{previous[2]}*{previous[1]}")
            # calculate the value of t (because of how we factor in r)
            previous[2] = s*t + previous[2]
        
        # set a or b equal to whatever a is (because of how we subbed in r)
        previous[indx] = a

    # print the final equation that gives us the coefficents
    print(f"{previous[3]}={s}*{previous[0]}-{previous[2]}*{previous[1]}")

    # if the number inputted first is greater its coefficent is s
    if _a > _b:
        return s, -previous[2]
    # if the number inputted second is greater its coefficent is s
    return -previous[2], s

def bezoutsTwo(_a: int, _b: int) -> Tuple[int, int]:

    # create 3 lists to keep track of all the values fo s, t, and q
    s = [1, 0] # s0 and s1 will always be 1, 0 respectively
    t = [0, 1] # t0, t1 will always be 0, 1 respectively
    q = [] 

    indx = 2 # we are starting to calculate s and t at index 2
    for index, vals in enumerate(_gcd(_a, _b), 1):
        # keep track of q
        q.append(vals[2])
        # use the extended euclidean formula to calculate s at index 2-j
        # akin to s(j-2) - q(j-1) * s(j-1)
        s.append(s[indx-2] - vals[2] * s[indx-1])
        # use the extended euclidean formula to calculate t at index 2-j
        # akin to t(j-2) - q(j-1) * t(j-1)
        t.append(t[indx-2] - vals[2] * t[indx-1])
        indx += 1

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
            print(f"s{index} = s{index-2} - {val} * s{index-1} = {val}", end=", ")
        else:
            # we don't need to calculate the value of s0 and s1
            print(f"s{index} = {val}", end=", ")

    print("")

    # print each sub value of t and how we calculated that subvalue
    for index, val in enumerate(t):
        if index not in (0, 1):
            # print each value and how we calculated that value for s
            print(f"t{index} = t{index-2} - {val} * t{index-1} = {val}", end=", ")
        else:
            # we don't need to calculate the value of s0 and s1
            print(f"t{index} = {val}", end=", ")

    print("")

    # if the number inputted first is greater its coefficent is s
    if _a > _b:
        return s[-1], t[-1]
    # if the number inputted second is greater its coefficent is s
    return t[-1], s[-1],

