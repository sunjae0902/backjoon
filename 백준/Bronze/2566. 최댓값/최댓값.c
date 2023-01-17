#include <stdio.h>
#include <stdlib.h>

int main(void){
    int matrix[81]={0,};
    int max=0,r,c,k=0;
    for(int i=0;i<81;i++) scanf("%d",&matrix[i]);
    
    for(int i=0;i<81;i++)
        if (max<matrix[i]) {
            max=matrix[i];
            k=i;
            }
    if((k+1)%9!=0){
        r=(k+1)/9+1;
        c=(k+1)%9;}
    else{
        r=(k+1)/9;
        c=9;
    }
    
    printf("%d\n%d %d\n",max,r,c);
   return 0;
}
