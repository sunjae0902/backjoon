import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	private static int[] num,oparr;
	private static int N, max=-1000000000, min=1000000000;
  
	public static void dfs(int res,int dep){ 
		if(dep==N) {
			if(max<res) max=res;
			if(min>res) min=res;
			return;
		}
		else {
			for(int i=0;i<4;i++) { // 모든 연산자. 대입 
				if(oparr[i]>0) {
					oparr[i]--;
					switch(i) {
					case 0:
						dfs(res+num[dep],dep+1);
						break;
					case 1:
						dfs(res-num[dep],dep+1);
						break;
					case 2:
						dfs(res*num[dep],dep+1);
						break;
					case 3:
						dfs(res/num[dep],dep+1);
						break;	
					}
					
					
					oparr[i]++;
				}
			}		
		}	
	}
	
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		num=new int[N];  // 수열 
		oparr=new int[4];
		
	   
		StringTokenizer st=new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			num[i]=Integer.parseInt(st.nextToken());
		}
		st=new StringTokenizer(br.readLine());

		for(int i=0;i<4;i++) {
			oparr[i]=Integer.parseInt(st.nextToken()); // 각 연산자의 개수 저장 	
		}
		
		br.close();
		dfs(num[0],1);
		System.out.println(max);
		System.out.println(min);
	
	}
}
