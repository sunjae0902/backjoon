#include <stdio.h>

int main() {
 
//1차원 배열-나머지
    int count=0,data[10]={0,},arr[10]={0,};
    for (int i=0;i<10;i++) {
        scanf("%d\n",&data[i]);
        arr[i]=data[i]%42;
    }
    
    for (int j=0;j<9;j++){
        for (int i=0;i<9-j;i++){
            if (arr[i]<arr[i+1]) { //버블 정렬 내림차순
                int temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
             
            }
            
            
        }
    }
    int temp=-1;
    for (int i=0;i<10;i++){
        if (temp!=arr[i]){
            temp=arr[i];
            count++;
        }
        
    }
    printf("%d\n",count);

return 0;
}
