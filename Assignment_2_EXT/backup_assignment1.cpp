#include <iostream>
#include <optional>
#include <array>

std::array<int, 11> domainOne = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

bool ForAll (bool (*func)(int)) {
  for (auto num : domainOne) {
    if (not(func(num))) {
      return false;
    }
  }
  return true;
}

bool ForSome (bool (*func)(int)) {
  for (auto num : domainOne) {
    if (func(num)) {
      return true;
    }
  }
  return false;
}

bool P(int x) {
  return (x < 2);
}

bool Q(int x) {
  return (x > 7);
}

bool PAndQ(int x) {
  return (P(x) || Q(x));
}

bool PFive(int x) {
  return (x < 5);
}

bool NotPFive(int x) {
  return (x >= 5);
}

bool DemorgansP(int x) {
  return (not(PFive(x)) == NotPFive(x));
}

void printSetOne() {
  std::cout << "1. a) "
    << std::boolalpha << ForSome(&P) << "\n";
  std::cout << "1. b) "
    << std::boolalpha << ForAll(&P) << "\n";

  std::cout << "1. c) "
    << std::boolalpha << ForSome(&PAndQ) << "\n";
  std::cout << "1. d) "
    << std::boolalpha << ForAll(&PAndQ) << "\n";

  std::cout << "1. e) "
    << std::boolalpha << ForSome(&DemorgansP) << "\n";
  std::cout << "1. f) "
    << std::boolalpha << ForAll(&DemorgansP) << "\n";
}

// Code for Set Two
std::array<double, 9> domainTwo = {1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1};

bool Pxy(double x, double y) {
  double mult = x * y;
  return mult == 1;
}

bool ForSomePxy(double given) {
  for (auto num : domainTwo) {
    if (Pxy(given, num)) {
      return true;
    }
  }
  return false;
}

bool ForAllPxy (double given) {
  for (auto num : domainTwo) {
    if (not(Pxy(given, num))) {
      return false;
    }
  }
  return true;
}

bool ForSomeXY(bool (*quant)(double)) {
  for (auto num : domainTwo) {
    if (quant(num)) {
      return true;
    }
  }
  return false;
}

bool ForAllXY (bool (*quant)(double)) {
  for (auto num : domainTwo) {
    if (not(quant(num))) {
      return false;
    }
  }
  return true;
}

void printSetTwo() {
  std::cout << "2. a) " 
    << std::boolalpha << ForAllXY(&ForAllPxy) << "\n";

  std::cout << "2. b) " 
    << std::boolalpha << ForAllXY(&ForSomePxy) << "\n";
  
  std::cout << "2. c) " 
    << std::boolalpha << ForAllXY(&ForSomePxy) << "\n";

  std::cout << "2. d) " 
    << std::boolalpha << ForSomeXY(&ForAllPxy) << "\n";

  std::cout << "3. e) " 
    << std::boolalpha << ForSomeXY(&ForAllPxy) << "\n";

  std::cout << "2. f) " 
    << std::boolalpha << ForSomeXY(&ForSomePxy) << "\n";
}


int main(int argc, char* argv[]) {
  printSetOne();
  std::cout << "\n";
  printSetTwo();
  return 0;
}
