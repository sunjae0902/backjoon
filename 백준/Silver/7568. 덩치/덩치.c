#include <stdio.h>




int main(){
    int N,j=0;
    scanf("%d",&N); //사람 수
    int x[50]={0,},y[50]={0,},rank[50]={0,}; //키,몸무게
    for (int i=0;i<N;i++) scanf("%d %d",&x[i],&y[i]);
    
    while (j<N) { //목표 사람의 인덱스 j
        for (int i=0;i<N;i++){ //비교 대상 인덱스 i
            if (x[j]<x[i] && y[j]<y[i]) rank[j]++;
        }
        j++; }
    for (int i=0;i<N;i++)
        printf("%d ",rank[i]+1);
    
    
    
    
    return 0;
    
}
