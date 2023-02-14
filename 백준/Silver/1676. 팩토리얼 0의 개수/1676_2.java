Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int n=0;
	
		if(N==0) n=1;
		while(N>1) { //N!에 5가 몇번 곱해졌는지 구하는 코드.
			N/=5;
			n+=N;
			}
		System.out.println(n);
		
