import java.util.Scanner;

public class Main {
	public static int fact(int a) {
		int sum=1;
		for(int i=1;i<=a;i++) sum*=i;
		return sum;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int K=sc.nextInt();
		int result=fact(N)/(fact(K)*fact(N-K));
		System.out.println(result);
	}
		
}
