package demo.example

//TOP LEVEL varaibles
val global_Val = "cadena global-scope estatica"
var global_Var = "cadena global-scope mutable"

fun main() {
    //Declaracion y asignacion de variable de solo lectura (estatica)
    val cadena_uno = "primera cadena"
    val numero_uno = 1

    //Declaracion y asignacion de variable mutable
    var cadena_dos = "segunda cadena"
    var numero_dos = 2

    //Reasignacion
    /*cadena = "mi cadena1" INVALIDO!!!, cadena es de tipo val y no es mutable*/
    /*cadena_dos = "mi cadena2" INVALID!! la reasignacion es redundante porque la variable no ha sido usada*/
    cadena_dos = "mi " + cadena_dos
    //----------------------- Uso de variables
    //Format print
    println("Variables globales:\n${global_Val}. ${global_Var}")
    println("Variables locales:\n${numero_uno}: ${cadena_uno}. ${numero_dos}: ${cadena_dos}")

}