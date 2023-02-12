
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
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int[] arr=new int[N];
		for(int i=0;i<N;i++) {
			arr[i]=sc.nextInt();
		}
		for(int i=0;i<N-1;i++) {
			System.out.println(arr[0]/gcd(arr[i+1],arr[0])+"/"+arr[i+1]/gcd(arr[i+1],arr[0]));
		}
		
	}
		
}