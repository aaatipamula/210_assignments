''' 
Program: EECS 210 Assignment 6
Inputs: No inputs to file required.
Outputs: No inputs required, outputs all the values of the required test cases
Collaborators/Sources: N/A
Name: Aniketh Aatipamula
Creation-Date: 11/28/2023
Description: define the functions to calculate for distinct/indistinct objects as well as
the functions to print the answers to the questions
'''

# import some functions to use for calculations
from math import factorial, comb

DIV_SIZE = 40

# recursive implementation
def distinct_items_boxes(items: int, items_per: int, boxes: int) -> float:
    # base case
    if boxes == 0:
        return 1
    # number of combos, equivalent to math.comb (https://docs.python.org/3/library/math.html#math.comb)
    C_n = factorial(items)/(factorial(items - items_per) * factorial(items_per))
    # product of all the combinations while we have boxes
    return int(C_n) * distinct_items_boxes(items - items_per, items_per, boxes - 1) 

def distinct_boxes_not_items(items: int, boxes: int) -> int:
    # Equivalent to the formula given in lecture
    # Simplified by setting a=items+boxes-1 and b=items for math.comb(a,b)
    return int(factorial(items + boxes - 1)/(factorial(boxes - 1) * factorial(items)))

def stirling_num_second_kind(n: int, j: int) -> float:
    ssum = 0
    # summation for the stirling num, taken from the slides
    # implemented using a for loop that will calculate each sum
    for i in range(j):
        # fomula within the stirling num summation
        ssum += pow(-1, i) * comb(j, i) * pow(j - i, n)
    # summation is multiplies by the inverse of the factorial of boxes
    return (1/factorial(j)) * ssum

def distinct_items_not_boxes(items: int, boxes: int) -> int:
    ssum = 0
    # summation for distinct items not boxes that uses the stirling number
    # taken from the lecture slides and adapted to fit python
    for j in range(1, boxes + 1):
        ssum += stirling_num_second_kind(items, j) 
    return int(ssum)

# uses a recursive implementation
def indistinguish_items_boxes(items: int, boxes: int) -> int:
    # base case one, if boxes are 0 there is just one way
    if items == 0:
        return 1
    # base case two, there are no ways if there are no boxes and items and they're both not zero
    if boxes == 0 or items < 0:
        return 0
    # taken from the lecture slides, simple closed form algo
    return indistinguish_items_boxes(items - boxes, boxes) + indistinguish_items_boxes(items, boxes - 1)

# functions to print each question mostly self explanatory
def q1():
    # print a division to seperate out each question
    print("-"*DIV_SIZE, "Question 1", "-"*DIV_SIZE, sep="\n")

    # example and answer
    ex8 = "Example 8: How many ways are there to deal 5-card poker hands from a 52 card deck to each of the four players"
    print(ex8)
    ans1 = distinct_items_boxes(52, 5, 4)
    print(f"{ans1} ways")

    # question and answer
    q1b = "Question 1b: A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box. How many ways can she distribute the journals if each box is numbered, so that they are distinguishable?"
    print(q1b)
    ans2 = distinct_items_boxes(40, 10, 4)
    print(f"{ans2} ways")

def q2():
    # print a division to seperate out each question
    print("-"*DIV_SIZE, "Question 2", "-"*DIV_SIZE, sep="\n")

    # example and answer
    ex9 ="Example 9: How many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?"
    print(ex9)
    ans1 = distinct_boxes_not_items(10, 8)
    print(f"{ans1} ways")

    # question and answer
    q2b = "Question 2b: How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?"
    print(q2b)
    ans2 = distinct_boxes_not_items(12, 6)
    print(f"{ans2} ways")

def q3():
    # print a division to seperate out each question
    print("-"*DIV_SIZE, "Question 3", "-"*DIV_SIZE, sep="\n")

    # example and answer
    ex10 = "Example 10: How many ways can Anna, Billy, Caitlin, and Danny be placed into three indistinguishable homerooms?"
    print(ex10)
    ans1 = distinct_items_not_boxes(4, 3)
    print(f"{ans1} ways")

    # question and answer
    q3b = "Question 3b: How many ways are there to put five temporary employees into four identical offices?"
    print(q3b)
    ans1 = distinct_items_not_boxes(5, 4)
    print(f"{ans1} ways")

def q4():
    # print a division to seperate out each question
    print("-"*DIV_SIZE, "Question 4", "-"*DIV_SIZE, sep="\n")

    # example and answer
    ex11 = "Example 11: How many ways can you pack six copies of the same book into four identical boxes?"
    print(ex11)
    ans1 = indistinguish_items_boxes(6, 4)
    print(f"{ans1} ways")

    # question and answer
    q4b = "Question 4b: How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?"
    print(q4b)
    ans1 = indistinguish_items_boxes(5, 3)
    print(f"{ans1} ways")

