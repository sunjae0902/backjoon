#include <stdio.h>
#include <string.h>

int main(){
    // 문자열-문자열 반복
    int T,n;
    char data[25]={0,};

    scanf("%d\n",&T); //테스트 케이스의 개수
    
    for (int a=0;a<T;a++){
        scanf("%d %s",&n,data); //반복 횟수, 문자열을 T만큼 입력받음
        for (int b=0;b<strlen(data);b++){ //외부: 문자열 이동
             for (int c=0;c<n;c++){ //내부: 각 문자  n회 반복출력
                 printf("%c",data[b]);
                
                }
        }
        
       
        printf("\n");
}
    
    
    
   
    
return 0;
}
