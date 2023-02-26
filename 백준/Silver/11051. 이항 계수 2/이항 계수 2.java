import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	public static int Binomial(int n,int k) {
		int [] arr=new int [k+1]; //일차원 배열 arr[0..k]에 저장. 
		for(int i=0;i<arr.length;i++) arr[i]=0; 
		arr[0]=1; //k=0인 경우 항상 1.
		
		for(int i=1;i<=n;i++) { //1부터 n까지 반복 
			for(int j=k;j>0;j--) {
				BigInteger bignum= BigInteger.valueOf(arr[j]+arr[j-1]); //큰 수를 저장해야하므로 BigInteger 사용
				arr[j]=bignum.intValue()%10007; //다시 int형으로 변환 후 나머지를 arr배열에 저장
			}
		}
		return arr[k];
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int K=sc.nextInt();
		int result=Binomial(N, K);
		System.out.println(result);
		
	}
		
}

