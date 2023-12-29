import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main  {
	private static int N,M,cnt=0;
	public static void main(String[] args) throws IOException{
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String s=br.readLine();
		N=Integer.parseInt(s.split(" ")[0]);
		M=Integer.parseInt(s.split(" ")[1]);
		Map<String,Integer> hmap=new HashMap<String,Integer>();
		
		for(int i=0;i<N;i++) {
			hmap.put(br.readLine(),0); // key: not 중복 
		}
		
		for(int i=0;i<M;i++) {
			String str=br.readLine();
			if(hmap.containsKey(str)) cnt++;
		}
		br.close();
		System.out.println(cnt);
		
		
	}




	}