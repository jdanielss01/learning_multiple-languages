package bucles;

public class bucles {
	public static void main(String[] args) {
		int num = 0;
		while(num < 10) {
			System.out.println(num);
			num++;
		}
		System.out.println("------");
		
		int num2 = 0;
		while(true) {
			System.out.println(num2);
			if(num2 == 5) {
				break;
			}
			num2++;
		}
		System.out.println("------");
		
		int num3 = 10;
		do {
			System.out.println(num3);
			num3++;
		}while(num3 < 20);
		
		System.out.println("------");
		
		for (int i=0; i < 10; i += 2) {
			System.out.println(i);
			if (i==6) {
				break;
			}
		}
		
		System.out.println("fin");
	}
}
