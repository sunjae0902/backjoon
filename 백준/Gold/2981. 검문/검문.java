import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
	
	public static int gcd(int a,int b) {
		int rem=1;
		while(rem>0) {
			rem=a%b;
			a=b;
			b=rem;
		}
		return a;
	}
		public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int[] arr=new int[N];
		int[] diff=new int[N-1];
		for(int i=0;i<N;i++) {
			arr[i]=sc.nextInt();
		}
		
		for(int i=0;i<N-1;i++) {
			diff[i]=Math.abs(arr[i+1]-arr[i]); //차이 저장 
		}
		Arrays.sort(diff);
		int gcd; 
		
		if(diff.length==1) gcd=diff[0]; 
		else gcd=gcd(diff[0],diff[N-2]);// 차이 배열에서 가장 작은 값과 가장 큰 값의 최대공약수가 차이 집합의 최대공약수임.
		
		ArrayList<Integer> result=new ArrayList <Integer>();
	    for(int i=1;i<=Math.sqrt(gcd);i++) { //최대공약수의 약수구하기 
	    	if(gcd%i==0 && i!=1) {
	    		result.add(i);
	    		if(gcd/i!=i) result.add(gcd/i);
	    	}
	    }
	    result.add(gcd);
	    Collections.sort(result);
	    for(int i:result) System.out.print(i+" ");
	    	
		
}
}
