import pdb
mass_table = {
	'A':71.03711,
	'R':156.10111,
	'N':114.04293,
	'D':115.02694,
	'C':103.00919,
	'E':129.04259,
	'Q':128.05858,
	'G':57.02146,
	'H':137.05891,
	'I':113.08406,
	'L':113.08406,
	'K':128.09496,
	'M':131.04049,
	'F':147.06841,
	'P':97.05276,
	'S':87.03203,
	'T':101.04768,
	'W':186.07931,
	'Y':163.06333,
	'V':99.06841
}

dna_codon = { 
	"M":[["ATG"]],
	"F":[["TTT"],["TTC"]],
	"L":[["TTA"],["TTG"],["CTT"],["CTC"],["CTA"],["CTG"]],
	"I":[["ATT"],["ATC"],["ATA"]],
	"V":[["GTT"],["GTC"],["GTA"],["GTG"]],
	"S":[["TCT"],["TCC"],["TCA"],["TCG"],["AGT"],["AGC"]],
	"P":[["CCT"],["CCC"],["CCA"],["CCG"]],
	"T":[["ACT"],["ACC"],["ACA"],["ACG"]],
	"A":[["GCT"],["GCC"],["GCA"],["GCG"]],
	"Y":[["TAT"],["TAC"]],
	"H":[["CAT"],["CAC"]],
	"Q":[["CAA"],["CAG"]],
	"N":[["AAT"],["AAC"]],
	"K":[["AAA"],["AAG"]],
	"D":[["GAT"],["GAC"]],
	"E":[["GAA"],["GAG"]],
	"C":[["TGT"],["TGC"]],
	"W":[["TGG"]],
	"R":[["CGT"],["CGC"],["CGA"],["CGG"],["AGA"],["AGG"]],
	"G":[["GGT"],["GGC"],["GGA"],["GGG"]]
}

def parse(file_path):
	str_fasta = "" ; key = ""; value = ""; nucleotides = ["A","T","C","G"]; parsed_dict = {}; recorrer =  False
	with open(file_path) as fasta_file:
		for line in fasta_file:
			str_fasta += line 
	str_fasta = str_fasta.splitlines() #aqui str_fasta ya es lists
	for elem in range(len(str_fasta)):
		if key != "" and value != "" and recorrer == False:
			parsed_dict[key] = value
			key = ""; value = ""
			if elem == len(str_fasta) - 1: break
		if str_fasta[elem].startswith(">") == True and key == "":
			key = str_fasta[elem]; continue
		for bases in range(len(nucleotides)):
			if str_fasta[elem].startswith(nucleotides[bases]) and elem < len(str_fasta)-1 and str_fasta[elem+1].startswith(">") == True:
				value = str_fasta[elem] ; break
			elif bases == len(nucleotides)-1 and value == "" and elem < len(str_fasta)-1 and recorrer == False: #quiere decir que el sig.elemento tiene nucleotidos
				value = str_fasta[elem]
				recorrer = True #para decir que tiene que guardar hasta el siguiente turno
				break
			elif recorrer == True:
				value = value + str_fasta[elem]
				if elem < len(str_fasta)-1 and str_fasta[elem+1].startswith(">"):
					recorrer = False
				if elem == len(str_fasta)-1 and str_fasta[elem].startswith(nucleotides[bases]) == True:
					value = value + str_fasta[elem]
					parsed_dict[key] = value
				break
			if elem == len(str_fasta)-1 and str_fasta[elem].startswith(nucleotides[bases]) == True:
				value = value + str_fasta[elem]
				parsed_dict[key] = value
	return parsed_dict

def translate(dna_seq):
	termine = False; inicio = 0; encontre = False; seq_prot = ''
	for i in range(len(dna_seq)): #buscar metionina
		if dna_seq[i:].startswith("ATG") == True:
			inicio = i
			break
	for recorrer_str in range(inicio,len(dna_seq),3):
		if encontre == True:
			encontre = False
		if termine == True:
			break
		for aa, codones in dna_codon.items():
			if termine == True or encontre == True: break
			for elem_lista_ext in range(len(dna_codon[aa])): #para entrar a la lista
				if termine == True or encontre == True: break
				for elem_interno_lista in range(len(dna_codon[aa][elem_lista_ext])):
					if dna_seq[recorrer_str:recorrer_str+3] == "TAA" or dna_seq[recorrer_str:recorrer_str+3] == "TAG" or dna_seq[recorrer_str:recorrer_str+3] == "UGA":
						termine = True
						break
					if dna_seq[recorrer_str:recorrer_str+3] == dna_codon[aa][elem_lista_ext][elem_interno_lista]:
						seq_prot += aa
						encontre = True
						break
	if seq_prot == '':
		print("No CDS were found")
	return seq_prot

def calc_mass(prot_seq):
	lista = []; mass = 0; conteo = 0
	for aa, mass in mass_table.items():
		conteo = prot_seq.count(aa)
		lista.append(mass*conteo)
	#print("Esta es la lista de masas",lista)
	mass = float(sum(lista))
	return mass

def orf(dna_seq):
	dna_complementario = []; almacen = ""; ultima_base = 0; list_complementary_chain = ""
	list_original_chain = ""; final_list = ""; cadena_dna_reverse = ""; para_eliminar = []; salvo_uno = False; siguiente = 0

	for i in range(len(dna_seq)-1,-1,-1): #invertir dna_seq para cadena comple
		cadena_dna_reverse += dna_seq[i]
	#print("cadena_dna_reverse",cadena_dna_reverse); print('\n')

	#print("DNA normal",dna_seq); print('\n')

	list_original_chain = whole_analisis(dna_seq)
	#print("list_original_chain",list_original_chain); print('\n')

	list_complementary_chain = whole_analisis(cadena_dna_reverse) #tenias dna_complementario
	#print("list_complementary_chain",list_complementary_chain); print('\n')

	final_list = list_original_chain + list_complementary_chain
	
	lista_nueva_final = []
	for i in final_list:
		if i not in lista_nueva_final:
			lista_nueva_final.append(i)
	return lista_nueva_final

def whole_analisis(dna_seq):
	almacen = ""; ultima_base = 0; inicio = 0; dna_marco_x = ""; 
	seq_prot = ""; final = 0; lista_final_prot = ""; fijar = 0; stop = 0; start = 0; lista_final_prot_final = []
	for marco_x in range(3):
		dna_marco_x,almacen,ultima_base = leer_marco(dna_seq,marco_x) #entrega una list

		codon_met = dna_marco_x.count("ATG") #analisis de codones de dna_marco_x
		positions_met = [index for index in range(len(dna_marco_x)) if dna_marco_x[index] == "ATG"]
		#print("positions_met",positions_met)
		positions_stop = [index for index in range(len(dna_marco_x)) if dna_marco_x[index] == "TAA" or dna_marco_x[index] == "TAG" or dna_marco_x[index] == "TGA"]
		#print("positions_stop",positions_stop)

		inicio,final,fijar,start,stop,seq_prot,lista_final_prot = analisis_aa(codon_met,positions_met,positions_stop,dna_marco_x)
		#print("Marco de lectura",marco_x+1,":",dna_marco_x)
		#print("\n")

		#if inicio == 0 and final == 0 and fijar == 0:
		#	print("There was no cds in ORF",marco_x+1,)
		#	print("\n")
		if start == len(positions_met) - 1 and stop == len(positions_stop) - 1:
			dna_marco_x.clear()
			positions_met.clear()
			positions_stop.clear()
		#else:
		#	print("Secuencia de aa para marco de lectura",marco_x+1,":",seq_prot)
		#	print("\n")
		almacen = ""
		ultima_base = 0
		fijar = 0
		#print("lista_final_prot",lista_final_prot)
		lista_final_prot_final.extend(lista_final_prot)

	return lista_final_prot_final

def leer_marco(dna_seq,marco_x):
	ultima_base = 0; almacen = ""; dna_marco_x = []
	for base in range(marco_x,len(dna_seq)): #cadena 5'-3'
		if len(almacen) == 3:
			dna_marco_x.append(almacen)
			almacen = ""
			almacen += dna_seq[base]
		elif len(almacen) < 3:
			almacen += dna_seq[base]
		ultima_base = ultima_base + 1
		if ultima_base == len(dna_seq):
			dna_marco_x.append(almacen)
	return dna_marco_x,almacen,ultima_base

def analisis_aa(codon_met,positions_met,positions_stop,dna_marco_x):
	fijar = 0; inicio = 0; final = 0; encontre = False; seq_prot = ""; lista_final_prot = []; start = 0; stop = 0
	if codon_met != 0:
		#pdb.set_trace()
		for start in range(len(positions_met)):
			for stop in range(len(positions_stop)):
				if fijar != 0:
					fijar = 0
					break
				if positions_met[start] < positions_stop[stop]:
					inicio = positions_met[start]
					final = positions_stop[stop]
					fijar = positions_stop[stop]
					
				if inicio != 0 and final != 0:
					for codon_in_list in range(inicio,final):
						if encontre == True: 
							encontre = False

						for aa, codones in dna_codon.items():
							if encontre == True: 
								break

							for elem_list_codones in range(len(codones)):
								if encontre == True: 
									break

								for elem_int_list_codones in range(len(codones[elem_list_codones])):
								#pdb.set_trace()
									if dna_marco_x[codon_in_list] == dna_codon[aa][elem_list_codones][elem_int_list_codones]:
										seq_prot += aa
										encontre = True
										if codon_in_list == final - 1:
											lista_final_prot.append(seq_prot)
											seq_prot = ""
											inicio = 0; final = 0
										break
	return inicio,final,fijar,start,stop,seq_prot,lista_final_prot