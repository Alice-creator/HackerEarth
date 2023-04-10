//Big data Algorithm
//problem : small factorial (hackerearth)
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;


int main(){
    freopen("INPUT.INP", "r", stdin);
    freopen("INPUT.OUT", "w", stdout);

    vector<string> mul (101,"");
    long long store[301];
    int T, N, count = 300, last = 0;

    fill(store, store + 301, 1);

    scanf("%d", &T);
    
    int i = 1;

    while(T > 0)
    {
        scanf("%d", &N);
        //tinh so i = N; neu da tinh N
        if(mul[N] != "")
            cout<<mul[N]<<endl;
        else        //neu chua tinh N
        {
            while(i <= N)
            {
                int spare = 0;
    
                for(int k = 300; k >= count; k--)
                {
                    store[k] = store[k] * i + spare;
                    spare = store[k] / pow(10, 5); //luu so du
                    store[k] = store[k] % 100000; // store[k] <= 100000
                    
                    if(k == count) //luu gia tri sau khi tinh xong
                    {
                        for(int e = 300; e >= count; e--)
                        {
                            mul[i] = to_string(store[e]) + mul[i]; 

                            while(mul[i].length() % 5 != 0 && (e != count || spare != 0))
                                mul[i] = "0" + mul[i];
                        }
                    }
                }
                if(spare != 0) // tao store moi neu co so du spare
                    {
                        store[count - 1] = spare;
                        mul[i] = to_string(spare) + mul[i];
                        spare = 0;
                        count--;
                    }
                i++; //tinh i cho den khi i = N
            } //ket thuc thuat toan
            cout<<mul[N]<<endl; 
        }
        T--;
    }
}
