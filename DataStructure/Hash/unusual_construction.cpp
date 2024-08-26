#include <iostream>

using namespace std;

void intputnumber(int &num){
    register int c = getchar();
    num = 0;
    for(; c >= '0' && c <= '9'; c = getchar()){
        num = num * 10 + (c - '0');
    }
}

int main(){
    freopen("INPUT.INP", "r", stdin);
    freopen("INPUT.OUT", "w", stdout);

    int T, N, K, reverse;
    intputnumber(T);
    

    for(int i = 0; i < T; i++){
        intputnumber(N);
        intputnumber(K);
        int arr[N];
        for(int j = 0; j < N; j++){
            intputnumber(arr[j]);
            reverse = 1;
            
            while(j - reverse >= 0 && K > 0 && arr[j - reverse] < arr[j]){
                K -= arr[j - reverse] == 0 ? 0 : 1;
                arr[j - reverse] = -1;
                reverse++;
            }
        }
        for(int j = 0; j < N; j++){
            if(arr[j] != -1)
                printf("%d ", arr[j]);
        }
        printf("\n");
    }
    return 0;
}