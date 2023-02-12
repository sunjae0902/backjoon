import java.util.Scanner;

public class Main {
	public static void swap(int a,int b) { //최댓값을 반환하는 max메서드 선언 
		int t=a;
		a=b;
		b=t;
	}
	public static void main(String[] args) {
		int gcd,lcm; //최대공약수, 최소공배수 
		Scanner sc=new Scanner(System.in);
		int num1=sc.nextInt();
		int num2=sc.nextInt();
		int mul=num1*num2;
		if(num2>num1) swap(num1, num2); //둘 중 큰 값이 Num1으로.
		
		int rem=1;
		//유클리드 알고리즘
		while(rem>0 && rem<=num2) {
			rem=num1%num2; 
			num1=num2;  
			num2=rem; 
		}
		gcd=num1;
		System.out.println(gcd);
		
		//최소공배수
        lcm=mul/gcd;
		System.out.println(lcm);
		}
	}


