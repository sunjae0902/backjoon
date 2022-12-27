#include <stdio.h>
#include <stdlib.h>
#define MAX 500000

int binarySearch(int a[],int l,int r,int key){//배열,처음,끝, 찾고자 하는 값
    while (l <= r) { //반복문 이용
       int mid = l + (r-l) / 2;
       
       if (a[mid] == key) // 종료 조건1 검색 성공.
         return 1;
       else if (a[mid] > key)
         r = mid - 1;
       else
         l = mid + 1;
     }
     return 0 ; // 종료 조건2 (low > high) 검색 실패.
   }

int static compare (const void* first, const void* second) //오름차순 정렬 함수
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}



int main(void){
    int N,M;
    int a[MAX],b[MAX]; //카드의 수를 저장할 배열
    int res[MAX]={-1,}; //결과를 저장할 배열
    
    scanf("%d",&N);
    for (int i=0;i<N;i++) scanf("%d",&a[i]);
    qsort(a,N,sizeof(int),compare); //상근이의 array오름차순 정렬
    
    scanf("%d",&M); //비교할 수
    for (int i=0;i<M;i++) scanf("%d",&b[i]);
    
    for (int i=0;i<M;i++){ //정렬된 상근이의 array에 대해 이진탐색(log n) 수행-> O(nlogn)
        res[i]=binarySearch(a,0,N-1,b[i]);
    }
      
    for (int i=0;i<M;i++) printf("%d ",res[i]);
     
   return 0;
}