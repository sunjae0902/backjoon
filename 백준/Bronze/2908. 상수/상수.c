#include <stdio.h>



int main(){
    // 문자열-상수
    char n[2][4]={0,};
    char temp;
    int num[2]={0,},i;
    for (int i=0;i<2;i++) scanf("%s",n[i]); //두 개의 세자리 문자열 입력
    
    
   
    for (int j=0;j<2;j++){
        for ( i=0;i<1;i++){ //1회 수행
            temp=n[j][i];
            n[j][i]=n[j][2-i];
            n[j][2-i]=temp; //자리교환
        }
        for (int k=0;k<3;k++)
            num[j]=num[j]*10+(n[j][k]-'0');
           
        
    }
    
    
    if (num[0]>num[1]) printf("%d\n",num[0]);
    else printf("%d\n",num[1]);
       
    
  
    
    
return 0;
}
