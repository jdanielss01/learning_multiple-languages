package prueba;

public class PrimeraClase {
	public static void main(String[] args) {
		//Comentario de una linea
		/*Comentario de
		de multiples lineas*/
		
		//print
		System.out.println("Hola mundo");
		
		//tipos de variables PRIMITIVOS/SIMPLE(byte, short, int, long, float, double, boolean, char)
		//numericas-enteros-byte: puede tener 512 valores posibles entre el -128 i +127
		byte VariableDeTipoByte = 34; //si fuese un numero fuera del rango eg: 300, pues da error
		//numericas-enteros-short: puede tener 65536 valores entre -32768 i +32767
		short VariabeDeTipoShort = 1000;
		//numericas-enteros-int: puede tener 4294967296 valores entre -2³¹ i +2³¹-1
		int VariableDeTipoInt = 1000000;
		//numericas-enteros-long: puede tener x valores entre -2⁶³ i +2⁶³-1
		//***Se ha de poner una l o L al final
		long VariableDeTipoLong = 100000000L;

		//numericas-decimales-float: puede ser cualquer decimal. Calcula con los 7 primeros decimales
		//***Se ha de poner una f o F al final
		float VariableDeTipoFloat = 1.0000000F;
		//numericas-decimales-double: puede ser cualquier decimal. Calcula con los 14 primeros decimales
		//***Java interpreta por defecto un numero decimal sin letra como double. La d o D es opcional
		double VariableDeTipoDouble = 1.234234D;
		
		//logica-boolean
		boolean VariableDeTipoBoolean = true;
		
		//textual-char: Puede tener solo un caracter
		//***Se ha de usar especificamente comillas simples. De lo contrario se interpreta como tipo String ???
		char VariableDeTipoChar = 'a';
		//
		
		//Tipos de variables objeto (string)
		//textual-String
		String VariableDeTipoString = "texto largo";
	}
}