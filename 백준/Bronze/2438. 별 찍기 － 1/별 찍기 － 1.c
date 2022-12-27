#include<stdio.h>
int main() {

int S;
    scanf("%d",&S); //n줄의 별 출력
    for (int i=1;i<=S;i++) { //외부 반복문: 1줄
        for (int j=0;j<i;j++){ // 1줄에 별 프린트
            printf("*");
        }
        printf("\n");//줄에 별 프린트 후 줄바꿈->다시 외부 for문으로 회귀
        
    }
  
return 0;
}