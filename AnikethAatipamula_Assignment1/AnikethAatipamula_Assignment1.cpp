/* Assignment Name: EECS 210 Assignment 1
 * Description: Print out the truth tables for each of the six given propositions using logical operators.
 * Inputs: None
 * Outputs: The truth tables for each proposition
 * Collaborators/Sources: N/A
 * Name: Aniketh Aatipamula
 * Creation Date: 8/24/2023
 */

# include <iostream> // Standard library for input and output streams.
# include <iomanip> // Standard library to format prettier output.
# include <string> // Standard library to add the string 'datatype'.

using namespace std; // Standard namespace for convenience

/* Description: The values needed for a two variable truth table
 * This is a 2D array of boolean values that define the 'input' for a two variable truth table.
 * Each 'column' corresponds to the possible values of one variable.
 * Each 'row' or 2 value array corresponds to a set of values that are used for each permutation
 */
const bool twoVarTT[4][2] = {
  {false, false},
  {true, false},
  {false, true},
  {true, true}
};

char twoVar[2] = {'p', 'q'}; // This a 2 value array that contains the logical variables to use in the header of a table.


/* Description: The values needed for a three variable truth table.
 * This is a 3D array of boolean values that define the 'input' for a three variable truth table.
 * Each 'column' corresponds to the possible values of one variable.
 * Each 'row' or 3 value array corresponds to a set of values that are used for each permutation
 */
const bool threeVarTT[8][3] = {
  {false, false, false},
  {false, false, true}, 
  {false, true, false},
  {false, true, true},
  {true, false, false},
  {true, false, true},
  {true, true, false},
  {true, true, true}
};

char threeVar[3] = {'p', 'q', 'r'}; // This a 3 value array that contains the logical variables to use in the header of a table.

/* Description: A simple function that implements the logical equivalent of the implication operator.
 * The logic was taken from the lecture slides. 
 */
bool implication(bool a, bool b) {
  return !a or b;
}

/* Description: A simple function that implements the logical equivalent of the biconditional operator.
 * The logic was taken from the lecture slides.
 */
bool biconditional(bool a, bool b) {
  return (implication(a, b) && implication(b, a));
}

/* Description: A class that stores information on a Truth table and prints out the correct information.
 */
class Table {
  private:
    string table_title; // Title of the table.
    string first_proposition; // The string representation of the first proposition to display in the table header.
    string second_proposition; // The string representation of the second proposition to display in the table header.
    int spacing_width; // How much spacing (in number of characters) to give the table header and rows.
    int number_vars; // How many logical variables are present in the table.
    char* vars; // Array of discrete variable combinations.

    /* Description: Print the title of the table along with the header row.
     * This firsts prints the title of the table 
     * Then depending on the number of variables it will print out the respective logical variables with proper spacing.
     * Finally it will print out the string representations of the two propositions with spacing defined in the class.
     */
    void printTitle() {
        cout << endl << table_title << endl << left;
        for (int i = 0; i < number_vars; i++) {
          cout << setw(10) << vars[i];
        }
        cout << setw(spacing_width) << first_proposition
          << setw(spacing_width) << second_proposition << endl;
    }


  public:
    /* Description: A constructor method for the class. 
     * This simply takes in the following variables and assigns them to the class.
     * Based on the number of variables the vars array will be assigned or an error is thrown.
     */
    Table(string title, string first_prop, string second_prop, int width, int num_vars) {
      table_title = title;
      first_proposition = first_prop;
      second_proposition = second_prop;
      spacing_width = width;
      if (num_vars == 2) {
        number_vars = num_vars;
        vars = twoVar;
      } else if (num_vars == 3) {
        number_vars = num_vars;
        vars = threeVar;
      } else {
        throw "Invalid variable size.";
      }
    }


    /* Description: Print the entire two value table.
     * This takes two pointers to two functions which are the logical representations of the propositions written using c++ operators.
     * This will first check if the number of variables is not 2 and throw and error if so.
     * It will then print the title using the private method.
     * Finally for each set of possible values of p and q it will do the following:
     * - Print the values of p and q with proper spacing.
     * - Print the values of the first and second propositions given p and q using logical representation functions.
     */
    void printTwo(bool (*op_one)(bool, bool), bool (*op_two)(bool, bool)) {

      if (number_vars == 3) {
        throw "Invalid method please use printThree";
      }

      printTitle();

      for (int i = 0; i < 4; i++) {
        bool a = twoVarTT[i][0];
        bool b = twoVarTT[i][1];
        cout << left << boolalpha
          << setw(10)  << a 
          << setw(10)  << b
          << setw(spacing_width) << op_one(a, b)
          << setw(spacing_width) << op_two(a, b) << endl;
      }
    }


    /* Description: Print the entire three value table.
     * This takes two pointers to two functions which are the logical representations of the propositions written using c++ operators.
     * This will first check if the number of variables is not 3 and throw and error if so.
     * It will then print the title using the private method.
     * Finally for each set of possible values of p, q, and r it will do the following:
     * - Print the values of p, q, and r with proper spacing.
     * - Print the values of the first and second propositions given p, q, and r using logical representation functions.
     */
    void printThree(bool (*op_one)(bool, bool, bool), bool (*op_two)(bool, bool, bool)) {

      if (spacing_width == 2) {
        throw "Invalid method please use printTwo.";
      }

      printTitle();

      for (int i = 0; i < 8; i++) {
        bool a = threeVarTT[i][0];
        bool b = threeVarTT[i][1];
        bool c = threeVarTT[i][2];
        cout << left << boolalpha
          << setw(10) << a 
          << setw(10) << b
          << setw(10) << c
          << setw(spacing_width) << op_one(a, b, c)
          << setw(spacing_width) << op_two(a, b, c) << endl;
      }
    }
};


Table DeMorgansFirst("1. Demorgans' First Law", "!(p+q)", "!p*!q", 10, 2); // Define a Table class for Demorgans' First Theorem.
bool demorganFirstOne(bool p, bool q) {return (!(p && q));} // A function to represent Demorgans first theorem with boolean operators.
bool demorganFirstTwo(bool p, bool q) {return (!p || !q);} // A function to represent Demorgans second theorem  with boolean operators.

Table DeMorgansSecond("2. Demorgans' Second Law", "!(p*q)", "!p+!q", 10, 2); // Define a Table class for Demorgans' Second Theorem.
bool demorganSecondOne(bool p, bool q) {return (!(p || q));} // A function to represent the first half of Demorgans first theorem with boolean operators.
bool demorganSecondTwo(bool p, bool q) {return (!p && !q);} // A function to represent the second half of Demorgans first theorem with boolean operators.

Table AssociativeFirst("3. First Associative Law:", "(p*q)*r", "p*(q*r)", 11, 3); // Define a table class for the First Associative Law.
bool associativeFirstOne(bool p, bool q, bool r) {return ((p && q) && r);} // A function to represent the first half of the first associative law with boolean operators.
bool associativeFirstTwo(bool p, bool q, bool r) {return (p && (q && r));} // A function to represent the second half of the first associative law with boolean operators.

Table AssociativeSecond("4. Second Associative Law:", "(p+q)+r", "p+(q+r)", 11, 3); // Define a table class for the Second Associative Law.
bool associativeSecondOne(bool p, bool q, bool r) {return ((p || q) || r);} // A function to represent the first half of the second associative law with boolean operators.
bool associativeSecondTwo(bool p, bool q, bool r) {return (p || (q || r));} // A function to represent the second half of the second associative law with boolean operators.

Table FifthProposition("5. Proposition Five:", "[(p+q)*(p->r)*(q->r)]->r", "True", 28, 3); // Define a table class for the Fifth Proposition.
bool fifthPropOne(bool p, bool q, bool r) {return implication(((p || q) && implication(p, r) && implication(q, r)), r);} // A function to represent the first half of the fifth proposition with boolean operators.
bool fifthPropTwo(bool p, bool q, bool r) {return true;} // A function to represent the second half of the fifth proposition with boolean operators.

Table SixthProposition("6. Proposition Six:", "p<->q", "(p->q)*(q->p)", 10, 2); // Define a table class for the Sixth Proposition.
bool sixthPropOne(bool p, bool q) {return biconditional(p, q);} // A function to represent the first half of the sixth proposition with boolean operators.
bool sixthPropTwo(bool p, bool q) {return (implication(p, q) && implication(q, p));} // A function to represent the second half fo the sixth proposition with boolean operators.

// Main function to run
int main(int argc, char* argv[]) {
  // Each of the following function calls in the try block take two functions that represent both 'halves' of the equation in boolean terms.
  try {
    DeMorgansFirst.printTwo(&demorganFirstOne, &demorganFirstTwo); // Print out the table of Demorgans First Law.
    DeMorgansSecond.printTwo(&demorganSecondOne, &demorganSecondTwo); // Print out the table of Demorgans Second Law.
    AssociativeFirst.printThree(&associativeFirstOne, &associativeFirstTwo); // Print out the table for the First Associative Law.
    AssociativeSecond.printThree(&associativeSecondOne, &associativeSecondTwo); // Print out the table for the Second Associative Law.
    FifthProposition.printThree(&fifthPropOne, &fifthPropTwo); // Print out the table for the Fifth Proposition.
    SixthProposition.printTwo(&sixthPropOne, &sixthPropTwo); // Print out the table for the Sixth Proposition.
  } catch (string e) {
    cout << e; // Catch any errors and print the string.
  }
  return 0; // End program.
}

