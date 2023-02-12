
import java.util.Scanner;

public class Main {
	public static int gcd(int a,int b) {
		int rem=1;
		while(rem>0) { 
			rem=a%b;
			a=b;
			b=rem;
		}
		return a;
	}

	public static void main(String[] args) {
		int lcm;
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		for(int i=0;i<T;i++) {
			int n1=sc.nextInt();
			int n2=sc.nextInt();
			lcm=n1*n2/gcd(n1,n2);
			System.out.println(lcm);
	}
	}

}