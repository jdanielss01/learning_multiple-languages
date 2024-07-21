import sys
import subprocess

def ping_ip_main():
	ip = sys.argv[1]
	crida_basica_cmd_ip(ip)
def ping_ips_main():
	ip_inicial = sys.argv[1]
	ip_final = sys.argv[2]
	print('OPCIONES:\n1-Dos ips\n2-Rango en un segmento\n3-Rango en varios segmentos')
	opcion = int(input('opcion: '))
	if opcion == 1: crida_basica_cmd_ips(ip_inicial, ip_final)
	if opcion == 2: crida_basica_cmd_rang(ip_inicial, ip_final) #ips = crida_basica_cmd_rang(ip_inicial, ip_final)
	if opcion == 3: crida_basica_cmd_rangs(ip_inicial, ip_final)
	"""for ip in ips:
		get_data_icmp(ip)"""


"""
===============================================================
SE HACE 1 PETICION ICMP o VARIAS PERICIONES ICMPS EN LA IP RECOGIDA. SE DEVUELVE RESULTADOS ESCOGIDOS EN LA FUNCION, O UN MENSAJE DE ERROR SI SE ESTABLECE CONEXION
===============================================================
"""
#=Se hace 1 peticion icmp y se recoge informacion especifica si funciona. Si no funciona se devuelve un mensaje de errror
def get_data_icmp(ip):
	try:
		stdout_byte = subprocess.check_output(['ping', '-c1', ip])
		stdout_str = stdout_byte.decode('UTF-8')
		lines = stdout_str.split('\n')
		line_ip = lines[1]
		extracted_data = ip + ' - ' + ' '.join(line_ip.split(' ')[-2:]).replace('time=', '')
		return extracted_data
	except:
		return (f'{ip} - ERROR')
#===============================================================
#=Se hace 4 peticiones icmp
def get_data_icmps(ip):
	print('c4 ping')
"""===============================================================
SE HACE 1 PETICION ICMP, A LA O LAS IPs QUE SE UNDIQUEN SEGUN LA FUNCION
==============================================================="""
#FER PING A 1 IP #=Se hace ping a una ip, si existe
def crida_basica_cmd_ip(ip):
	get_data_icmp(ip)

#===============================================================
#FER PING A UNA O VARIES IPS #=Se hace ping a una o varias ip, si existe
def crida_basica_cmd_ips(*ips):
	for ip in ips:
		get_data_icmp(ip)

#===============================================================
#FER PING A UN RANG IPS EN UN SEGMENT #=Se hace ping a un rango de 1 segmento(el 4to), si las ips existen
def crida_basica_cmd_rang(ip_ini, ip_fin):
	ip_ini_list = ip_ini.split('.')
	ip_fin_list = ip_fin.split('.')
	ini_segment = int(ip_ini_list[3])
	fin_segment = int(ip_fin_list[3])
	#ips = []
	for i in range(fin_segment-ini_segment+1):
		segment = str(ini_segment+i)
		ip_ini_list[3] = segment
		ip = '.'.join(ip_ini_list)
		get_data_icmp(ip)
		#ips.append(ip); #return ips

#===============================================================
#FER PING A UN RANG IPS EN VARIS SEGMENTS #=Se hace ping a un rango por cada segmento, si las ips existen
def crida_basica_cmd_rangs(ip_ini, ip_fin):
	"""1 - Se recogen los argumentos i valores necesarios del del programa"""
	# <editor-fold desc="code">
	ip_ini_list = ip_ini.split('.') #argv[1] Se recoge la ipv4 incial en 4 segmentos
	ip_fin_list = ip_fin.split('.') #argv[2] Se recoge la ipv4 final en 4 segmentos
	ip_segments_diffs = [] #Se crea una lista para las diferencias en cada segmento
	diff_broadcast = False #Se define a una diferencia broadcast(256) como inexistente
	valors_posibles = 256 #Se define la cantidad de valores posibles en cada segmento
	last_segment = 0 #Se define el valor del anterior segmento, para usar en un bucle
	# </editor-fold>

	"""2 - Se buscan las diferencias en las ip de cada segmento"""
	# <editor-fold desc="code">
	for ip_ini_segment, ip_fin_segment in zip(ip_ini_list, ip_fin_list): #Bucle para comparar entre segmentos de cada ip (4 reps en total)
		if diff_broadcast is False: #Para cuando diff de broadcast no existe (ocurre si el anterior segmento tenia una diff = 0, )
			segment_diff = int(ip_fin_segment)-int(ip_ini_segment) #Se calcula la difirencia entre el final i el inicial
			ip_segments_diffs.append(segment_diff) #Se añade a la lista de diferencias 
			last_segment = segment_diff #Se crea el numero de valores para el siguiente segmento
			if segment_diff > 0: #Para cuando diferencia sea mayor de 0
				diff_broadcast = True #La diferencia de broadcast existe
		else: #Para cuando diff broacast existe
			segment_diff = last_segment*valors_posibles - int(ip_ini_segment) + int(ip_fin_segment) #Se calcula la difenrencia buscando valores posibles por cada valor añadido en el anterior segmento
			ip_segments_diffs.append(segment_diff) #Se añade a la lista de diferencias
	# </editor-fold>
	
	"""3-1 - Se crean variables para el incremento de ips"""
	# <editor-fold desc="code">
	segments_length = ip_segments_diffs[3] #El valor en el cuarto segmento de diferencia, representa la distancia de decimales a contar (poniedo como limite 255)
	ip_ini_list_int = [int(ip_ini_segment) for ip_ini_segment in ip_ini_list] #Se tranformala lista inicial de cadenas a enteros
	s1,s2,s3 = ip_ini_list_int[0], ip_ini_list_int[1], ip_ini_list_int[2] #Se definen los segmentos iniciales para ir sumandoles valores
	reps1, reps2, reps3 = 1, 1, 1 #Se definen las repeticiones para indicar cuantas veces se ha llegado a 255
	# </editor-fold>
	"""3-2 - Se incrementan las ip desde el segmento de la derecha, segun se llegue a 255. Luego se hace ping por cada ip"""
	for i in range(segments_length+1):
		s4 = (ip_ini_list_int[3] + i) % 256
		if s4 == 0:
			s3 = (ip_ini_list_int[2] + reps1) % 256
			reps1 += 1
			if s3 == 0:
				s2 = (ip_ini_list_int[1] + reps2) % 256
				reps2 += 1
				if s2 == 0:
					s1 = ip_ini_list_int[0] + reps3

		"""3-2-1 - Se busca la interconexion ping por cada ip"""
		ip = f'{s1}.{s2}.{s3}.{s4}'
		get_data_icmp(ip)











#import pythonping
#pythonping.ping(ip, verbose=True)
#Hacer ping a un rango , si la ip existe, Se deberia crear un diccionario
#Nativamente, ping no permite asignar un rango de paquetes, se puede usar nmap


