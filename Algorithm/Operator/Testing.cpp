#include <iostream>
#include <cstdio> // For printf
using namespace std;

void fastScan(unsigned long long int &number) {
    bool negative = false;
    register unsigned long long int c;
    
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
    unsigned long long int T, L, R, k, zerosCount = 0, tempOnes = 1;

    T = 1;
    // cout<<T;
    while(T > 0){
        L = 19345887176838426;
        R = 666421096271935940;
        k = 16;
        
        if(R >> k){
            if(!(L >> k)){
                printf("pass here %llu\n", (1ULL << k) - 1);
            }
            else{
                for(int i = 0; i <= 60; i++){
                    if(zerosCount == k)
                        break;
                    zerosCount += (L & 1) ? 0 : 1;
                    tempOnes = (tempOnes << 1) | 1;
                    L >>= 1;
                }
                if(zerosCount == k){
                    printf("%llu", L | tempOnes);
                }
                else
                    printf("can't fit %d\n", -1);
                
                printf("%llu", zerosCount);
            }
            
        }
        else
            printf("%d\n", -1);
        T--;
    }



    return 0;
}