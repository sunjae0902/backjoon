#include <stdio.h>
#include <stdlib.h>



int main(void){
    int N,l=0,k;
    int ind[10000],arr[10]={0,}; //종말의 수를 저장할 배열과 자릿수를 저장할 배열
    
    scanf("%d",&N); //N번째 종말의 숫자 출력
    for(int i=666;l<10000;i++){
        k=i;
        int m=0;
        while (k>0) {
            arr[m]=k%10;
            k/=10;
            m++;
        } //k의 자릿수를 배열m에 저장
        //종말의 수이면 저장, 아니면 저장x
        for(int j=0;j<m;j++){
            if(arr[j]==arr[j+1] && arr[j+1]==arr[j+2] && arr[j+2]==6) {
                ind[l++]=i;
                break;
            }
        }
    }
    printf("%d\n",ind[N-1]);
    
    
    
    return 0;
}
    
   
    
    

    
    
    