#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  string digits = "0123456789";
  // string digits = "012";
  int n = 1;
  do {
    if (n == 1000000) {
      cout << digits << '\n';
      return 0;
    }
    n++;
  } while (next_permutation(digits.begin(), digits.end()));
}
