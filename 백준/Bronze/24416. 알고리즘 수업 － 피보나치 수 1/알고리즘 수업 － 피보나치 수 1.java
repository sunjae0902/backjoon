import java.util.Scanner;



public class Main {
	static int recurCnt=0;
	public static int fibo1(int n) {
		if(n<=2) {
			recurCnt++;
			return 1;
		}
		else{
			return fibo1(n-1)+fibo1(n-2);
		}
		}
	
	public static int fibo2(int n) {
		int cnt=0;
		int[] arr=new int[n];
			arr[0]=1;
			arr[1]=1;
			for(int i=2;i<n;i++) {
				cnt++;
				arr[i]=arr[i-2]+arr[i-2];
			}
			return cnt;
		}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt(); 
		fibo1(n);
		System.out.println(recurCnt+" "+fibo2(n));
	}		
}
