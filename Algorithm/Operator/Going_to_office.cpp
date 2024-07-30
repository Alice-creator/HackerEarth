#include <iostream>
#include <cstdio> // For printf
using namespace std;

void fastScan(long int &number) {
    bool negative = false;
    register long int c;
    
    number = 0; // Initialize the number variable
    c = getchar();
    
    if (c == '-') {
        negative = true;
        c = getchar();
    }
    
    // Read until a non-digit character is found
    while (c >= '0' && c <= '9') {
        number = number * 10 + (c - '0');
        c = getchar();
    }
    
    if (negative) {
        number *= -1;
    }
}

int main() {
    long int inputValue[8];

    // Read input values
    for (long int i = 0; i < sizeof(inputValue) / sizeof(inputValue[0]); i++) {
        fastScan(inputValue[i]);
    }

    // Compute onlineCost and classicCost
    long int onlineCost = inputValue[1] + (inputValue[0] - inputValue[2]) * inputValue[3];
    long int classicCost = inputValue[5] + (inputValue[0] / inputValue[4]) * inputValue[6] + inputValue[0] * inputValue[7];

    // Find the minimum cost
    const char* result = (onlineCost <= classicCost) ? "Online Taxi" : "Classic Taxi";

    // Print the result
	// printf("%d %d\n", onlineCost, classicCost);
    printf("%s\n", result);

    return 0;
}
