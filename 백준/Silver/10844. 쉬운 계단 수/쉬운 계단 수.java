import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;



public class Main {
	private static int n;
	private static long[][] arr;
    private static final long val=1000000000; 
	
	public static void dp(int n) {
		long sum=0;
		for(int i=0;i<9;i++) arr[1][i]=1; //초기화 
		for(int i=2;i<n+1;i++) {
			
			arr[i][0]=arr[i-1][1] % val;
			
			for(int j=1;j<=8;j++) {
				arr[i][j]=arr[i-1][j-1]%val+arr[i-1][j+1]%val;
				
			}
			
			arr[i][9]=arr[i-1][8] % val;
			
			
		}
		for(int i=0;i<10;i++) {
			sum+=arr[n][i];
		}
		
		System.out.println(sum%val);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n=Integer.parseInt(br.readLine());
		arr=new long[n+1][10]; //n개의 자릿값 
		
		br.close();
		
		dp(n);
		
}
}