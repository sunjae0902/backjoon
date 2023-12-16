import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;


public class Main {
	
	private static StringBuffer sb=new StringBuffer(); 
	private static int[] arr;
	private static boolean[] visited;
	private static int N,M;

	public static void DFS(int depth) throws IOException {
		if(depth==M+1) {
			for(int i=1;i<M+1;i++)
				sb.append(arr[i]).append(" ");
			sb.append("\n");
			return;
		}
		else {
			for(int i=1;i<N+1;i++) {
				if(!visited[i] && arr[depth-1] < i) {
					visited[i]=true;
					arr[depth]=i;
					DFS(depth+1);
					visited[i]=false;
				}
			}
		}
	
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
	
		br.close();
		Scanner sc=new Scanner(System.in);
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		visited= new boolean[N+1];
		Arrays.fill(visited,false);
		arr= new int[M+1];
		
		DFS(1);
		System.out.println(sb);
		
	}
}
