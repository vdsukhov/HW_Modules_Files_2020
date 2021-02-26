mass_table = {'G': 57.021464,
            'A': 71.037114,
            'S': 87.032028,
            'P': 97.052764,
            'V': 99.068414,
            'T': 101.047678,
            'C': 103.009184,
            'I': 113.084064,
            'L': 113.084064,
            'N': 114.042927,
            'D': 115.026943,
            'Q': 128.058578,
            'K': 128.094963,
            'E': 129.042593,
            'M': 131.040485,
            'H': 137.058912,
            'F': 147.068414,
            'R': 156.101111,
            'Y': 163.063329,
            'W': 186.079313}

rna_codon = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
           "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
           "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
           "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
           "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
           "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
           "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
           "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
           "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
           "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
           "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
           "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
           "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
           "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
           "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
           "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


#file_path = '/home/maria/Documents/Python/fasta_data.txt'

def parse(file_path):
    with open(file_path) as our_file:
        d = dict()
        for line in our_file:
            line = line.strip()
            key = line
            value = our_file.readline().strip('\n')
            d[key] = value
        #print(d)
        return(d)

#parse(file_path)


#rna_seq_path = '/home/maria/Documents/Python/rna_seq.txt'

def translate(rna_seq):
    with open(rna_seq_path) as rna_seq:
        b = 0
        c = b+3
        answ = ''
        for line in rna_seq:
            while line[b:c] != '\n':
                a = line[b:c]
                answ += rna_codon[a]
                b += 3
                c += 3
        #print(answ)
        return(answ)

#translate(rna_seq_path)

#prot_seq = '/home/maria/Documents/Python/prot_seq.txt'
        
def calc_mass(prot_seq):
     prot_mass = 0
     with open(prot_seq) as prot:
        for el in prot:
            el = el.strip()
            for i in el:
                prot_mass += mass_table[i]
            #print(prot_mass)
        return(prot_mass)

#calc_mass(prot_seq)
    
#rna_seq_path = '/home/maria/Documents/Python/rna_seq.txt'

def orf(rna_seq):
    with open(rna_seq_path) as rna_seq:
        start = 'AUG'
        b = 0
        c = 3
        stop = ['UAG', 'UAA','UGA']
        rnas = []
        prot_str = ''
        list_of_prot = []
        for line in rna_seq:
            line = line.strip() 
            while c < len(line): 
                
                if line[b:c] == start:
                    our_line = line[b:]
                    st = []
                    for el in stop:
                        if el in our_line:
                            st.append(our_line.find(el))
                    our_line = our_line[:min(st)]
          
                    f = 0
                    d = f+3
                    while f < len(our_line):
                        codon = our_line[f:d]
                        prot_str += rna_codon[codon]
                        f += 3
                        d += 3
                    list_of_prot.append(prot_str)
                b += 1
                c += 1
        #print(list_of_prot)
    return(list_of_prot)
#orf(rna_seq_path)
