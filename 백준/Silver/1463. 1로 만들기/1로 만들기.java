import java.util.Scanner;

public class Main {
	public static int min(int a,int b) {
		if(a<b) return a;
		else return b;
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int[] dp=new int[N+2]; //1-N , 최대 계산: 1을 N-1번 빼는 것. 
		dp[1]=0;
		dp[2]=1;
		
		for(int i=3;i<N+1;i++) {
			if(i%2!=0 && i%3!=0) dp[i]=dp[i-1]+1; //2와 3모두로 나누어지지 않는 경우-> 무조건 -1해야함. =d[i-1]과 같은 값. 
			else if(i%2==0 && i%3!=0) dp[i]=min(dp[i-1],dp[i/2])+1;  //2로는 나눠지면서 3으로는 나눠지지 않는 경우. 
			else if(i%2!=0 && i%3==0) dp[i]=min(dp[i-1],dp[i/3])+1; //2로 나눠지지 않고 3으로만 나눠지는 경우 
			else dp[i]=min(dp[i-1],min(dp[i/2],dp[i/3]))+1; //둘 다 나눠지는 경우 세 가지 연산 중 최소 선택. 
					
}
		sc.close();
		System.out.println(dp[N]);
	
		
	}
}
