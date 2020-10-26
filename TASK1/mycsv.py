import pdb
import os.path #para usar funcion os.path.exists()
def read_csv(path_to_csv_file, delimiter = ","):
	lista = []
	cuantas_lineas = 0
	conteo_categorias = 0
	if os.path.exists(path_to_csv_file) ==  False: #dara True si existe path_to_csv_file
		print("Error, such file doesn't exist")
		return lista
	with open(path_to_csv_file) as csv_open:
		for linea in csv_open:
			for i in range(len(linea)):
				if i >= len(linea):
					break
				else:
					if linea[i] == "'" or linea[i] == '"':
						linea = linea.replace("'","")
						linea = linea.replace('"','') #es str
			linea = linea.split()
			#linea = linea.splitlines() #usado con str, retorna list sin los espacios \n al final de cada elemento en la lista
			cuantas_lineas = cuantas_lineas + 1 #es un contador para saber cual linea estamos analizando
			if cuantas_lineas == 1: #si es la primera linea que analizas entonces haces un conteo de cuantos delimitadores hay en la linea, asi sabes cuantas categorias debe de haber 
				for conteo in range(len(linea[0])):
					if linea[0][conteo] == delimiter: 
						conteo_categorias = conteo_categorias + 1 #contador de categorias en linea 1
			linea = "".join(linea) #convierto list a str
			linea = linea.split(delimiter,conteo_categorias) #usado con str, retorna lista
			lista.append(linea)
	return lista

def write_csv(path_to_csv_file,data,delimiter = ','):
	with open(path_to_csv_file,"w") as escribir:
		#print("Este es el tipo de dato de data",type(data)) #Lista
		#print("Datos que hay dentro de data",type(data[0])) #Lista[lista]
		for elem in range(len(data)):
			for elemento in range(len(data[elem])):
				almacen_data = ''.join(data[elem][elemento])
				if almacen_data.isalpha() ==  True:
					nuevo_almacen = almacen_data
				elif almacen_data.isdigit() == False and almacen_data.isalpha() ==  False:
					nuevo_almacen = '"' + almacen_data + '"'
				elif almacen_data.isdigit() == True: 
					nuevo_almacen = almacen_data
				if elemento == len(data[elem]) - 1:
					nuevo_almacen = nuevo_almacen + '\n'
					escribir.write(nuevo_almacen)
				else:
					nuevo_almacen = nuevo_almacen + delimiter
					escribir.write(nuevo_almacen)
				almacen_data = "" ; nuevo_almacen = ""
	return 