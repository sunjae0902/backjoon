import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;




public class Main {
	
	private static int[] col; //col[i]=j: i행의 노드가 j열에 위치함. 2차원->1차원 배열로 줄이기 
	private static int N,cnt=0;
  
	public static void Nqueen(int dep){ // 체스판의 각 가로, 세로, 대각선에 하나의 퀸만 있어야 함 
		if(dep == N) {
			cnt++; // 최종 해답 도출 
			return;
		}
		// 조건 검사  
		else {
			for(int i=0;i<N;i++) {
				col[dep]=i; // dep 행에 i번째 열의 노드에 놓아본다
				if(isPromise(dep)) { // 유망하다면, 다음 행으로 이동 
					
					Nqueen(dep+1);
				}			
			}
		}	
	}
	public static boolean isPromise(int i) { // i행에 놓일 노드가 유망한 지 
		for(int x=0;x<i;x++) {
			if(col[x]==col[i] || Math.abs(col[i]-col[x])==(i-x)) return false;
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		br.close();
	    col=new int[N];  
	    Nqueen(0);
		System.out.println(cnt);
		
	}
}
