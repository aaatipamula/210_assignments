/* Program: EECS 210 Assignment 2
 * Inputs: No inputs to file required.
 * Outputs: The values of each assertion outlined in the assignment.
 * Collaborators/Sources: Google for cpp syntax.
 * Name: Aniketh Aatipamula
 * Creation-Date: 9/12/2023
 * Description: This is a program that emulates the assertions given to us in the assignment outline for Assignment 2. 
 */

#include <iostream>
#include <optional>
#include <array>

/* Declare and initialize an array called 'domainOne' with 11 integer elements.
 * This contains the domain for all the assertions to be made in part 1.
 * Used Google for std::array usage
 */
std::array<int, 11> domainOne = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

/* Define a function 'ForAll' that takes a function pointer 'func' as an argument,
 * which represents a boolean function that takes an integer argument.
 * If the proposition is false for one value of the domain the assertion is false.
 */
bool ForAll(bool (*func)(int)) {
  /* Iterate over each element 'num' in the 'domainOne' array.
   * for auto loop taken from stack overflow
   */
  for (auto num : domainOne) {
    // If the result of 'func(num)' is false the entire assertion is false for this quantifier.
    if (not(func(num))) {
      std::cout << "if x = " << num << "; "; // print the value that disproves the quantifier.
      return false;
    }
  }
  // If the loop completes without returning false, the assertion is true for this quantifier.
  std::cout << "for all x; ";
  return true;
}

// Define a function 'ForSome' similar to 'ForAll', but returns true if the proposition (func) is true for at least one 'num'.
bool ForSome(bool (*func)(int)) {
  /* Iterate over each element 'num' in the 'domainOne' array.
   * for auto loop taken from stack overflow
   */
  for (auto num : domainOne) {
    // If the result of 'func(num)' is true, then the assertion is true for the entire domain.
    if (func(num)) {
      std::cout << "if x = " << num << "; "; // print the value that proves the quantifier.
      return true;
    }
  }
  // If the loop completes without returning true, then the assertion is false for this quantifier.
  return false;
}

/* Define three boolean functions 'P', 'Q', and 'PAndQ' that take an integer argument
 * and return true or false based on some conditions.
 */

// Function 'P' returns true if 'x' is less than 2.
bool P(int x) {
  return (x < 2);
}

// Function 'Q' returns true if 'x' is greater than 7.
bool Q(int x) {
  return (x > 7);
}

// Function 'PAndQ' returns true if either 'P(x)' or 'Q(x)' is true.
bool PAndQ(int x) {
  return (P(x) || Q(x));
}

// Define three more boolean functions 'PFive', 'NotPFive', and 'DemorgansP'.

// Function 'PFive' returns true if 'x' is less than 5.
bool PFive(int x) {
  return (x < 5);
}

// Function 'NotPFive' returns true if 'x' is greater than or equal to 5.
bool NotPFive(int x) {
  return (x >= 5);
}

// Function 'DemorgansP' returns true if the negation of 'PFive(x)' is equal to 'NotPFive(x)'.
bool DemorgansP(int x) {
  return (not(PFive(x)) == NotPFive(x));
}

/* Define a function 'printSetOne' to print the results of various boolean functions
 * This is applied to 'domainOne'.
 * Print the values in 'true' and 'false' (std::boolalpha)
 */
void printSetOne() {
  std::cout << "1. a) " << std::boolalpha << ForSome(&P) << "\n";
  std::cout << "1. b) " << std::boolalpha << ForAll(&P) << "\n";
  std::cout << "1. c) " << std::boolalpha << ForSome(&PAndQ) << "\n";
  std::cout << "1. d) " << std::boolalpha << ForAll(&PAndQ) << "\n";
  std::cout << "1. e) " << std::boolalpha << ForSome(&DemorgansP) << "\n";
  std::cout << "1. f) " << std::boolalpha << ForAll(&DemorgansP) << "\n";
}

// Define an array 'domainTwo' with 9 double elements.
std::array<double, 9> domainTwo = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1};

/* Define a boolean function 'Pxy' that takes two double arguments 'x' and 'y',
 * and returns true if their product is equal to 1.
 */
bool Pxy(double x, double y) {
  double mult = x * y;
  return mult == 1;
}

/* Define a function 'ForSomePxy' that checks if there exists an element in 'domainTwo'for which 'Pxy(given, num)' is true.
 * This function is meant to be wrapped by another quantifier function and emulates the Exestential-
 * Quantifer similar to the previously defined Exestential Quantifer function.
 */
bool ForSomePxy(double given) {
  for (auto num : domainTwo) {
    if (Pxy(given, num)) {
      std::cout << num << ", "; // print the number that made the quantifier true
      return true; 
    }
  }
  return false;
}

/* Define a function 'ForAllPxy' that checks if 'Pxy(given, num)' is true for all elements in 'domainTwo'.
 * This function is meant to be wrapped by another quantifier function and emulates the Universal-
 * Quantifer similar to the previously defined Universal Quantifer function.
 */
bool ForAllPxy(double given) {
  for (auto num : domainTwo) {
    if (not(Pxy(given, num))) {
      std::cout << num << ", "; // print the number that made the quantifier false
      return false;
    }
  }
  return true;
}

// Define two more functions 'ForSomeXY' and 'ForAllXY' that apply boolean functions to elements of 'domainTwo'.

/* Function 'ForSomeXY' checks if there exists an element in 'domainTwo' for which 'quant(num)' is true.
 * This function is meant to wrap another quantifier function and applies the Exestential-
 * Quantifier to another arbitrary quantifier.
 */
bool ForSomeXY(bool (*quant)(double ), char dom1, char dom2) {
  std::cout << "if " << dom2 << " = "; // print pretty stuff to show values
  for (auto num : domainTwo) {
    if (quant(num)) {
      std::cout << "and "<< dom1 << " = " << num << "; "; // more printing of pretty stuff to show values
      return true;
    }
  }
  std::cout << "for each " << dom1 << "; "; // more printing of pretty stuff to show values
  return false;
}

/* Function 'ForAllXY' checks if 'quant(num)' is true for all elements in 'domainTwo'.
 * This function is meant to wrap another quantifier function and applies the Universal-
 * Quantifier to another arbitrary quantifier.
 */
bool ForAllXY(bool (*quant)(double), char dom1, char dom2) {
  std::cout << "if " << dom2 << " = "; // print pretty stuff to show values
  for (auto num : domainTwo) {
    if (not(quant(num))) {
      std::cout << "and "<< dom1 << " = " << num << "; "; // more printing of pretty stuff to show values
      return false;
    }
  }
  std::cout << "for all " << dom1 << "; "; // more printing of pretty stuff to show values
  return true;
}

/* Define a function 'printSetTwo' to print the results of various boolean functions.
 * This is applied to 'domainTwo'.
 * Print the values in 'true' and 'false' (std::boolalpha)
 */
void printSetTwo() {
  std::cout << "2. a) " << std::boolalpha << ForAllXY(&ForAllPxy, 'x', 'y') << "\n";
  std::cout << "2. b) " << std::boolalpha << ForAllXY(&ForSomePxy, 'x', 'y') << "\n";
  std::cout << "2. c) " << std::boolalpha << ForAllXY(&ForSomePxy, 'y', 'x') << "\n";
  std::cout << "2. d) " << std::boolalpha << ForSomeXY(&ForAllPxy, 'x', 'y') << "\n";
  std::cout << "3. e) " << std::boolalpha << ForSomeXY(&ForAllPxy, 'y', 'x') << "\n";
  std::cout << "2. f) " << std::boolalpha << ForSomeXY(&ForSomePxy, 'x', 'y') << "\n";
}

// The main function that prints the results of both 'printSetOne' and 'printSetTwo'.
int main(int argc, char* argv[]) {
  printSetOne(); // print the first set
  std::cout << "\n"; // space out the two sets
  printSetTwo(); // print the second set
  return 0;
}

