#include <stdio.h>
#define swap(a,b) {int temp; temp=a; a=b; b=temp;}

int main(void){
    int N,arr[1000]={0,};
    scanf("%d",&N);
    for (int i=0;i<N;i++) scanf("%d",&arr[i]);
    
    for (int j=0;j<N-1;j++){
        for (int i=0;i<N-1-j;i++){
            if (arr[i]>arr[i+1]) swap(arr[i],arr[i+1]);
        }
    }
    for (int i=0;i<N;i++) printf("%d\n",arr[i]);
    
    
    
    
    return 0;
}