mass_table = {
	'G': 57.021464, 'A': 71.037114, 'S': 87.032028, 'P': 97.052764, 
	'V': 99.068414, 'T': 101.047678, 'C': 103.009184, 'I': 113.084064, 
	'L': 113.084064, 'N': 114.042927, 'D': 115.026943, 'Q': 128.058578, 
	'K': 128.094963, 'E': 129.042593, 'M': 131.040485, 'H': 137.058912, 
	'F': 147.068414, 'R': 156.101111, 'Y': 163.063329, 'W': 186.079313}

dna_codon = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def parse(filepath):
	with open(filepath) as f:
		#n=0
		dictionary = dict()
		line = f.readline().rstrip()
		while line != '':
			#line = f.readline()
			#print(line)
			if line.startswith('>'):
				try:
					dictionary[seq_id] = ''.join(seq)
				except:
					True

				seq_id = line.lstrip('>')
				seq = []
			else:
				seq.append(line)
			line = f.readline().rstrip()
			
		try:
			dictionary[seq_id] = ''.join(seq)
			#return
		except:
			True
		#print(dictionary)
		return dictionary


def translate(dna_seq, start_from_start_codon=False, stop_on_stop_codons=False):
	length = len(dna_seq)
	#print(length)
	step = 0
	prot_string = str()
	start = True
	if start_from_aug:
		start = False
	while step<length-2:
		codon = dna_seq[step:step+3]
		if codon == 'ATG':
			start = True
		if start:
			if stop_on_stop_codons and (codon in ['TAA', 'TGA', 'TAG']):
				break

			prot = dna_codon[codon]
			prot_string = ''.join([prot_string, prot])
		step += 3
	return prot_string

def calc_mass(prot_seq):
	sum = 0
	for i in prot_seq:
		sum += mass_table[i]
	return sum

def orf(dna_seq):
	length = len(dna_seq)
	#print(length)
	p_list = list()
	#print('forward')
	for step in [0,1,2]:
		#print(step)
		prot_string = str()
		start = False
		while step<length-2:
			codon = dna_seq[step:step+3]
			if codon == 'ATG':
				#print('ATG')
				start = True
				#prot_string = ''.join([prot_string, 'M'])

			if start:
				if codon in ['TAA', 'TGA', 'TAG']:
					start = False
					break
					#p_list.append(prot_string)
					#prot_string = str()
					#start = False
					#continue


				prot = dna_codon[codon]
				prot_string = ''.join([prot_string, prot])
				#print(prot_string)
			step += 3
		if not start:
			p_list.append(prot_string)

	#print('backward')
	#dna_seq2 = dna_seq[::-1]
	dna_seq2 = str()
	#print(dna_seq)
	#print(dna_seq2)
	dd = {'A':'T','T':'A','C':'G','G':'C'}

	#for i in dd.keys():
	#	print(i)
	#	for j in range(dna_seq2.count(i)):
	#		dna_seq2 = dna_seq2.replace(i, dd[i])
	#print(dna_seq2)
	for i in range(len(dna_seq)-1,-1,-1):
		#dna_seq2.append()
		#print(dna_seq[i])
		dna_seq2 = ''.join([dna_seq2, dd[dna_seq[i]] ])
	#print(dna_seq2)

	for step in [0,1,2]:
		#print(step)
		prot_string = str()
		start = False
		while step<length-2:
			codon = dna_seq2[step:step+3]
			#print(codon)
			#print('before', codon)
			#dd = {'A':'T','T':'A','C':'G','G':'C'}
			#for i in dd.keys():
			#	for j in range(codon.count(i)):
			#		codon = codon.replace(i, dd[i])
			#print('after', codon)

			if codon == 'ATG':
				#print('ATG on position', step)
				start = True
				#prot_string = ''.join([prot_string, 'M']) 
				# WHY DONT I NEED TO ADD M!!! BECAUSE RIGHT AFTER THAT if start BECOMES TO BE TRUE

			if start:
				if codon in ['TAA', 'TGA', 'TAG']:
					start = False
					break
					#p_list.append(prot_string)
					#prot_string = str()
					#start = False
					#continue

				prot = dna_codon[codon]
				prot_string = ''.join([prot_string, prot])
				#print(prot_string)
			step += 3
		
		if not start:
			p_list.append(prot_string)


	'''
	for step in [length,length-1,length-2]:
		#print(step)
		prot_string = str()
		start = False
		while step>2:
			print(step)
			codon = dna_seq[step-1:step-4:-1]
			if step == 3:
				codon = dna_seq[step-1::-1]
			print('before', codon)
			dd = {'A':'T','T':'A','C':'G','G':'C'}
			for i in dd.keys():
				for j in range(codon.count(i)):
					codon = codon.replace(i, dd[i])
			print('after', codon)
			if codon == 'ATG':
				start = True

			if start:
				if codon in ['TAA', 'TGA', 'TAG']:
					break

				prot = dna_codon[codon]
				prot_string = ''.join([prot_string, prot])
			step -= 3
		p_list.append(prot_string)'''

	q = 0
	while q<len(p_list):
		if p_list[q]=='':
			p_list.pop(q)
		else:
			if p_list.count(p_list[q])>1:
				p_list.pop(q)
			#print(p_list[q])
			x = p_list[q].split('M')
			#print(x)
			x = [''.join(['M',i]) for i in x[1:]]
			#print(x)
			p_list.pop(q)
			length = len(x)
			for nn in range(length):
				p_list.insert(q,''.join(x[nn:length]))
				q+=1
	#for i in range(len(p_list)):
	#	if 

	
	return p_list