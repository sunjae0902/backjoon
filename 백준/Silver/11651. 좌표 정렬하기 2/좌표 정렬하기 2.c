#include <stdio.h>
#include <stdlib.h>


typedef struct {
    int x; int y;
}coord;

int compare(const void *a, const void *b){
    coord A=*(coord *)a;
    coord B=*(coord *)b;
    if (A.y > B.y)
           return 1;
    else if (A.y == B.y)
       {
        if (A.x > B.x)
            return 1;
        else
            return -1;
       }
    return -1; 
    
}


int main(){
    int N;
    scanf("%d",&N);
    coord arr[N]; //coord형의 배열 생성.
    for (int i=0;i<N;i++){
        scanf("%d %d",&arr[i].x,&arr[i].y);
    }
    qsort(arr,N,sizeof(coord),compare);
   
    
   
    
    for (int i=0;i<N;i++){
        printf("%d %d\n",arr[i].x,arr[i].y);
    }
    
    

    
    
    


    
   
    return 0;
    
}