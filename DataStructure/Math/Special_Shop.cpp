#include <iostream>
#include <cmath>
using namespace std;


void fastscan(unsigned long long &number) 
{
    unsigned long long c;
    number = 0;
    c = getchar();
    if (c=='\n') c = getchar(); 
    for (; (c>47 && c<58); c=getchar()) 
        number = number *10 + c - 48;
}
int main()
{
    freopen("INPUT.INP", "r", stdin);
    freopen("INPUT.OUT", "w", stdout);
    unsigned long long X , Y , result;
    unsigned long long T , N , A , B;

    fastscan(T);

    while(T != 0)
    {
        fastscan(N);
        fastscan(A);
        fastscan(B);

        if(A > B)
            {
                A = A + B;
                B = A - B;
                A = A - B;
            }
        
        X = N;
        Y = 0; 
        
        for(unsigned long long i = 0;;i++)
        {
        if((X - i + X - i - 1) * A <= (Y + i + Y + i + 1) * B)
            {
                result = (X - i) * (X - i) * A + (Y + i) * (Y + i) * B;
                break;
            }
        }

        cout<<result<<endl;

        T--;
    }
}