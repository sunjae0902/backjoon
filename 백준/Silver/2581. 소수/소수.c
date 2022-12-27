#include <stdio.h>

 
int min(int a[],int n){ //배열에서 최솟값을 찾는 함수
    int min=a[0];
    for (int i=0;i<n;i++){
        if (min>a[i]) min=a[i];
    }
    return min;
}

int main(){
    // 기본수학1-2581번
    int N,M,cnt=0,j=0,sum=0;
    int a[10000]={0,};
    int b[10000]={0,};
    
    scanf("%d %d",&M,&N);
    
    for (int i=M;i<=N;i++){
        if (i==2) a[i-M]=2;
            
        else if (i>=3){
            for (int j=2;j<=i-1;j++){
                if (i%j==0) goto end; //나눠떨어지는 순간 탈출
            }
            a[i-M]=i;
            }
    end:
        continue;
    }
    for (int i=0;i<=N-M;i++){
        if (a[i]!=0) {//0이아닌 소수일 경우
            cnt++;
            b[j++]=a[i]; }
    }
    
    if (cnt==0) printf("%d\n",-1);
    else
    {
        for (int i=0;i<=j;i++)
            sum+=b[i];
        
        printf("%d\n",sum);
        printf("%d\n",min(b,cnt));
    }
    
       
    
    

 return 0;
}

    
