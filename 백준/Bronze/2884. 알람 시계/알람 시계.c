#include <stdio.h>

int main() {
 //if문- 알람시계
    int H,M;
    scanf("%d %d",&H,&M);
    
    if (H>0){
        if (M>=45) printf("%d %d\n",H,M-45);
        else printf("%d %d\n",H-1,M+15);
        }
    else if (H==0) {
        if (M>=45) printf("%d %d\n",H,M-45);
        else printf("%d %d\n",23-H,M+15);
        }
    
    return 0;
}
