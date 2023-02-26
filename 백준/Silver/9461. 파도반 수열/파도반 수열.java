import java.util.Scanner;



public class Main {
	public static long P(int N) {
		long[] arr=new long[100]; //0-99
		arr[0]=1;
		arr[1]=1;
		arr[2]=1;
		arr[3]=2;
		arr[4]=2;
		for(int i=5;i<N;i++) //5-99
			arr[i]=arr[i-1]+arr[i-5];
		return arr[N-1];
	
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb=new StringBuilder();
		long T=sc.nextInt();
		
		for(long i=0;i<T;i++) {
			int N=sc.nextInt();
			sb.append(P(N));
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
