#include <stdio.h>
#include <string.h>

int main(){
    // 문자열-크로아티아 알파벳
    char wd[101]={0,};
    int num=0;
    scanf("%s",wd); //단어 입력
    for (int i=0; i<strlen(wd);i++){
        if (wd[i]=='c' && wd[i+1]=='=') num++;//두자리
        else if (wd[i]=='c' && wd[i+1]=='-') num++;
        else if (wd[i]=='d' && wd[i+1]=='-') num++;
        else if (wd[i]=='l' && wd[i+1]=='j') num++;
        else if (wd[i]=='n' && wd[i+1]=='j') num++;
        else if (wd[i]=='s' && wd[i+1]=='=') num++;
        else if (wd[i]=='d' && wd[i+1]=='z'&& wd[i+2]=='=') num+=2;
        else if (wd[i-1]!='d'&& wd[i]=='z' && wd[i+1]=='=') num++;
    
    }
    
    
    printf("%d\n",(int)strlen(wd)-num);
    
    
    
    
return 0;
}
