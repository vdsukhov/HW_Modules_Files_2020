def mass_table(amino_acid: str):
    mass = {'G': 57.021464, 'A': 71.037114, 'S': 87.032028, 'P': 97.052764,
            'V': 99.068414, 'T': 101.047678, 'C': 103.009184, 'I': 113.084064,
            'L': 113.084064, 'N': 114.042927, 'D': 115.026943, 'Q': 128.058578,
            'K': 128.094963, 'E': 129.042593, 'M': 131.040485, 'H': 137.058912,
            'F': 147.068414, 'R': 156.101111, 'Y': 163.063329, 'W': 186.079313}
    return mass[amino_acid]


def dna_codon(dna_cod: str):
    codon_dict = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L',
                  'CTA': 'L', 'CTG': 'L', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
                  'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'TCT': 'S', 'TCC': 'S',
                  'TCA': 'S', 'TCG': 'S', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                  'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A',
                  'GCA': 'A', 'GCG': 'A', 'TAT': 'Y', 'TAC': 'Y', 'TAA': 'STOP', 'TAG': 'STOP',
                  'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAT': 'N', 'AAC': 'N',
                  'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                  'TGT': 'C', 'TGC': 'C', 'TGA': 'STOP', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R',
                  'CGA': 'R', 'CGG': 'R', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                  'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    return codon_dict[dna_cod]


def parse(file_path):
    with open(file_path) as fasta_file:
        result = {}
        seq_id = ''
        for line in fasta_file:
            line = line.strip()
            print(line)
            if line[0] == '>':
                seq_id = line[1:]
                result[seq_id] = ''
            else:
                seq = line
                result[seq_id] += seq
    return result


def translate(dna_seq):
    start_codon = 'ATG'
    start_point = None
    for i in range(0, len(dna_seq)):
        if dna_seq[i:i+3] == start_codon:
            start_point = i
            break
    protein_seq = ''
    # check if START exists
    if start_point is not None:
        for j in range(start_point, len(dna_seq), 3):
            # check if codon consists of 3 letters, if less -> they are last letters -> were no STOP -> no protein
            # check if it is last codon and it is still not STOP -> no protein
            if len(dna_seq[j:j+3]) == 3 and (dna_seq[j:j+3] != dna_seq[-3:] or dna_codon(dna_seq[-3:]) == 'STOP'):
                amino_acid = dna_codon(dna_seq[j:j+3])
                if amino_acid == 'STOP':
                    break
                else:
                    protein_seq += amino_acid
            else:
                return 'No protein can be translated'
    return protein_seq


def calc_mass(prot_seq):
    result = 0
    for amino_acid in prot_seq:
        result += mass_table(amino_acid)
        return result


def orf(dna_seq):
    dna_seq_compl = ''
    compl_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for nucl in dna_seq[::-1]:
        dna_seq_compl += compl_dict[nucl]
    protein_seq = []
    for start in range(0, len(dna_seq) - 5):
        prot = translate(dna_seq[start:len(dna_seq)])
        if prot not in protein_seq and prot != 'No protein can be translated' and len(prot) > 0:
            protein_seq.append(prot)
    for start in range(len(dna_seq_compl) - 5):
        prot = translate(dna_seq_compl[start:len(dna_seq_compl)])
        if prot not in protein_seq and prot != 'No protein can be translated' and len(prot) > 0:
            protein_seq.append(prot)
    return protein_seq
