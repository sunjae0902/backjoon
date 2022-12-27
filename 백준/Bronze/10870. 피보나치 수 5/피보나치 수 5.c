#include <stdio.h>

 
int fibo(int n){
    if (n==0) return 0;
    else if (n<=2) return 1;
    else return fibo(n-1)+fibo(n-2);
    
}

int main(){
    int N,result=0;
    scanf("%d",&N);
    result=fibo(N);
    printf("%d",result);
   
    
    

 return 0;
}
