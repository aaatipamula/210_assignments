/* Assignment Name: EECS 210 Assignment 1
 * Description: Print out the truth tables for each of the six given propositions using logical operators.
 * Inputs: None
 * Outputs: The truth tables for each proposition
 * Collaborators/Sources: N/A
 * Name: Aniketh Aatipamula
 * Creation Date: 8/24/2023
 */

// Standard libraries for output, output formatting, and strings
# include <iostream> // input and output streams
# include <iomanip> // library to format prettier output
#include <streambuf>
# include <string> // library to add the string 'datatype'
#include <string_view>

using namespace std; // standard namespace for convenience
                     //

/* Description: The values needed for a two variable truth table
 * This is a 2D array of boolean values that define the 'input' for a two variable truth table.
 * Each 'column' corresponds to the possible values of one variable.
 * Each 'row' or 2 value array corresponds to a set of values that are used for each permutation
 */
const bool truthTableOne[4][2] = {
  {false, false},
  {true, false},
  {false, true},
  {true, true}
};


/* Description: The values needed for a three variable truth table.
 * This is a 3D array of boolean values that define the 'input' for a three variable truth table.
 * Each 'column' corresponds to the possible values of one variable.
 * Each 'row' or 3 value array corresponds to a set of values that are used for each permutation
 */
const bool truthTableTwo[8][3] = {
  {false, false, false},
  {false, false, true}, 
  {false, true, false},
  {false, true, true},
  {true, false, false},
  {true, false, true},
  {true, true, false},
  {true, true, true}
};


/* Description: Print the title of a table and its header.
 * This is a simple function that takes in the following parameters:
 * - The title of the table
 * - An array of all the input variables to list in the table header row
 * - The size of the previous array
 * - The first proposition
 * - The second proposition
 * This function then prints out those parameters in a neat order. It is meant to be a helper function.
 * It first prints out the title with spacing and a new line with a function that left aligns the following text.
 * It then prints out every input variable with a spacing of 5 characters.
 * Finally it prints out the two propositions that we are comparing.
 */
void printTitle(string title, char *sets, int size, string op_one, string op_two, int width) {
    cout << endl << title << endl << left;
    for (int i = 0; i < size; i++) {
      cout << setw(5) << sets[i];
    }
    cout << setw(width) << op_one
      << setw(width) << op_two << endl;
}


/* Description: Implementation of the implication operator in a function.
 * This is defined from the logical equivalences given to us in lecture.
 */
bool implication(bool a, bool b) {
  return !a or b;
}


/* Description: Implementation of the biconditional operator in a function.
 * This is defined from the logical equivalences given to us in lecture.
 */
bool biconditional(bool a, bool b) {
  return (implication(a, b) && implication(b, a));
}

/* Description: Print a truth table for DeMorgans' First and Second Laws.
 * This function accepts a 4x2 array and a parameter to select the first or second DeMorgans law.
 * The array is supposed to be the input table for a two variable truth table.
 * From there I define an array size, which I then use to define an array that contains the variables to use.
 * I also define a sizing width to use when formatting the output.
 * The function then branches at the if statement depending on the chosen law.
 * For law 1 and 2 I then print their respective titles of the table with the helper function I previously defined.
 * Then for every possible permutation of a two variable truth table I print out the values of the variables
 *   and the values for each equivalent equation.
 * If the law is not equal to 1 or 2 it will raise an error.
 * Each equation is defined using c++ logical operators.
 */
void deMorgansLaws(const bool table[4][2], int law) {

  int size = 2;
  int width = 10;
  char vals[size] = {'A', 'B'};

  // Depending on the law print the correct table or throw an error.
  if (law == 1) {

    // Print the title of the table and the header values
    printTitle("1. Demorgans' First Law:", vals, size, "!(A+B)", "!A*!B", width);

    // Print each possible value of the truth table for the values of A and B and the values of each proposition.
    for (int i = 0; i < 4; i++) {
      bool a = table[i][0];
      bool b = table[i][1];
      cout << left 
        << setw(5) << a 
        << setw(5) << b
        << setw(width) << (!(a && b))
        << setw(width) << (!a || !b) << endl;
    }

  } else if (law == 2) {

    printTitle("2. Demorgans' Second Law:", vals, size, "!(A*B)", "!A+!B", width);

    for (int i = 0; i < 4; i++) {
      bool a = table[i][0];
      bool b = table[i][1];
      cout << left 
        << setw(5) << a 
        << setw(5) << b
        << setw(width) << (!(a || b)) // The c++ representation of the proposition
        << setw(width) << (!a && !b) << endl; // The c++ representation of the proposition
    }

  } else {
    throw "Invalid DeMorgans Law."; // Throw an error if the law is not the first or second
  }
}


// Printn the truth tables for the Associative Laws
void associativeLaws(const bool table[8][3], int law) {

  int size = 3;
  int width = 11;
  char vals[size] = {'A', 'B', 'C'};

  if (law == 1) {
    
    printTitle("3. First Associative Law:", vals, size, "(A*B)*C", "A*(B*C)", width);

    for (int i = 0; i < 8; i++) {
      bool a = table[i][0];
      bool b = table[i][1];
      bool c = table[i][2];
      cout << left 
        << setw(5) << a 
        << setw(5) << b
        << setw(5) << c
        << setw(width) << ((a && b) && c)
        << setw(width) << (a && (b && c)) << endl;
    }

  } else if (law == 2) {

    printTitle("4. Second Associative Law:", vals, size, "(A+B)+C", "A+(B+C)", width);

    for (int i = 0; i < 8; i++) {
      bool a = table[i][0];
      bool b = table[i][1];
      bool c = table[i][2];
      cout << left 
        << setw(5) << a 
        << setw(5) << b
        << setw(5) << c
        << setw(width) << ((a || b) || c)
        << setw(width) << (a || (b || c)) << endl;
    }

  } else {
    throw "Invalid Associative Law."; // Throw an error if the law is invalid
  }
}


void fifthProposition(const bool table[8][3]) {

  int size = 3;
  int width = 25;
  char vals[] = {'p', 'q', 'r'};
  
  printTitle("5. Proposition Five:", vals, size, "[(p+q)*(p->r)*(q->r)]->r", "True", width);

  for (int i = 0; i < 8; i++) {
      bool p = table[i][0];
      bool q = table[i][1];
      bool r = table[i][2];
      cout << left 
        << setw(5) << p
        << setw(5) << q
        << setw(5) << r
        << setw(width) << implication(((p || q) && implication(p, r) && implication(q, r)), r)
        << setw(width) << (true) << endl;
  }

}


void sixthProposition(const bool table[4][2]) {

  int size = 2;
  int width = 10;
  char vals[] = {'p', 'q'};
  
  printTitle("6. Proposition Six:", vals, size, "p<->q", "(p->q)*(q->p)", width);

  for (int i = 0; i < 8; i++) {
      bool p = table[i][0];
      bool q = table[i][1];
      cout << left 
        << setw(5) << p
        << setw(5) << q
        << setw(width) << biconditional(p, q)
        << setw(width) << (implication(p, q) && implication(q, p)) << endl;
  }

}


int main(int argc, char* argv[]) {

  try {

    char test[3] = {'A', 'B', 'C'};
    
    deMorgansLaws(truthTableOne, 1);
    deMorgansLaws(truthTableOne, 2);

    associativeLaws(truthTableTwo, 1);
    associativeLaws(truthTableTwo, 2);
    
    fifthProposition(truthTableTwo);
    sixthProposition(truthTableOne);

  } catch (string e) {
    cout << e;
  }

  return 0;
}
