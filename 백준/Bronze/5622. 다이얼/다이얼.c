#include <stdio.h>
#include <string.h>


int main(){
    // 문자열-다이얼
    char num[16]={0,};
    int time=0;
    
    scanf("%s",num);
    for (int i=0;i<strlen(num);i++){
        if (num[i]>=65 && num[i]<=67) time+=3;
            else if (num[i]>=68 && num[i]<=70) time+=4;
            else if (num[i]>=71 && num[i]<=73) time+=5;
            else if (num[i]>=74 && num[i]<=76) time+=6;
            else if (num[i]>=77 && num[i]<=79) time+=7;
            else if (num[i]>=80 && num[i]<=83) time+=8;
            else if (num[i]>=84 && num[i]<=86) time+=9;
            else if (num[i]>=87 && num[i]<=90) time+=10;
        
        
    }
    printf("%d\n",time);

    
return 0;
}
