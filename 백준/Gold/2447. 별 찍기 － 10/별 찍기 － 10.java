import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main  {
	private static int N;
	private static char[][] arr;
	public static void myrecur(int i,int j,int N) { // x,y,n
		if(N==1) {
			//arr[i][j]='*';
			return;
		}
		else if(i/(N/3)%3==1 && j/(N/3)%3==1 ) {
			arr[i][j]=' ';
		}
		myrecur(i,j,N/3);
		
	}
	public static void main(String[] args) throws IOException{
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb =new StringBuilder();
		N=Integer.parseInt(br.readLine());
		br.close();
		arr=new char[N][N];
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				arr[i][j]='*';
			}
		}	
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				myrecur(i,j,N);
				sb.append(arr[i][j]);
			}
			sb.append('\n');
		}	
		System.out.print(sb);
		
	}

	}