#include <stdio.h>
#define swap(a,b) {int t; t=a; a=b; b=t;}

void countingSort(int a[],int N){ //배열의 사이즈
    int cnt[8001]={0,};
    int k=0;
    for (int i=0;i<N;i++){
        cnt[a[i]+4000]++; //배열의 각 원소가 몇번 나오는지 저장
    }
   
    for (int i=0;i<8001;i++){
        for (int j=0;j<cnt[i];j++)
            a[k++]=i-4000;
            }
            
    
        
}

int main(){
    
    int N,arr[500000]={0,},arr2[8001]={0,};
    int i;
    double sum=0.0;
    
    scanf("%d",&N);
    
    for (i=0;i<N;i++){
        scanf("%d",&arr[i]);
        arr2[arr[i]+4000]++; //goto line 37
    }
    countingSort(arr,N);
 
    
    for (int i=0;i<N;i++) sum+=arr[i];
     //총합구하기
    
    int two=arr[(N-1)/2];
    printf("%d\n%d\n",sum<0 ?(int)(sum/N-0.5):(int)(sum/N+0.5),two); // 산술 평균,중앙값
    
    //최빈값
    int max=0,flag=0;
    for (int i=0;i<8001;i++){
        if (arr2[i]>max){
            max=arr2[i];
            flag=i; //flag는 최빈값들 중 가장 작은 값의 인덱스 (max보다 arr2[i]값이 커야만 업데이트되기 때문에)
        }
    }
    
    for (int i=flag+1;i<8001;i++){
        if (max==arr2[i]) {
            flag=i; //중복 값이 나타날 경우 바로 다음값으로 업데이트. (최빈값 중 두번째로 작은 값)
            break;
       }
    }
    printf("%d\n",flag-4000); //최빈값
    printf("%d\n",arr[N-1]-arr[0]); //범위

    
   
    return 0;
    
}