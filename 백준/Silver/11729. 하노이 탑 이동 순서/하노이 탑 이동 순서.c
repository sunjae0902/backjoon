#include <stdio.h>

void hanoi(int,char,char,char);



void hanoi(int n,char from, char to , char aux){ //원판의 개수, from->aux->to
    if (n==1) {
        printf("%c %c\n",from,to);
        return;} //원반이 한 개라면 그냥 바로 옮김
   
    else{ //원반이 두 개 이상일때
        hanoi(n-1, from, aux, to); // n-1개의 원반을 from-> aux로 옮기기 . 보조기둥 to
        printf("%c %c\n",from,to); //가장 큰 원반을 목적지로 이동
        hanoi(n-1, aux, to, from); //n-1개의 원반을 aux->to로 옮기기. 보조 기둥 from
    }
    
}


int main(){
    int N,cnt=1;
    scanf("%d",&N); //원판의 개수
    
    for (int i=0;i<N;i++) cnt*=2;
    printf("%d\n",cnt-1);
    hanoi(N,'1','3','2'); //from=1 to=3 aux=2
 
    
   
    
    
    return 0;
    
}
