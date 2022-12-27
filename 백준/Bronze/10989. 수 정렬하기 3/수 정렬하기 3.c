#include <stdio.h>
#define MAX 10001

int main(){
    int N,tmp;
    int a[MAX]={0,};
    scanf("%d",&N);
    
    for (int i=0;i<N;i++){
        scanf("%d",&tmp);
        a[tmp]++;
    }
    
    for (int i=0;i<MAX;i++){
        for (int j=0;j<a[i];j++){
            printf("%d\n",i);
        }
    }
    
    
    
    
    

    
    
   
   
    return 0;
    
}
