import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {
	private static int n;
	private static int[] arr;

	
	public static void dp() {
		int max=-1000000000;
		
		for(int i=1;i<n;i++) {
			arr[i]=Math.max(arr[i-1]+arr[i],arr[i]);
		}
		for(int i=0;i<n;i++) {
			if(arr[i]>max) max=arr[i];
		}
		System.out.println(max);
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n=Integer.parseInt(br.readLine());
		
		arr=new int[n];
		StringTokenizer st=new StringTokenizer(br.readLine());
		br.close();
		
		for(int i=0;i<n;i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		
		dp();
		
}
}