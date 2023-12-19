import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	private static int[][] arr;
	
	private static int N,min=99;
	private static boolean[] visited;
  
	public static void dfs(int ind,int depth){ 
		if(depth==N/2) {
			int res1=0,res2=0;
			for (int i = 0; i < N - 1; i++) {
				for (int j = i + 1; j < N; j++) {
					if (visited[i]&& visited[j]) {
						res1 += arr[i][j];
						res1 += arr[j][i];
					}
					else if (!visited[i]&& !visited[j]) {
						res2 += arr[i][j];
						res2 += arr[j][i];
					}
				}
			}
			
			if(Math.abs(res1-res2)<min) min=Math.abs(res1-res2);
			return;
		}
		{
			for(int i=ind;i<N;i++) {
				if(!visited[i]) {
					visited[i]=true;
					dfs(i+1,depth+1);
					visited[i]=false;	
				}	
			}
			
		}
		
					
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		arr=new int[N][N];
		visited=new boolean[N]; // 스타트 팀에 들어갈 사람 
		for(int i=0;i<N;i++) {
			st=new StringTokenizer(br.readLine());
			for(int j=0;j<N;j++)
				arr[i][j]=Integer.parseInt(st.nextToken()); // 각 연산자의 개수 저장 	
		}
		
		br.close();
		dfs(0,0);
		
		System.out.println(min);
	
	}
}
