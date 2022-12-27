#include <stdio.h>

int main(){
    // 기본수학1-분수 찾기
    int X,n,sum=1;
    scanf("%d",&X);
    
    for (n=1;n<10000000;n++){
        sum+=n;
        if(X<sum) break;
    }
    if (n%2==0) printf("%d/%d\n",1+X-(sum-n),n-(X-(sum-n)));
    else printf("%d/%d\n",n-(X-(sum-n)),1+X-(sum-n));
    return 0;
}
