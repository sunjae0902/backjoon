import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	public static int max(int a, int b){
		if (a < b) return b;
		else return a;
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		
		int[][] arr=new int[T+1][T+1];
		int[][] d=new int[T+1][T+1];
		
		for(int i=1;i<T+1;i++) {
			for(int j=1;j<i+1;j++) {
				arr[i][j]=sc.nextInt();
			}
		}//입력
		
		d[1][1]=arr[1][1]; 
		for(int i=2;i<T+1;i++) {
			for(int j=1;j<i+1;j++) {
				d[i][j]=max(d[i-1][j-1],d[i-1][j])+arr[i][j];
			}
			
		}
		Arrays.sort(d[T]);
		System.out.println(d[T][T]);
		
		
	}
}
