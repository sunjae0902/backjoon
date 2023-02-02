#include <stdio.h>
#define MAX 100001

/*int arr[MAX][2]={0,};
int temp[MAX][2]={0,};

-> 2차원배열을 구조체 배열로. 훨씬 더 편함*/

typedef struct {
    int x;
    int y;
}Coordinate;
Coordinate arr[MAX];
Coordinate tempArr[MAX];

void Mergesort(Coordinate arr[],int left, int right){
    int mid=(left+right)/2;
    int cmpIdxLeft = left, cmpIdxRight = (left + right) / 2;
    int copyIdx = left;
    
    if(mid-left>1) //반으로 나누었을 때 또 mergesort 호출-> merge함수와 합쳐 구현하기.
        Mergesort(arr,left,mid);
    if(right-mid>1)
        Mergesort(arr,mid,right);
    while(cmpIdxLeft<mid && cmpIdxRight<right){ //x,y 조건 한번에 입력->함수포인터로..
        if(arr[cmpIdxLeft].x<arr[cmpIdxRight].x||(arr[cmpIdxLeft].x==arr[cmpIdxRight].x&&arr[cmpIdxLeft].y <= arr[cmpIdxRight].y))
            tempArr[copyIdx++]=arr[cmpIdxLeft++];
        else
            tempArr[copyIdx++]=arr[cmpIdxRight++];
    }
    while (cmpIdxLeft<mid) {
        tempArr[copyIdx++]=arr[cmpIdxLeft++];
    }
    while (cmpIdxRight<right) {
        tempArr[copyIdx++]=arr[cmpIdxRight++];
    }
    for(int i=left;i<right;i++)
        arr[i]=tempArr[i];
    
}

int main() {
    int N;
    scanf("%d",&N);
    for (int i=0;i<N;i++) scanf("%d %d",&arr[i].x,&arr[i].y); //x,y좌표 입력
    Mergesort(arr,0,N);
    for (int i=0;i<N;i++) printf("%d %d\n",arr[i].x,arr[i].y);
    
    return 0;
}