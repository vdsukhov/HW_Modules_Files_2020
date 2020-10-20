mass_table = {
	"G": 57.021464,
	"A": 71.037114,
	"S": 87.032028,
	"P": 97.052764,
	"V": 99.068414,
	"T": 101.047678,
	"C": 103.009184,
	"I": 113.084064,
	"L": 113.084064,
	"N": 114.042927,
	"D": 115.026943,
	"Q": 128.058578,
	"K": 128.094963,
	"E": 129.042593,
	"M": 131.040485,
	"H": 137.058912,
	"F": 147.068414,
	"R": 156.101111,
	"Y": 163.063329,
	"W": 186.079313
}

dna_codon = {
	"A":     ["GCT", "GCC", "GCA", "GCG"],
	"R":     ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
	"N":     ["AAT", "AAC"],
	"D":     ["GAT", "GAC"],
	"B":     ["AAT", "AAC", "GAT", "GAC"],
	"C":     ["TGT", "TGC"],
	"Q":     ["CAA", "CAG"],
	"E":     ["GAA", "GAG"],
	"Z":     ["CAA", "CAG", "GAA", "GAG"],
	"G":     ["GGT", "GGC", "GGA", "GGG"],
	"H":     ["CAT", "CAC"],
	"I":     ["ATT", "ATC", "ATA"],
	"L":     ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
	"K":     ["AAA", "AAG"],
	"M":     ["ATG"],
	"F":     ["TTT", "TTC"],
	"P":     ["CCT", "CCC", "CCA", "CCG"],
	"S":     ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
	"T":     ["ACT", "ACC", "ACA", "ACG"],
	"W":     ["TGG"],
	"Y":     ["TAT", "TAC"],
	"V":     ["GTT", "GTC", "GTA", "GTG"],
	"STOP":  ["TAA", "TGA", "TAG"],
	"START": ["ATG"]
}

def parse(file_path):
	res_dict = {}
	current_key = ""
	try:
		with open(file_path, 'r') as input_file:		
			for line in input_file:
				line = line.strip()
				if line.find(">") == 0:
					current_key = line[1:]
					res_dict[current_key] = ""
					continue
				res_dict[current_key] += line

	except Exception:
			print("Error, such file doesn't exist")

	return res_dict

def translate(dna_seq):
	protein = ""
	for i in range (0,len(dna_seq),3):
		triplet = dna_seq[i:i+3]
		if triplet in dna_codon["STOP"]:
			break
		elif triplet in dna_codon["A"]:
			protein += "A"
		elif triplet in dna_codon["R"]:
			protein += "R"
		elif triplet in dna_codon["N"]:
			protein += "N"
		elif triplet in dna_codon["D"]:
			protein += "D"
		elif triplet in dna_codon["B"]:
			protein += "B"
		elif triplet in dna_codon["C"]:
			protein += "C"
		elif triplet in dna_codon["Q"]:
			protein += "Q"
		elif triplet in dna_codon["E"]:
			protein += "E"
		elif triplet in dna_codon["Z"]:
			protein += "Z"
		elif triplet in dna_codon["G"]:
			protein += "G"
		elif triplet in dna_codon["H"]:
			protein += "H"
		elif triplet in dna_codon["I"]:
			protein += "I"
		elif triplet in dna_codon["L"]:
			protein += "L"
		elif triplet in dna_codon["K"]:
			protein += "K"
		elif triplet in dna_codon["M"]:
			protein += "M"
		elif triplet in dna_codon["F"]:
			protein += "F"
		elif triplet in dna_codon["P"]:
			protein += "P"
		elif triplet in dna_codon["S"]:
			protein += "S"
		elif triplet in dna_codon["T"]:
			protein += "T"
		elif triplet in dna_codon["W"]:
			protein += "W"
		elif triplet in dna_codon["Y"]:
			protein += "Y"
		elif triplet in dna_codon["V"]:
			protein += "V"
	return protein

def calc_mass(prot_seq):
	masses = {}
	masses["G"] = 57.021464
	masses["A"] = 71.037114
	masses["S"] = 87.032028
	masses["P"] = 97.052764
	masses["V"] = 99.068414
	masses["T"] = 101.047678
	masses["C"] = 103.009184
	masses["I"] = 113.084064
	masses["L"] = 113.084064
	masses["N"] = 114.042927
	masses["D"] = 115.026943
	masses["Q"] = 128.058578
	masses["K"] = 128.094963
	masses["E"] = 129.042593
	masses["M"] = 131.040485
	masses["H"] = 137.058912
	masses["F"] = 147.068414
	masses["R"] = 156.101111
	masses["Y"] = 163.063329
	masses["W"] = 186.079313
	total_mass = 0
	for ch in prot_seq:
		total_mass += masses[ch]
	return total_mass

def second_strand(dna_seq):
	second_strand_dna_seq = ""
	length = len(dna_seq)
	compl_rule = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
	for i in range(length - 1, -1, -1):
		second_strand_dna_seq += compl_rule[dna_seq[i]]

	return second_strand_dna_seq

def split_to_triplets(dna_seq):
	triplets = []
	for i in range (0,len(dna_seq),3):
		triplets.append(dna_seq[i:i+3])
	if len(triplets[-1]) != 3:
		triplets.pop()
	return triplets

def orf(dna_seq):
	all_triplets = []
	second_strand_dna_seq = second_strand(dna_seq)
	all_triplets.append(split_to_triplets(dna_seq[0:]))
	all_triplets.append(split_to_triplets(dna_seq[1:]))
	all_triplets.append(split_to_triplets(dna_seq[2:]))
	all_triplets.append(split_to_triplets(second_strand_dna_seq[0:]))
	all_triplets.append(split_to_triplets(second_strand_dna_seq[1:]))
	all_triplets.append(split_to_triplets(second_strand_dna_seq[2:]))

	proteins_list = []
	for triplets in all_triplets:
		where_starts = []
		where_stops = []
		for i in range(len(triplets)):
			triplet = triplets[i]
			if triplet in dna_codon['START']:
				where_starts.append(i)
				continue
			if len(where_starts) > 0:
				if triplet in dna_codon['STOP']:
					where_stops.append(i)

		if len(where_starts) > 0 and len(where_stops) > 0:
			starts_considered = 0
			for where_stop in where_stops:
				for where_start in where_starts[starts_considered:]:
					orf = ""
					if where_start > where_stop:
						break
					for i in range(where_start, where_stop):
						triplet = triplets[i]
						orf += triplet
					protein = translate(orf)
					if protein not in proteins_list:
						proteins_list.append(protein)
					starts_considered += 1

	return proteins_list 
