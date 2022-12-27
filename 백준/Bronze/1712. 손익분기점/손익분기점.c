#include <stdio.h>
#include <string.h>

int main(){
    // 기본수학1-손익분기점
    int A,B,C,i=0;
    scanf("%d %d %d",&A,&B,&C); //A:고정 B:가변 C:노트북 한 대당 가격
    if (C!=B){ i=A/(C-B);
        if (i<0) printf("-1\n");
        else printf("%d\n",i+1);}
    else printf("-1\n");
 return 0;
}
