#!/bin/bash

#DECLARACION DE VARIABLES Y TIPOS DE DATOS
#string
string="string variable."
#int
number=1
#string_command
cmd=`pwd`
#array_list ---> mutables, index_ini: 0, cualquier valor sera de tipo string?
array_list=("str1" "str2")

#USAR VARIABLES
#Mostrar
echo "string: $string"
echo "number: $number"
echo "cmd: $cmd"

#Operaciones con strings
concatenation="$string Another string variable"
echo "conatenation: $concatenation"
#Operaciones numericas: expressiones, let
sum=$((number+1))
echo "adicion en declaracion: $sum"
((sum++)) #sum=sum+1
echo "adicion de 1: $sum"
((sum+=2)) #sum=sum+1
echo "adicion de x: $sum"
let "sum=number+1"
let "sum++"
let "sum+=2"
echo "adicion con lets: $sum"

#Operaciones con comandos 
cmd2=cmd

#Operaciones con array-list: cambiar indice, usar x indices, 
array_list[1]=2
echo "valores de lista: ${array_list[*]}"
echo "longitud de chars en lista: ${#array_list[*]}"
echo "valor de index ${array_list[0]}"
echo "longitud de chars index: ${#array_list[1]}"
