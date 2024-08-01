#include <iostream>
#include <cstdio> // For printf
using namespace std;

void fastScan(unsigned long long number) {
    bool negative = false;
    register unsigned long long c;
    
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

bool checkInrange(unsigned long long L, unsigned long long R, unsigned long long k){
    unsigned long long temp = 1 << k;
    return (L <= temp) && (temp <= R) ? true : false;
}

int main() {
    unsigned long long T, L, R, k;

    fastScan(T);
    while(T > 0){
        fastScan(L);
        fastScan(R);
        fastScan(k);
        if(checkInrange(L, R, k))
            printf("%llu", (1 << k) - 1);
        else
            printf("%d", -1);
        T--;
    }



    return 0;
}
