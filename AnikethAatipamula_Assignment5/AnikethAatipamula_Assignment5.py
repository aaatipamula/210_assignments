from ext import (
    Relation,
    bezouts,
    bezoutsTwo,
    is_function,
    inverse_func,
    func_type,
    gcd
)

DIV_SIZE = 15

def resolveProblemOne(A: set, B: set, relation: Relation) -> None:
    if is_function(A, B, relation):
        function_type = func_type(B, relation)
        print("a) Is a function")
        print(f"b) Is {function_type}")
        if function_type == 'bijective':
            print(f"c) {inverse_func(relation)}")
        else:
            print("c) N/A")
    else:
        print("a) Not a function")
        print("b) N/A")
        print("c) N/A")

    print('-'*len(str(relation)))

def resolveProblemTwo(a: int, b: int) -> None:
    common_denom = gcd(a, b)
    print(f"gcd({a}, {b})={common_denom}")
    print('-'*DIV_SIZE)

def resolveProblemThree(a: int, b: int) -> None:
    s, t = bezouts(a, b)
    print(f"gcd({a}, {b})=({s}*{a})+({t}*{b})")
    print('-'*DIV_SIZE)

def resolveProblemFour(a: int, b: int) -> None:
    s, t = bezoutsTwo(a, b)
    print(f"gcd({a}, {b})=({s}*{a})+({t}*{b})")
    print('-'*DIV_SIZE)

def printProblemOne() -> None:
    print("1) Problem One\n")

    A = {'a','b','c','d'}
    B = {'v','w','x','y','z'}
    f = {('a','z'),('b','y'),('c','x'),('d','w')}
    resolveProblemOne(A, B, f)

    A = {'a','b','c','d'}
    B = {'x','y','z'}
    f = {('a','z'),('b','y'),('c','x'),('d','z')}
    resolveProblemOne(A, B, f)

    A = {'a','b','c','d'}
    B = {'w','x','y','z'}
    f = {('a','z'),('b','y'),('c','x'),('d','w')}
    resolveProblemOne(A, B, f)

    A = {'a','b','c','d'}
    B = {1,2,3,4,5}
    f = {('a',4),('b',5),('c',1),('d',3)}
    resolveProblemOne(A, B, f)

    A = {'a','b','c'}
    B = {1,2,3,4}
    f = {('a',3),('b',4),('c',1)}
    resolveProblemOne(A, B, f)
    
    A = {'a','b','c','d'}
    B = {1,2,3}
    f = {('a',2),('b',1),('c',3),('d',2)}
    resolveProblemOne(A, B, f)
    
    A = {'a','b','c','d'}
    B = {1,2,3,4}
    f = {('a',4),('b',1),('c',3),('d',2)}
    resolveProblemOne(A, B, f)

    A = {'a','b','c','d'}
    B = {1,2,3,4}
    f = {('a',2),('b',1),('c',2),('d',3)}
    resolveProblemOne(A, B, f)

    A = {'a','b','c'}
    B = {1,2,3,4}
    f = {('a',2),('b',1),('a',4),('c',3)}
    resolveProblemOne(A, B, f)

def printProblemTwo() -> None:
    print("2) Problem Two\n")

    resolveProblemTwo(414, 662)
    resolveProblemTwo(6, 14)
    resolveProblemTwo(24, 36)
    resolveProblemTwo(12, 42)
    resolveProblemTwo(252, 198)

def printProblemThree() -> None:
    print("3) Problem Three\n")

    resolveProblemThree(414, 662)
    resolveProblemThree(6, 14)
    resolveProblemThree(24, 36)
    resolveProblemThree(12, 42)
    resolveProblemThree(252, 198)

def printProblemFour() -> None:
    print("3) Problem Four\n")

    resolveProblemFour(414, 662)
    resolveProblemFour(6, 14)
    resolveProblemFour(24, 36)
    resolveProblemFour(12, 42)
    resolveProblemFour(252, 198)

def main() -> None:
    printProblemOne()
    printProblemTwo()
    printProblemThree()
    printProblemFour()

if __name__ == "__main__":
    main()
