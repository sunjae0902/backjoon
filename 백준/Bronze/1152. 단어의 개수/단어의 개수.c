#include <stdio.h>
#include <string.h>
//공백으로 시작하거나 끝날 수 있다

int main(void){
    char str[1000000];
    gets(str); //공백을 무시하고 엔터를 누를때까지 저장
    int cnt=0;
    char *p=strtok(str," ");
    while (p!=NULL) {
        cnt++;
        p=strtok(NULL," ");
    }
    printf("%d\n",cnt);
    
    return 0;
}