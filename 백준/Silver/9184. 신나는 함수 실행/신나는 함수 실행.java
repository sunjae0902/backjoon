import java.util.Scanner;



public class Main {
	static int[][][] dp=new int[21][21][21];
	public static int w(int a,int b,int c) {
		if(inRange(a,b,c)&&dp[a][b][c]!=0) return dp[a][b][c]; //배열의 범위를 넘지 않으면서 이미 값이 존재할 경우 해당 값을 바로 반환. 
		if(a<=0 || b<=0 || c<=0) return 1;
		if(a>20 || b>20 || c>20) return dp[20][20][20]=w(20,20,20); //최솟값이 20이상일때부터는 모두 같은 값이므로: 바로 배열에 값을 저장한 후 반환한다. 
		if(a<b && b<c) return dp[a][b][c]= w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
		return dp[a][b][c]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
	}
	/*
	 재귀와 메모제이션. 메모제이션: 처음 방문하면 그 값을 메모리(배열)에 저장해놓고, 이후 재방문 할 경우 저장된 값을 사용하는 것.
	  여기에서는 3차원 배열 dp[0..20][][]을 이용한다.
	 
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb= new StringBuilder(); //더 안정적인 StringBuilder 사용 
		int a=0,b=0,c=0;
		
		while(true) {
			a=sc.nextInt(); 
		    b=sc.nextInt(); 
			c=sc.nextInt(); 
			if(a==-1&&b==-1&&c==-1) break;
			sb.append("w(" + a + ", " + b + ", " + c + ") = ").append(w(a ,b ,c)).append('\n');
			
		}
		System.out.println(sb);
	}
	 /*  배열을 참조하려 할 때 a, b, c 중 하나라도 범위 밖의 수가
	 *  나올 수 있기 때문에 이를 체크를 해주기 위한 함수다.
	 */
	static boolean inRange(int a, int b, int c) {
		return 0 <= a && a <= 20 && 0 <= b && b <= 20 && 0 <= c && c <= 20; 
	}
}


