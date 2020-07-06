package replay;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub



		Scanner s = new Scanner(System.in);
		int a = 0;
		int b = 0;
		int c = 0;
		
		a = s.nextInt();
		b = s.nextInt();
		c = s.nextInt();
				
		System.out.println((a+b)%c);
		System.out.println(((a%c)+(b%c))%c);
		System.out.println((a*b)%c);
		System.out.println(((a%c)*(b%c))%c);
		
	}

}
