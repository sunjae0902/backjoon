import java.util.Scanner;

public class Main {
	public static int Binomial(int m,int n) {
		int[] arr=new int[n+1];
		arr[0]=1;
		for(int i=1;i<=m;i++) {
			for(int j=n;j>0;j--) {
				arr[j]+=arr[j-1];
			}
		}
		return arr[n];
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		for(int i=0;i<T;i++) {
			int N=sc.nextInt();
			int M=sc.nextInt();
			int result=Binomial(M,N);
			System.out.println(result);
			}
		
	}
		
}