#include <stdio.h>
#include <string.h>

int main(){
    // 문자열-단어 공부
    char wd[1000001]={0,};
    scanf("%s",wd);
    char alph[27][2]={0,};
    int num[27]={0,};
    unsigned long len=strlen(wd);
    for (int j=0;j<26;j++){
        alph[j][0]='A'+j; //대문자 저장
        alph[j][1]='a'+j; //소문자 저장
    }

    for (int i=0;i<len;i++){ //시간복잡도 증가 방지
        for (int j=0;j<26;j++){
            if (wd[i]==alph[j][0] || wd[i]==alph[j][1])
                num[j]++;
        }
    }
    int max=num[0],a=0;
    for (int i=0;i<26;i++){
        if (num[i+1]>max) {
            max=num[i+1];
            a=i+1; //최댓값 인덱스 저장
        }
    }
    for (int i=0;i<26;i++){
        if (num[i]==max && i!=a)
        { printf("?\n"); return 0;}
    }printf("%c\n",alph[a][0]);
    
        
    
    
   
    
        
    
                
        
        
        
        
    
    
    
    return 0;
}
