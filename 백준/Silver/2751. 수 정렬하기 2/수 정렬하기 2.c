#include <stdio.h>
#include <stdlib.h> //rand함수
#include <time.h>
#define n 1000000
#define swap(a,b) {int t=a; a=b; b=t;}
/*
int isSorted(int a[],int R){ //배열이 정렬되었는지 확인하는 함수.
    int i=0,j=0;
    if (a[i]<=a[i+1]){
        while (++i<=R) {
            if (a[i]>a[i+1]) return -1;
        }
        return 0; //오름차순으로 정렬됨
    }
    
    else{
        while (++j<=R) {
            if (a[j]<a[j+1]) return -1;
        }
        return 1; //내림차순으로 정렬됨
    }
} */

void Shuffle(int a[],int R){
    srand(time(NULL));
    for (int i=0;i<(R+1)/2;i++){
        int c,b;
        b=rand()%(R+1);
        c=rand()%(R+1);
        swap(a[b], a[c]);
    }
}

void quicksort(int a[],int L,int R){ //L: 배열의 맨 왼쪽 R: 배열의 가장 오른쪽
    int left=L; int right=R;
    int pv=a[(L+R)/2];
    
    do{
        while (a[left]<pv) {
            left++;
        }
        while (a[right]>pv) {
            right--;
        }
        if (left<=right) {
            swap(a[left],a[right]);
            left++;
            right--;
        }
        }while(left<=right);
    
    if(L<right) quicksort(a,L,right);
    if (left<R) quicksort(a,left,R);
}
   

int main(void) {
    int N;
    scanf("%d",&N);
    int a[n]={0,};
    for (int i=0;i<N;i++){
        scanf("%d",&a[i]);
    }
    //최악의 경우를 막기 위해 정렬 전에 배열의 요소를 랜덤으로 섞어주기
    Shuffle(a, N-1);
  
    quicksort(a, 0, N-1);
    for (int i=0;i<N;i++){
        printf("%d ",a[i]);}
   
    
   
   
return 0;
}