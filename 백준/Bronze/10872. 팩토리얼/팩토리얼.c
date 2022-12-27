#include <stdio.h>
int fact(int n){
    if (n<=1) return 1;
    else return fact(n-1)*n;
}

int main(){
    int N,result=0;
    scanf("%d",&N);
    result=fact(N);
    printf("%d",result);
    
    return 0;
}