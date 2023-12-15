import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
//bufferedreader+stringbuffer 사용

public class Main {
	
	private static StringBuffer sb=new StringBuffer(); 
	private static int[] arr;
	private static boolean[] visited;

	public static void DFS(int n, int m, int depth) throws IOException {
		if(depth==m+1) {
			for(int i=1;i<m+1;i++)
				sb.append(arr[i]).append(" ");
			sb.append("\n");
			
			return;
		}
		else {
			for(int i=1;i<n+1;i++) {
				if(!visited[i]) {
					visited[i]=true;
					arr[depth]=i;
					DFS(n,m,depth+1);
					visited[i]=false;
				}
			}
		}
	
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		br.close();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		visited= new boolean[N+1];
		Arrays.fill(visited,false);
		arr= new int[M+1];
		
		DFS(N,M,1);
		System.out.println(sb);
		 
		
	}
}
