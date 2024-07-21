package importar_Clases;
public class classname {
	//Atributos
	int AtributoInt;
	String AtributoString;
	//Constructores
	public classname (int ArgumentoInt, String ArgumentoString){
		this.AtributoInt = ArgumentoInt;
		this.AtributoString = ArgumentoString;
	}
	public classname() {
		System.out.println("Constructor que no hace nada. Por defecto ya se crea un costructor vacion para llamar a los objetos");
	}
	
	
	//Metodos
	void metodname1() {
		System.out.println("esto es un metodo sin salida ni argumentos de entrada");
	}
	int metodname2(int ArgumentoInt) {
		int suma = 1 + ArgumentoInt;
		System.out.println("ESTO ES UN METODO QUE USA UN ARGUMENTO DE TIPO INT PARA SUMAR"
				+ " Y DEVOLVER ESTE RESULTADO DE TIPO INT:" + suma);
		return suma;
	}
}
