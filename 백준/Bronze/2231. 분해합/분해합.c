#include <stdio.h>


int sumfunc(int x){
    int Sum=0;
    while (x>0) {
        Sum+=x%10;
        x=x/10;
    }

    return Sum;
}
   


int main(){
    int N,x=1;
    scanf("%d",&N);
    int a=sumfunc(198);
    
   while (N>x) {
        
       if (sumfunc(x)+x==N) {printf("%d\n",x); return 0;}
        x++;
    }
    printf("%d\n",0);
      
    return 0;
    
}
