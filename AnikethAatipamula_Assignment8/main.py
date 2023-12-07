''' 
Program: EECS 210 Assignment 8
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 12/06/2023
Description: Run the main program
'''

# main imports from other files
from graph import (
    pproblemOne,
    pproblemTwo,
    pproblemThree
)
from graphs import (
    ProblemOneG1,
    ProblemOneG2,
    ProblemOneG3,
    ProblemOneBridge,
    ProblemOneTest,
    ProblemTwoThreeG1,
    ProblemTwoThreeG2,
    ProblemTwoThreeG3,
    ProblemTwoThreeTest,
)

from nim import printFourAB, printFourC

# define our div size and bar
DIV_SIZE = 30
DIV_BAR = "-"*DIV_SIZE

# run the main program
def main() -> None:
    print(DIV_BAR, "Problem 1", DIV_BAR, sep="\n")
    pproblemOne("Debug G1", ProblemOneG1)
    pproblemOne("Debug G2", ProblemOneG2)
    pproblemOne("Debug G3", ProblemOneG3)
    pproblemOne("Debug Bridge", ProblemOneBridge)
    pproblemOne("Test Problem One", ProblemOneTest)

    print(DIV_BAR, "Problem 2", DIV_BAR, sep="\n")
    pproblemTwo("Debug G1", ProblemTwoThreeG1)
    pproblemTwo("Debug G2", ProblemTwoThreeG2)
    pproblemTwo("Debug G3", ProblemTwoThreeG3)
    pproblemTwo("Test Problem Two", ProblemTwoThreeTest)

    
    print(DIV_BAR, "Problem 3", DIV_BAR, sep="\n")
    pproblemThree("Debug G1", ProblemTwoThreeG1)
    pproblemThree("Debug G2", ProblemTwoThreeG2)
    pproblemThree("Debug G3", ProblemTwoThreeG3)
    pproblemThree("Test Problem Three", ProblemTwoThreeG1)

    print(DIV_BAR, "Problem 4", DIV_BAR, sep="\n")
    fourA = printFourAB("Debug 1", 2, 2, 1)
    printFourAB("Test Problem Four", 1, 2, 3)
    printFourC("Simulation Problem Four", fourA)

if __name__ == "__main__":
    main()

