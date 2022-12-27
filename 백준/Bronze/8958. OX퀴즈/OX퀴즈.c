#include <stdio.h>
#include <string.h>

int main() {
 
//1차원 배열-ox배열
    int N;
    scanf("%d",&N);
    for (int i=0;i<N;i++){
        int sum=0,cnt=1; //문자열 새로 받을 때마다 초기화
        char data[85];
        scanf("%s",data);
        
        for (int j=0;j<strlen(data);j++){
            
            if (data[j]=='O'){
                
                sum+=cnt;
                cnt++;
            }
            
            else cnt=1; //x만날때마다 cnt=0으로 초기화.
        }
        
        printf("%d\n",sum);
        
        
    }
    
    
        
        
    
    
    
    
    
    

    return 0;
}
