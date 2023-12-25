import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {
	public static void main(String[] args) throws IOException {
		int N,M,min=32;
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		int [][]arr=new int[N][M];
		
		for(int i=0;i<N;i++) {
			String str=br.readLine();
			for(int j=0;j<M;j++) {
				if(str.charAt(j)=='W') arr[i][j]=0;
				else arr[i][j]=1;
			}
		}
		
		br.close();
		
		for(int i=0;i<N-7;i++) {
			for(int j=0;j<M-7;j++) {
				int cnt1=0,cnt2=0;
				for(int k=i;k<i+8;k++) { // bwbw
					for(int m=j;m<j+8;m++) {
						 if (((k - i + m - j) % 2) == 0) {
		                        if (arr[k][m] != 1)
		                            cnt1++;    //다시 칠하기
		                    }
		                    //합이 홀수일 때
		                    else {
		                        if (arr[k][m] != 0)
		                            cnt1++;    //다시 칠하기
		                    }
					}
					
					
				}
				
				for(int k=i;k<i+8;k++) { // wbwb
					for(int m=j;m<j+8;m++) {
						 if (((k - i + m - j) % 2) == 0) { //떨어진 거리에 따라 달라지는 규칙성 발견
		                        if (arr[k][m] != 0)
		                            cnt2++;    //다시 칠하기
		                    }
		                    //합이 홀수일 때
		                    else {
		                        if (arr[k][m] != 1)
		                            cnt2++;    //다시 칠하기
		                    }
					}
					
					
				}
				min=Math.min(Math.min(cnt1,cnt2),min);
			}
		}
		System.out.println(min);
		
}
}