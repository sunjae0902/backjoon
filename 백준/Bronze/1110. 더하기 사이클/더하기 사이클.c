#include<stdio.h>
int main(){
int a,b,c,N,n=-1; //a,b: 각각 몪과 나머지를 저장할 변수, c:입력받은 N을 저장한 초기 비교값,n:사이클을 거치게되는 숫자
    int count=0;
    
    scanf("%d",&N);
    c=N;
    
    while (n!=N) {
        b=c%10; //나머지
        a=c/10; //몫
        c=b*10+(a+b)%10;
        n=c;
        count++;
    }
    printf("%d\n",count);
  
    
    return 0;
}
