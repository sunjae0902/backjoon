#include <stdio.h>
int hansu(int N){
    
    int num=0,sum=0;
    if (N<100)
        for (int i=1;i<=N;i++) num++;//한자리~두자리
        
       
    if (N<=999 && N>=100) { //세자리 수인 경우
        
            
        sum=hansu(99); //sum=99
        for (int j=100;j<=N;j++) {
            int temp1=j/100; //백의자리
            int temp2=j%100/10;//십의자리
            int temp3=j%10; //일의자리
            if (temp3-temp2==temp2-temp1) num++;
    }
}
    sum+=num;
        
            
    
     if (N==1000) sum=hansu(999); //네자리
    
    
    
    
    
    return sum;
}


int main() {
    int N;
    scanf("%d",&N);
    printf("%d\n",hansu(N));
    
    
return 0;
}
