package replay;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner s = new Scanner(System.in);
		
		int a = 0;	//ù��° �Է°�
		int b = 0;	//�ι�° �Է°�
		
		a = s.nextInt();	//a�� �Է¹���
		b = s.nextInt();	//b�� �Է¹���
		
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
