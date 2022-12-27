#include <stdio.h>

int main() {
 
//1차원 배열-최대값 찾기
    int data[9];
    for (int i=0;i<9;i++)  scanf("%d",&data[i]);
    
    int max=0,sum=0,cnt=0;
    for (int i=0;i<9;i++){
        if (data[i]>sum) {
            sum=data[i];
            max=sum;
            cnt=i; //반복문이 돌때마다 i로 나타낸 현재 위치를 cnt변수에 저장
            
        }
        
    }
    
    printf("%d\n%d\n",max,cnt+1); // i는 0부터 세므로 현재 위치는 +1해서 나타냄
    
        
    
    
return 0;
}
