
public class Clase_operadores_bucles {
	public static void main(String[] args) {
		//OPERADOR DE CONCATENACION
		//+ : JUNTA DOS String en uno solo
		//OPERADORES ARITMETICOS(+, -, *, /,%)
		//Creacion de variables con operadores: Se puede hacer operaciones tanto con datos numericos insertados o guardados en otras variables 
		//
		int SumaConDatos = 10 + 20;
		int num1 = 10;
		int num2 = 20;
		int SumaConVariables = num1 + num2;
		int Resta = num2 - num1;
		int Multiplicacion = num1 * num2;
		int Division = num2 / num1;
		int Modulo = num1 % num2;
		
		//**Se puede asignar el valor de una variable a otra variable
		int TmpVar = num1;
		
		//OPERADORES DE ASIGNACION(=)
		//El igual: Asigna a una variable el valor que tenga detras del igual i que se corresponda con su tipo
		//Los preoperadores: Simplifican una operacion de 2, se utuliza cuando cuando se quiere actualizar una variable ya declarada
		//***CUANDO SE ACTUALIZA UNA VARIABLE NO HACE FALTA ESPECIFICAR EL TIPO YA QUE YA LO TIENE ASIGNADO
		//preoperador mas-igual(+=):
		num1 += 2; 
		//preoperador menos-igual(-=):
		num1 -= 1;
		//preoperador por-igual(*=):
		num1 *= 1;
		//preoperador dividido-igual(+=):
		num1 /= 2;
		//preoperador modulo-igual
		
		//OPERADORES UNITARIOS (O DE SIMBOLO O ENTEROS POSITIVOS Y NEGATIVOS)
		int positivo = +10;
		int negativo = -10;
		
		//OPERADORES INCRIMENTALES(suman 1 o restan 1)
		num1++;
		num1--;
		
		//OPERADORES RELACIONALES (mayor que >, menor que <, igual a ==, no igual a !=, igual-mayor que =>, igual-menor que =< )
		//*** Devuelen datos de tipo boolean
		
		//OPERADORES LOGICOS (opera con condiciones o boolean)
		//AND - &&
		boolean var1  =  1 == 1 && 2 == 2;
		//OR - ||
		boolean var2  =  1 == 1 || 2 == 3;
		//NOT - !
		boolean var3  = !(1==2);
		
		//OPERADORES DE BITS
				// CAMBIO A DERECHAS - >>
				// CAMBIO A IZQUIERDAS - <<
				// CAMBIO TOTAL A DERECHA - >>>
				// CAMBIO TOTAL A IZQUIERDA - <<<
				// AND - &
				// OR - |
	}	
}
