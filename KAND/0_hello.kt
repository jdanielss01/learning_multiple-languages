//Entrypoint
fun main(arguments: Array<String>) {
	//SINGLE LINE COMMNET
	
	/*
	MULTI-LINE COMMENT
	*/
	
	//PRINTING
	println("texto con salto de linea al final i argumento: ") //+ arguments[0])
	print("texto sin salto de linea")
	
	
	//VARIABLES AND TYPES
		/* notas
		 * 2 tipos var(para variables mutables) o val(para variables inmutables/final)
		 * si no hay tipado se asigna el tipo segun el contexto de entrada -> 1--int, "h"--String, 'c'--char
		 
		 
		Names can contain letters, digits, underscores, and dollar signs
		Names should start with a letter
		Names can also begin with $ and _ (but we will not use it in this tutorial)
		Names are case sensitive ("myVar" and "myvar" are different variables)
		Names should start with a lowercase letter and it cannot contain whitespace
		Reserved words (like Kotlin keywords, such as var or String) cannot be used as names
		Camelcase
		*/
		//String (characters group)
			var var1: String; //initialization (typed required)
			var1 = "string con tipo"	//assigment auto-typed
			val var2 = "string sin tipo"	// static variable
			//var2 = "da error"	// error: val cannot be reassigned
		
		//Char (characters group)
			val caracter: Char = 'a' // = 11 is converted to char
		
		//(numbers-integer group)
			//Int
				val entero: Int = 100000
			//Short
				val corto: Short = 32767
			//Long
				val largo: Long = 15000000000L
			//Byte
				//val byton: Byte = 
		
		//(numbers-float group)	
			//Double
			val doble: Double = 1.2
			val flotante: Float = 1.1F
			//scientific numbers

		//Boolean (booleans group)
			val booleano: Boolean = true //false
		
		//Array (array group)
			val myarray: Array<Int> = arrayOf(1, 2, 3)
			myarray[0] = 2
			println(" my array: " + myarray[0])
		
		//Classes
		
	//CONVERSIONS var.toType()
		entero.toString()
		//...
	//OPERTATIONS: 
		//concatenation 
		//aritmetical operators: +, -, *, /, %, ++, --, 
		//asignment operators: +=, -=, *=, /=, %=
		//boolean/comparison operators: ==, !=, >, <, >=, <=
		//logic operators: !, ||, &&
}
