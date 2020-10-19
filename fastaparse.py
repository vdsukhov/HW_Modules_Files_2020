mass_table = {'A' : 71.037114, 'C' : 103.009184, 'D' : 115.026943, 
              'F' : 147.068414, 'E' : 129.042593, 'G' : 57.021464, 
              'H' : 137.058912, 'I' : 113.084064, 'K' : 128.094963, 
              'L' : 113.084064, 'M' : 131.040485, 'N' : 114.042927, 
              'P' : 97.052764, 'Q' : 128.058578, 'R' : 156.101111, 
              'S' : 87.032028, 'T' : 101.047678, 'V' : 99.068414, 
              'W' : 186.079313, 'Y' : 163.063329}

dna_codon = {'A' : ('GCT', 'GCC', 'GCA', 'GCG'), 'C' : ('TGT', 'TGC'), 
             'D' : ('GAT', 'GAC'), 'F' : ('TTT', 'TTC'), 'E' : ('GAA', 'GAG'), 
             'G' : ('GGT', 'GGC', 'GGA', 'GGG'), 'H' : ('CAT', 'CAC'), 
             'I' : ('ATT', 'ATC', 'ATA'), 'K' : ('AAA', 'AAG'), 
             'L' : ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'), 'M' : ('ATG'), 
             'N' : ('AAT', 'AAC'), 'P' : ('CCT', 'CCC', 'CCA', 'CCG'), 
             'Q' : ('CAA', 'CAG'), 'R' : ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
             'S' : ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'), 
             'T' : ('ACT', 'ACC', 'ACA', 'ACG'), 'V' : ('GTT', 'GTC', 'GTA', 'GTG'), 
             'W' : ('TGG'), 'Y' : ('TAT', 'TAC'), 'STOP' : ('TAA', 'TAG', 'TGA')}

def parse(path):    
     with open(path, "r") as file:
        seq_id = []
        seq = []
        for line in file:
            if line.startswith('>'):
                seq_id.append(line[1:-1])
            else:
                seq.append(line[:-1])
        res_dict = dict(zip(seq_id, seq))
        return res_dict
  
def translate(dna_seq):
    prot = ''
    for j in range(len(dna_seq) - 2):
        if dna_seq[j:j+3] == dna_codon.get('M'):
            prot += 'M'
            for i in range(j + 3, len(dna_seq) - 2, 3):
                if dna_seq[i:i+3] in dna_codon.get('STOP'):
                    return prot
                for k in dna_codon.values():
                    if dna_seq[i:i+3] in k:
                        prot += list(dna_codon.keys())[list(dna_codon.values()).index(k)]
            return prot

def calc_mass(prot_seq):
    mass = 0
    for protein in prot_seq:
        mass += mass_table.get(protein)
    return mass

def orf(dna_seq):
    #For forward strand
    start = [st for st in range(len(dna_seq)) if dna_seq.startswith('ATG', st)]
    start_stop = {}
    for i in start:
        for j in range(i, len(dna_seq) - 2, 3):
            if dna_seq[j:j+3] in dna_codon.get('STOP'):
                start_stop.setdefault(i, j)      
    #For reverse strand
    r = dna_seq.replace('A', 't')
    r = r.replace('C', 'g')
    r = r.replace('G', 'c')
    r = r.replace('T', 'a')
    rdna_seq = r.upper()[::-1]
    rstart = [st for st in range(len(rdna_seq)) if rdna_seq.startswith('ATG', st)]
    rstart_stop = {}
    for i in rstart:
        for j in range(i, len(rdna_seq) - 2, 3):
            if rdna_seq[j:j+3] in dna_codon.get('STOP'):
                rstart_stop.setdefault(i, j)      
    #Proteins
    res =[]
    for i in list(start_stop.items()):
        res.append(translate(dna_seq[i[0]:i[1]]))
    rres = []
    for i in list(rstart_stop.items()):
        rres.append(translate(rdna_seq[i[0]:i[1]]))
    result = []
    for protein in res + rres:
        if protein not in result:
            result.append(protein)
    return result
