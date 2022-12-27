#include <stdio.h>
#define swap(a,b){int t=a; a=b; b=t;}

void Sorting(int N){
    int a[12]={0,};
    int i=0;
    while (N>=1) {
        a[i++]=N%10;
        N=N/10;
    }
    
    //내림차순 정렬
    
    for (int m=0;m<i-1;m++){
        for (int n=0;n<i-m-1;n++){
            if (a[n]<a[n+1]) swap(a[n], a[n+1]);
        }
    }
    
    for (int j=0;j<i;j++) printf("%d",a[j]);
}

int main(void) {
    int N;
    scanf("%d",&N);
    Sorting(N);
   
   
return 0;
}
