#include <stdio.h>

int main(){
    // 기본수학1-10757번

    // 기본수학1-ACM호텔
    int N,H,W,T,sum=0,i;
    scanf("%d\n",&T); //테스트
    for (int j=0;j<T;j++){
        scanf("%d %d %d",&H,&W,&N);
        for (i=1;i<=W;i++){
            sum=1+H*(i-1);
            if (sum<=N && N<sum+H) break;
    }
        printf("%d\n",100*(N-sum+1)+i);     
    }
    return 0;
}

    