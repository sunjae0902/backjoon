import java.math.BigInteger;
import java.util.Scanner;
public class Main {
	public static String fact(int a) {
		BigInteger sum=new BigInteger("1");  //string형 
		int i=1; 
		while(i<=a) {
			sum=sum.multiply(BigInteger.valueOf(i));
			i++;
			
		}
		return sum.toString();
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		String str=fact(N);
		int cnt=0;
		for(int i=str.length()-1;i>=0;i--) {
			char c=str.charAt(i);
			if(c=='0') cnt++; //string에서 char단위로 접근. 괄호 안에 인덱스.
			else break;
		}
		System.out.println(cnt);
		
	}
		
}

