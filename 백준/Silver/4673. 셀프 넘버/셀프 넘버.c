#include <stdio.h>
int d(int n){
    int data[5]={0,},pos[5]={10000,1000,100,10,1};
    int sum=n;
    for (int i=0;i<4;i++){
       
        
        data[i]=(n%pos[i])/pos[i+1];
        n=n%pos[i];
 
        }
    for (int i=0;i<5;i++){
        sum+=data[i];
    }
    return sum;
        
}
    

int main() {

    int check,arr[10040]={0,};
    
    for(int i=0; i<10000; i++){//배열에 1~10000까지 넣어주고
            arr[i]=i;
        }
    for(int i=0; i<10000; i++){//셀프넘버가 아닌 수들: check에 저장후 배열 값 0으로 초기화
            check=d(i);
            arr[check]=0;
        }
        
    
    for (int i=0;i<=10000;i++){
        if (arr[i]!=0) printf("%d\n",arr[i]);
        }
    
    
    
   
    
return 0;
}

