#include <stdio.h>
int main(){
    // 기본수학1-1978번
    int N,cnt=0;
    int num[101]={0,}; //수들을 저장할 배열
    scanf("%d",&N); //개수 입력
    for (int i=0;i<N;i++) scanf("%d",&num[i]);
        
    for (int i=0;i<N;i++){
        if (num[i]>=3){
            for (int j=2;j<=num[i]-1;j++){
                if (num[i]%j==0) num[i]=0;
        }
            if (num[i]!=0) cnt++;
            
    }
        else if (num[i]==2) cnt++;
    }
    printf("%d\n",cnt);
 return 0;
}

    
