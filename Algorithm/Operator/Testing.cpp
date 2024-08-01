#include <iostream>

using namespace std;

int main() {
    int a = 12;            // Signed integer
    unsigned int b = 12;   // Unsigned integer
    b = b | (b >> 1);
    cout << b;

    return 0;
}
