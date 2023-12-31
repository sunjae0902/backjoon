#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 10000

int compare(const void *a,const void *b){
    return strcmp(*(char **)a,*(char **)b);
    
}

int binarysearch(char *s[],int l,int r, char *value){
    if(l<=r){
        int m = (l+r)/2;
        int res = strcmp(value,s[m]);
        if(res == 0) return 1;
        else if (res < 0)
            return binarysearch(s,l,m-1,value);
        else
            return binarysearch(s,m+1,r,value);
    }
    else 
        return 0;
}


int main(void){
    int N,M,cnt=0;
    
    scanf("%d %d",&N,&M);
    
    char *s[MAX];
    char temp[500];
  
    for (int i = 0; i < N; i++) {
        scanf("%s",temp);
        s[i]=(char *)malloc(strlen(temp)+1);
        strcpy(s[i],temp);
    }
    
    qsort(s,N,sizeof(char *),compare); // 정렬
    
    for (int i = 0; i < M; i++) {
        scanf("%s",temp);
        cnt+=binarysearch(s,0,N-1,temp);
        
    }
    printf("%d\n",cnt);
    
    for (int i = 0; i < N; i++) {
        free(s[i]);
    }
    
    return 0;
}
