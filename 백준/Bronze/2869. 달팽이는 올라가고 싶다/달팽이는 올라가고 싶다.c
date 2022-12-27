#include <stdio.h>

int main(){
    // 기본수학1-달팽이는올라가고싶다
    int A,B,V,i=1;
    scanf("%d %d %d",&A,&B,&V);
   if ((V-B)%(A-B)==0) i=(V-B)/(A-B);
   else i=(V-B)/(A-B)+1;
    
    printf("%d\n",i);
 
    return 0;
}
