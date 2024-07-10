import sys
#sys.abiflags ||
#sys.addaudithook ||
#sys.audit() ||
#sys.arg ||
'''
print(sys.argv)
'''
#sys.version || da la version del progrma
'''
print(sys.version)
'''

#sys.stdin, sys.stdout, sys.stderr
'''
stdin (STanDard INput)
stdout (Standard Output)
stderr (Starndard Error)
print(sys.stdin)
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
ex: bucle infinito, dado un valor introducido en stdin, ejecuta las instrucciones
    * Util para separar elementos de una variable, cua funcion permite crear valores, en otras palabras, podemos crear una lista de valores en un bucle
<<<<<
for value in sys.stdin:
 print(f, value)
>>>>>
ex: Dado un valor en stdin, ejecuta una condicion en un bucle infinito (en este caso el bucle for tiene como rango no especificado, de ahi que sea infinito)
      Si la letra 'q' es igual a el valor insertado en value acortada con un metodo 'rstrip' para eliminar espacios de la deracha de la cadena
        Entonces rompe el bucle for
      Despues printa un string con el valor de value acompañada utilizando el metodo f'string'
<<<<<<
>>>>>
'''
for value in sys.stdin:
 print('value:'value})

"""FILTRADO DE IPs
# genera una IP aleatoria
def genrardor_ip():
  ip = ''
  for i in range(3):
    ip = ip + str( randint(0, 255) ) + '.'
  return  ip

ip_list = []
for i in range(10):
  ip_list.append(generador_ip)
print(ip_list)

def escribir_ip():
  archivo = sys.argv[1]
  lista = generador_ip()
  escribir_ip
"""
