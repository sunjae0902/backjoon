import java.util.Scanner;



public class Main {
	
	public static int solve(int N) { //점화식을 발견하자. N==k일때, k-1인 경우에서 1이 1개 추가된 경우(=1가지)와 k-2인 경우에서 00이 1개 추가된 경우(=1가지)의 합으로 나타낼 수 있다. 
		int[] arr=new int[N+1];
		arr[0]=1; 
		arr[1]=1;
		for(int i=2;i<N+1;i++) arr[i]=(arr[i-1]+arr[i-2])%15746;
		return arr[N];
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		System.out.println(solve(N));
		}
}


