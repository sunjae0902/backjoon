#include <stdio.h>

int main() {
   // 블랙잭 변형 게임
    int n,m;
    int arr[100];
    
    scanf("%d %d",&n,&m); //n,m입력
    for (int i=0;i<n;i++) scanf("%d",&arr[i]); //카드에 쓰인 수 입력 후 저장
    
    int sum=0,max=0;
    for (int i=0;i<n-2;i++){
        for (int j=i+1; j<n-1;j++){
            for (int k=j+1;k<n;k++){
                sum=arr[i]+arr[j]+arr[k]; //삼중 반복문: 모든 경우의 수 저장
                if (sum<=m && sum>max)
                    max=sum;   // m이하 최대 값을 찾아서 Max변수에 저장
            }
        }
    }
    
    printf("%d\n",max);
    return 0;
}
