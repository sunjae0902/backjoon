#include <stdio.h>
#include <string.h>

int main(){
    // 문자열-알파벳
    char wd[101]={0,};
    char data[125]={0,};
    rewind(stdin);
    scanf("%s",wd);
    

    
    for (int i='a';i<='z';i++){ //i는 아스키 코드 값 97-122
        data[i]=-1;//-1로 초기화
        for (int j=0;j<strlen(wd);j++){
            if (i==wd[j]) {
                data[i]=j;
                break;
            }
    }
}
    for (int i=97;i<123;i++) printf("%d ",data[i]);
    
    printf("\n");
    
    
   
    
return 0;
}
