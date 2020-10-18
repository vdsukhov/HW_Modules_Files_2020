import re

# Monoisotopic mass table as a dictionnary
mass_table = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
              "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
              "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
              "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
              "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}

# RNA codon table
rna_codon = {
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
        'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
        'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W', }

# That parses a fasta file and returns a dictionary of pairs seq_id as string and the sequence itself seq as stg or list
def parse(file_path):
    dictionary = {}
    lines = []
    with open(file_path, "r") as inp_f:
        for line in inp_f:
            lines.append(line)
    k = 0
    val = []
    for i in range(len(lines)):
        if lines[i][0] == ">":
            dictionary[lines[i][1:len(lines[i]) - 1]] = ""
            k = 0
        else:
            k += 1
            if k == 1:
                val.append(lines[i].replace('\n', ''))
            else:
                val[-1] += lines[i][:len(lines[i])].replace('\n', '')
    i = 0
    for key in dictionary:
        dictionary[key] = val[i]
        i += 1
    return(dictionary)

def translate(rna_seq):
    rna_codon = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'STOP', 'TAG': 'STOP',
        'TGC': 'C', 'TGT': 'C', 'TGA': 'STOP', 'TGG': 'W', }
    start_codon = rna_seq.find('ATG')
    protein_seq = ''
    if start_codon != -1:
        rna_seq_start = rna_seq[int(start_codon):]
        for i in range(0, len(rna_seq_start), 3):
            if rna_codon[rna_seq_start[i:i + 3]] == "STOP":
                return(protein_seq)
            else:
                protein_seq += rna_codon[rna_seq_start[i:i + 3]]
    if protein_seq != "":
        return(protein_seq)

def calc_mass(prot_seq):
    mass_table = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
                "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
                "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
                "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}
    sum = 0
    for ch in prot_seq:
        sum += float(mass_table[ch])
    return(sum)

def translate_for_orf(rna_seq):
    rna_codon = {
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
        'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
        'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W', }
    protein_seqs = []
    start_codons = [m.start() for m in re.finditer('ATG',rna_seq)]
    for i in range(len(start_codons)):
        protein_seq = ""
        if start_codons[i] != -1:
            rna_seq_start = rna_seq[int(start_codons[i]):]
            for j in range(0, len(rna_seq_start)-3, 3):
                if rna_codon[rna_seq_start[j:j+3]] == "STOP":
                    protein_seqs.append(protein_seq)
                    break
                else:
                    protein_seq += rna_codon[rna_seq_start[j:j+3]]
    return(protein_seqs)

def orf(rna_seq):
    compl = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    compl_rna_seq = ''.join([compl[i] for i in reversed(rna_seq)])
    T = list(set(translate_for_orf(rna_seq) + translate_for_orf(compl_rna_seq)))
    result = "\n".join(T)
    return result
