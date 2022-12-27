#include <stdio.h>

int main(){
    // 기본수학1-부녀회장
    int people[14][15];//호 층
    int T,k,n;
    scanf("%d",&T);
    for(int j=0;j<T;j++){
        scanf("%d\n",&k); //k층 n호
        scanf("%d",&n);
        
        for (int i=0;i<15;i++) people[0][i]=1;
        for (int i=1;i<=14;i++) people[i-1][0]=i;
        for (int a=1;a<=14;a++){
            for (int b=1;b<=13;b++){
                people[b][a]=people[b][a-1]+people[b-1][a];
            }
        }
        printf("%d\n",people[n-1][k]);
        
    }
    return 0;
}
