import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
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
		public static void arraySortByName(List<String> list) {
			for(int i=0;i<list.size();i++) {
				for(int j=i+1;j<list.size();j++) {
					if(list.get(i).length()==list.get(j).length()) {
						if(list.get(i).compareTo(list.get(j))>0) {
							swap(list,i,j);
						}
					}
				}
			}
		

	
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
		
		quickSortByLen(list,0,list.size()-1);
		arraySortByName(list);
		print(list);
			
		
		
	}
	}