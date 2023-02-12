import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc=new Scanner(System.in);
		while(true) { //x,y가 둘 다 0이면 종료 
			int x=sc.nextInt();
			int y=sc.nextInt();
			if (x==0 && y==0) return;
			
			if(y%x==0) { //첫번째 수가 두번째 수의 약수이다 
				System.out.println("factor");
			}
			if(x%y==0) { //첫번째 수가 두번째 수의 배수이다 
				System.out.println("multiple");
			}
			if(y%x!=0&&x%y!=0)  System.out.println("neither");
			
		}
		
		
	}

}
