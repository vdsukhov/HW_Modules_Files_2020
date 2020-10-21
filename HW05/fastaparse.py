mass_table = {
    "G":57.021464,
    "A":71.037114,
    "S":87.032028,
    "P":97.052764,
    "V":99.068414,
    "T":101.047678,
    "C":103.009184,
    "I":113.084064,
    "L":113.084064,
    "N":114.042927,
    "D":115.026943,
    "Q":128.058578,
    "K":128.094963,
    "E":129.042593,
    "M":131.040485,
    "H":137.058912,
    "F":147.068414,
    "R":156.101111,
    "Y":163.063329,
    "W":186.079313
}

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
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
}

# start = ATG
# stop = _

def parse(file_path):
    res = {}
    with open(file_path, 'r') as f:
        key = ""
        val = ""
        for line in f:
            if line.strip().startswith('>'):
                if key:
                    res[key] = val
                key = line.strip()[1:]
                val = ""
            else:
                val += line.strip()
        if key:
            res[key] = val
    return res

print(parse("/home/elizaveta/Desktop/ITMO/Python/fasta_data.txt"))

def translate(dna_seq, skip_start = True):
    start = "ATG"
    tmp = dna_seq.find(start)
    if tmp < 0:
        return ""
    if skip_start:
        tmp += 3
    dna_seq = dna_seq[tmp:]
    res = ""
    while len(dna_seq) >= 3:
        nxt = dna_seq[0:3]
        if nxt not in dna_codon:
            return ""
        if dna_codon[nxt] == '_':
            return res
        res = res + dna_codon[nxt]
        dna_seq = dna_seq[3:]
    return ""

print(translate("AAATGCTGCCGTGA"))

def calc_mass(prot_seq):
    res = 0
    for c in prot_seq:
        res += mass_table[c]
    return res

print(calc_mass("CGMALPK"))

def orf_impl(dna_seq):
    res = []
    start = "ATG"
    tmp = dna_seq.find(start)
    while tmp > 0:
        nxt = translate(dna_seq[tmp:], False)
        if nxt:
            res.append(nxt)
        dna_seq = dna_seq[tmp + 3:]
        tmp = dna_seq.find(start)
    return res    

def orf(dna_seq):
    dna_seq_comp = ""
    for c in dna_seq:
        if c == 'A':
            dna_seq_comp += 'T'
        elif c == 'T':
            dna_seq_comp += 'A'
        elif c == 'C':
            dna_seq_comp += 'G'
        elif c == 'G':
            dna_seq_comp += 'C'
    dna_seq_comp = dna_seq_comp[::-1] 
    res = []
    res += orf_impl(dna_seq)
    res += orf_impl(dna_seq_comp)
    return list(set(res))

print(orf("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"))
