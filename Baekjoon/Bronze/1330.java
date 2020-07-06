package replay;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner s = new Scanner(System.in);
		
		int a = 0;	//첫번째 입력값
		int b = 0;	//두번째 입력값
		
		a = s.nextInt();	//a값 입력받음
		b = s.nextInt();	//b값 입력받음
		
		if(a>b) { 
			System.out.println(">");
		}
		else if(a<b) { //
			System.out.println("<");
		}
		else {
			System.out.println("==");
		}
		
		// string answer = ""
//		if a > b : answer = ">"
//		if a < b : answer = "<"
//		if a == b : answer = "=="
//
//		System.out.println(answer)
//
//		a > b ? answer = ">" : (a < b ? answer = "<" : answer = "==")
		
		
		
		
		
		
	}

}
