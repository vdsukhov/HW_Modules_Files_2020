start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]
dna_codon = {"TTT": "F", "TTC": "F",
             "TTA": "L", "TTG": "L",
             "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
             "ATT": "I", "ATC": "I", "ATA": "I",
             "ATG": "M",
             "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
             "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
             "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
             "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
             "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
             "TAT": "Y", "TAC": "Y",
             "CAT": "H", "CAC": "H",
             "CAA": "Q", "CAG": "Q",
             "AAT": "N", "AAC": "N",
             "AAA": "K", "AAG": "K",
             "GAT": "D", "GAC": "D",
             "GAA": "E", "GAG": "E",
             "TGT": "C", "TGC": "C",
             "TGG": "W",
             "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
             "AGT": "S", "AGC": "S",
             "AGA": "R", "AGG": "R",
             "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

mass_table = {'G': 57.021464, 'A': 71.037114, 'S': 87.032028, 'P': 97.052764, 'V': 99.068414,
              'T': 101.047678, 'C': 103.009184, 'I': 113.084064, 'L': 113.084064,
              'N': 114.042927, 'D': 115.026943, 'Q': 128.058578, 'K':128.094963, 'E':129.042593,
              'M':131.040485, 'H':137.058912, 'F':147.068414, 'R':156.101111,
              'Y':163.063329, 'W':186.079313}


#parses a fasta file and returns a dictionary.
#The dictionary consists of pairs seq_id as string and the sequence itself seq as string or list
def parse(file_path):
    dict = {}
    key = ''
    value = ''
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith('>'):
                if value != '':
                    dict[key] = value
                key = line[1:].strip('\n')
                value = ''
            else:
                value += line.strip('\n')
        if not(key in dict.keys()):
            dict[key] = value
    return dict


#takes DNA sequence as a string and returns the protein string encoded by dna_seq as a string
def tr(s):
    res = ''
    for i in range(0, len(s) - 1, 3):
        res += dna_codon[s[i: i + 3]]
    return res


def translate(dna_seq):
    protein_start = dna_seq.find(start_codon) + 3
    for i in range(protein_start, len(dna_seq) - 1, 3):
        codon = dna_seq[i: i + 3]
        if codon in stop_codons:
            return tr(dna_seq[protein_start: i])


#takes a string encoding a protein and returns the mass as float
def calc_mass(prot_seq):
    return sum([mass_table[x] for x in prot_seq])


#takes DNA sequence as string and returns list of every distinct candidate protein string
#that can be translated from ORF of dna_seq
def orf(dna_seq):
    res = set()
    dcomplimentary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dna_reverse_seq = "".join([dcomplimentary[nucleotide] for nucleotide in dna_seq[::-1]])
    for i in range(len(dna_seq)-3):
        if dna_seq[i:i+3] == start_codon:
            for j in range(i, (len(dna_seq)-3)):
                if dna_seq[j:j+3] in stop_codons:
                    res.add('M' + (translate(dna_seq[i:]) or ''))
    for i in range(len(dna_reverse_seq) - 3):
        if dna_reverse_seq[i:i + 3] == start_codon:
            for j in range(i, (len(dna_reverse_seq) - 3)):
                if dna_reverse_seq[j:j + 3] in stop_codons:
                    res.add('M' + (translate(dna_reverse_seq[i:]) or ''))
    return list(res)

def test():
    res_dict = parse(r"C:\Users\yakup\PycharmProjects\python_hw4\fasta_data.txt")
    print(res_dict == {
        "fasta_0": "GTCCG",
        "fasta_1": "GATAATTCTATATGT",
        "fasta_2": "CGTGCCAGCGTGACAACGGGAAAACAAATAGCGG",
        "fasta_3": "CATTTACTATCTGTGACACCCGCAGTTCTCTGGACGGAATTCAATCGGTCTTTAAAACCTTTCAATTCTCGAGTGTGCGT",
        "fasta_4": "TTGTTGTACCCTTTTCGCATAAAGACCCCAATGAAATTACGGATCTGCGCGCGCCCATCCCGAAAAGCGTGAGCCACTACAAAAGCGCATGCTATGCTTCTTAAGGTCACTGAGCTCTCCACTTTAGGCAG"
    })

    dna_seq = "ACAGGACGGCATTGCCACGTCACGC"\
               "CGTTTTGCCAGAGACATCGATCGCG"\
               "AAGCCGATTTCGATGAGTCCCGCAT"\
               "GCCTAAGGCACAATAGAATGTAGCA"\
               "TCCAGACACTGAGGTGCGTCTGGAA"\
               "AAAGACACTCAGGGATAAAAATCAC"\
               "AGTACCACACAGTGCCGCAGCTCCG"\
               "AATGTCGAGGTTCATATAATCGGAC"\
               "CTTCTCTCTCGAAAGCTGACCTTCG"\
               "ACATGTAAAAGATAAATCCAGCAGA"\
               "TGCATGTAACCAAGGTCGGACCAGA"

    orfs = orf(dna_seq)
    print(set(orfs) == set(["MSKVSFRERRSDYMNLDIRSCGTVWYCDFYP",
            "MLHSIVP", "MPKAQ", "MNLDIRSCGTVWYCDFYP",
            "M", "MHLLDLSFTCRRSAFEREGPII", "MSRFI",
            "MSPACLRHNRM"]))
