import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Main {
	
	
		
		public static void print(List<String> list) {
			for(String s:list) System.out.println(s);
		}
		
		public static void swap(List<String> list, int i, int j) {
			String temp=list.get(i);
			list.set(i,list.get(j));
			list.set(j,temp);
		}
		
		public static void quickSortByLen(List<String> list, int l, int r) {


			if(l>=r) return;
			else {
				int pv=l; // 가장 왼쪽 인덱스를 피봇으로 저장 
				int low=l+1;
				int high=r;
				
				while(low<=high) {
					while (low <= r && (list.get(low).length() <= list.get(pv).length())) {
						low++; // 오른쪽 방향으로 탐색 , 피벗의 길이보다 큰 값을 만날 때까지
					 }
					while(high > l && (list.get(high).length() >= list.get(pv).length())) {
						high--; // 왼쪽으로 탐색 피벗 요소의 길이보다 짧은 길이의 문자열을 만날 때 까지 
					}
					if(low > high) swap(list,high,pv); // 엇갈릴 경우 Pv과 교체 
					else swap(list,low,high); //교체 
					     
					
				}
				quickSortByLen(list, l, high - 1); // 피봇 기준 좌측 값들에 대해 정렬 
			    quickSortByLen(list, high + 1,r); // 우측 값들에 대해 정렬 
				
			}
			
			
		}
		
		public static void arraySort(List<String> list) {
			list.sort(new Comparator<String>() {
				public int compare(String s1, String s2) {
					// 단어 길이가 같을 경우 
					if (s1.length() == s2.length()) {
						return s1.compareTo(s2); // 사전식 정렬 
					} 
					// 그 외의 경우 
					else {
						return s1.length() - s2.length(); // 길이로 정렬 
					}
				}
			});	
		
	}
	
	
	public static void main(String[] args) throws IOException{
		int N;
		List<String> list=new ArrayList<String>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N=Integer.parseInt(br.readLine());
			
		for(int i=0;i<N;i++) {
			String str=br.readLine();
			if(!list.contains(str.toString()))
				list.add(str);
			}
		br.close();
		
//		quickSortByLen(list,0,list.size()-1);
//		arraySortByName(list);
		arraySort(list);
		print(list);
			
		
		
	}
	}