import java.util.Scanner;

public class Main {
	public static int min(int a,int b)
	{
		if(a<b) return a;
		else return b;
	}
	public static int cnt2(int N) {
		int ans=0;
		while(N>0) {
			N/=2;
			ans+=N;
		}
		return ans;
	}
	public static int cnt5(int N) {
		int ans=0;
		while(N>0) {
			N/=5;
			ans+=N;
		}
		return ans;
	}
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int d = n - m;
		int result;
		
		if (m==0) result=0; //0의 개수는 0
		
		else{
			result=min(cnt2(n)-(cnt2(m)+cnt2(d)),cnt5(n)-(cnt5(m)+cnt5(d)));
		}
		System.out.println(result);

	}

}