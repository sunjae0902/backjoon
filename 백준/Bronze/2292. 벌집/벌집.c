#include <stdio.h>

int main(){
    // 기본수학1-벌집
    long long int N;
    scanf("%lld",&N);
    int n=1;
    if (N==1) { printf("1\n"); return 0;}
    else{
        while(1){
            if (N>=(3*n*n-3*n+2) && N<=(3*n*n+3*n+1)) break;
            else n++;}
    }
    
        printf("%d\n",n+1);
  
    return 0;
}
