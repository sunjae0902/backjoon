import java.util.Scanner;

public class Main {
	public static int min(int a, int b) {
		if(a>b) return b;
		else return a;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x=sc.nextInt();
		int y=sc.nextInt(); 
		int w=sc.nextInt(); 
		int h=sc.nextInt(); 

		System.out.println(min(min(w-x,h-y),min(x,y)));
}		
}
