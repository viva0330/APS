package replay;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner s = new Scanner(System.in);
		
		int num1 = 0;	//�Է°� 1
		int num2 = 0;	//�Է°�2
		
		num1 = s.nextInt();		//�Է°�1 ����
		num2 = s.nextInt();		//�Է°�2 ����
		
		//100�� �ڸ��� ���ϱ�
		int a = num2/100;
		//10�� �ڸ��� ���ϱ�
		int b = num2%100;
		b = b/10;
		//1�� �ڸ��� ���ϱ�		
		int c = num2%10;
		
		System.out.println(num1*c);
		System.out.println(num1*b);
		System.out.println(num1*a);
		System.out.println(num1*num2);
		
		
		
		
	}

}
