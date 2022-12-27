#include <stdio.h>

int main() {
 
//1차원 배열-최소,최대
    int N;
    int data[1000000];
    scanf("%d",&N);
    for (int i=0;i<N;i++) scanf("%d",&data[i]);
    
    int min=0,max=0,sum1=-1000001,sum2=1000001;
    
    for (int i=0;i<N;i++) {
        if (data[i]>sum1) {
            sum1=data[i];
            max=sum1;
        }
    }
    
    for (int i=0;i<N;i++) {
        if (data[i]<sum2) {
            sum2=data[i];
            min=sum2;
        }
    }
    printf("%d %d\n",min,max);
   
    
        
        
    
        
    
    return 0;
}
