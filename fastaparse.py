
mass_table = {'A': 71.037114, 'C': 103.009184, 'D': 115.026943, 'E': 129.042593, 'F': 147.068414,
        'G': 57.021464, 'H': 137.058912, 'I': 113.084064, 'K': 128.094963, 'L': 113.084064,
        'M': 131.040485, 'N': 114.042927, 'P': 97.052764, 'Q': 128.058578, 'R': 156.101111,
        'S': 87.032028, 'T': 101.047678, 'V': 99.068414, 'W': 186.079313, 'Y': 163.063329 }

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
        'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
        'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W'}

def parse(file_path):
    res = []
    t = []
    with open(file_path) as f:
        concat = ''.join(x.rstrip('\n') for x in f)
        line = concat.split(">")
        del line[0]
        for i in range(len(line)):
            N = 7
            res.append(line[i][:N] + "," + line[i][N:])
            t.append(res[i].split(','))
    one = sum(t, [])
    it = iter(one)
    res_dct = dict(zip(it, it))
    return res_dct


def translate(dna_seq):
    cut = dna_seq.find("ATG")
    res = ""

    i = 0
    while i < len(dna_seq[cut:]):
        if dna_seq[i:i + 3] in "TAA" or dna_seq[i:i + 3] in "TAG" or dna_seq[i:i + 3] in "TGA":
            break
        else:
            res += dna_codon[dna_seq[cut:][i:i + 3]]
        i += 3
    remov = "".join(res.partition("STOP")[0:2])
    remov = remov[:-4]
    return remov


def calc_mass(prot_seq):
    res = sum(mass_table[i] for i in prot_seq)
    return res

# def orf(dna_seq):

