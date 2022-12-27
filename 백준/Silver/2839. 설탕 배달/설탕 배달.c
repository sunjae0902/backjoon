#include <stdio.h>

int main(){
    // 기본수학1-설탕배달
    int N,i;
    scanf("%d",&N);
    if (N%5!=0){
        for (i=N/5;i>=0;i--){
            if ((N-5*i)%3==0){
                printf("%d\n",i+(N-5*i)/3);
                return 0;}
            else continue;
  }
        printf("-1\n");
    }
   else printf("%d\n",N/5);
    return 0;
}
