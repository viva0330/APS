package replay;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner s = new Scanner(System.in);
		
		int num1 = 0;	//입력값 1
		int num2 = 0;	//입력값2
		
		num1 = s.nextInt();		//입력값1 받음
		num2 = s.nextInt();		//입력값2 받음
		
		//100의 자리수 구하기
		int a = num2/100;
		//10의 자리수 구하기
		int b = num2%100;
		b = b/10;
		//1의 자리수 구하기		
		int c = num2%10;
		
		System.out.println(num1*c);
		System.out.println(num1*b);
		System.out.println(num1*a);
		System.out.println(num1*num2);
		
		
		
		
	}

}
