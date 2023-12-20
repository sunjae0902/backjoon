import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {
	private static StringBuffer sb=new StringBuffer();
	private static int[][] arr;

	public static void dfs(int row, int col){ 
		if(col==10) {
			dfs(row+1,1); //다음행으로 이동  
			return;
		}
		if(row==10) { //종료 
			for(int i=1;i<10;i++) {
				for(int j=1;j<10;j++) {
					sb.append(arr[i][j]).append(" ");
				}
				sb.append("\n");
			}
            System.out.print(sb);
			System.exit(0);
			
		}
		else {
			if(arr[row][col]==0) {
				for(int j=1;j<10;j++) {
					if(isPromise(row,col,j)) { // J값이 유망하다면 
						arr[row][col]=j;
						dfs(row,col+1);
					}
				}
				arr[row][col]=0; // 초기화, 답을 못찾았을 경우 
				return;
			}
			dfs(row,col+1); //빈칸이 아닌 경우 -> 옆으로 한 칸 이동.
			
		}
		
					
	}
	public static boolean isPromise(int row, int col, int val) {
		
		int row2 = (row<=3) ? 1 : (row<=6) ? 4 : 7;
		int col2 = (col<=3) ? 1 : (col<=6) ? 4 : 7;
		
		for(int i=1;i<10;i++){ // 행, 열 검사 
			if(arr[row][i]==val || arr[i][col]==val) return false; 
		}
		for(int k=row2;k<row2+3;k++) { // 사각형 
			for(int j=col2;j<col2+3;j++) {
				if(arr[k][j]==val) return false;
			}
		}
		return true;
	}
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		arr=new int[10][10];

		
		for(int i=1;i<10;i++) {
			st=new StringTokenizer(br.readLine());
			for(int j=1;j<10;j++) {
				arr[i][j]=Integer.parseInt(st.nextToken()); // 각 연산자의 개수 저장
			}
		}
		dfs(1,1);
		
		
		br.close();

	}
}
