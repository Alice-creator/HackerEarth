#include <iostream>
#include <cstdio> // For printf
#include <bitset>
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
    unsigned long long int T, L, R, k, zerosCount = 0, tempOnes = 0;

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
                unsigned long long int tempL = L;
                for(int i = 0; tempL; i++){
                    if(zerosCount == k)
                        break;
                    if(tempL & 1)
                        k -= 1;
                    else
                        zerosCount += 1;
                    tempOnes = tempOnes << 1 | 1;
                    tempL >>= 1;
                    cout<< bitset<60>(L)<<endl<<zerosCount<<endl<<bitset<60>(tempOnes)<<endl<<endl;
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