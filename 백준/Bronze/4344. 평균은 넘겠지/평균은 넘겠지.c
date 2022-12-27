#include <stdio.h>


int main() {
 
//1차원 배열-평균은 넘겠지
    int C,N;
    double rat=0.0,ave=0.0;
    int data[1001];
    
    scanf("%d",&C); //테스트 케이스의 수
    for (int i=0;i<C;i++) {
        scanf("%d",&N); //학생 수 입력
         int sum=0,num=0;
         for (int j=0;j<N;j++){
              scanf("%d",&data[j]);
              sum+=data[j];
         
              ave=(double)sum/N;
             
         }
        for (int j=0;j<N;j++){
            if (data[j]>ave) num++;
        }
              
        
        
        
        rat=(double)num/N*100;
        printf("%0.3f%%\n",rat);
    
        
    }
    
    
    
    
    
    
    

    return 0;
}
