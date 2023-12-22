import java.util.Scanner;

public class Main {
	public static int max(int a,int b) {
		if(a>b) return a;
		else return b;
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int[] arr=new int[N+2];
		int[] d=new int[N+2];
		
		for(int i=1;i<N+1;i++) {
			arr[i]=sc.nextInt();
		}
		//1) 전전 계단을 밟고, 마지막 계단을 밟는 경우
		//2) 전계단을 밟고, 마지막 계단을 밟는 경우-> 연속으로 3계단을 밟지 않도록 조건을 추가해야함. (그 전에는 무조건 두칸전에서)
		
		
		//초깃값 설정
        arr[0]=0;
		d[0]=0;
		d[1]=arr[1];
		d[2]=arr[1]+arr[2]; //계단이 2개 이하일때. 각 초깃값으로 설정. 
		
		for(int i=3;i<N+1;i++) {
			d[i]=max(d[i-3]+arr[i-1],d[i-2])+arr[i];
		}
		System.out.println(d[N]);
		
		
	}
}
