
public class condicionales {
	public static void main(String[] args) {
		//***Se pueden dejar de usar las llaves si la condicion conlleva solo una instruccion
		int num1 = 10;
		int num2 = 20;
		if (num1 > num2) {
			System.out.println("El num " + num1 + " es major a " + num2);
		}if (num1 == num2) {
			System.out.println("El num " + num1 + " es igual a " + num2);
		}else {
			System.out.println("El num " + num1 + " es menor a " + num2);
		}
		
		
		if (num1 > num2) {
			System.out.println("El num " + num1 + " es major a " + num2);
		}else if (num1 == num2) {
			System.out.println("El num " + num1 + " es igual a " + num2);
		}else {
			System.out.println("El num " + num1 + " es menor a " + num2);
		}
		
		String resultat = (num1 == num2) ? "Son numeros iguales" : "No son numeros iguales";
		System.out.println(resultat);
		
		if (!(num1 == num2)) { 
			System.out.println("No son iguales");
		}
		
		switch(num1) {
		case 0:
			System.out.println("es igual a 0");
			break;
		case 5:
			System.out.println("es igual a 5");
			break;
		case 10:
			System.out.println("es igual a 10");
			break;
		case 15:
			System.out.println("es igual a 15");
			break;
		default:
			
		}
	}
}
