#include <stdio.h>

int main(){
    // 문자열-숫자 합산
    int N,sum=0;
    char p[101]={0,};
    scanf("%d",&N);//숫자의 개수
   
   
    scanf("%s",p);
           
    for (int i=0;i<N;i++){
       sum+=p[i]-'0';
    }
    printf("%d\n",sum);
    
    
    
   
    
return 0;
}
