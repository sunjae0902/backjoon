import java.util.Scanner;

public class Main {
	public static int min(int a, int b){
		if (a < b) return a;
		else return b;
	
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int[][] arr=new int[1001][3];
		int[][] d = new int[1001][3];
		for(int i=1;i<=N;i++) 
			for(int j=0;j<3;j++) arr[i][j]=sc.nextInt();
		 //입력 . 
		//점화식(마지막에 0번째 빨간색 선택한 경우): d[i][0]=min(d[i-1][1],d[i-1][2])+arr[i][0]
		d[0][0]=d[0][1]=d[0][2]=arr[0][0]=arr[0][1]=arr[0][2]=0;  //초기화 
		for(int i=1;i<=N;i++) {
			d[i][0]=min(d[i-1][1],d[i-1][2])+arr[i][0]; //i번째에 빨간색을 칠한 경우 ->i-1번째에는 초록/파랑 중 하나, 그 중 최소를 선택  
			d[i][1]=min(d[i-1][0],d[i-1][2])+arr[i][1];//이전값을 배열에 저장해놓고 그 값을 참조하여 다음값을 도출함. 
			d[i][2]=min(d[i-1][0],d[i-1][1])+arr[i][2];
		}
		//첫번째 집으 색을 칠하는 경우에 따라 케이스 분류 후 각각 최소를 계산하고 그 중 최소의 경우를 도출한다. 
		
		
		
		System.out.println(min(d[N][0],min(d[N][1],d[N][2])));
		
	}
}
