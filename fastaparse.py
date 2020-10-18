mass_table={'G': 57.021464,
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
 'K': 128.094963,
 'Q': 128.058578,
 'E': 129.042593,
 'M': 131.040485,
 'H': 137.058912,
 'F': 147.068414,
 'R': 156.101111,
 'Y': 163.063329,
 'W': 186.079313}
dna_codon={ 
        'ATA':'I', 
    'ATC':'I', 
    'ATT':'I', 
    'ATG':'M', 
    'ACA':'T', 
    'ACC':'T', 
    'ACG':'T', 
    'ACT':'T', 
    'AAC':'N', 
    'AAT':'N', 
    'AAA':'K', 
    'AAG':'K', 
    'AGC':'S', 
    'AGT':'S', 
    'AGA':'R', 
    'AGG':'R',                  
    'CTA':'L', 
    'CTC':'L', 
    'CTG':'L', 
    'CTT':'L', 
    'CCA':'P', 
    'CCC':'P', 
    'CCG':'P', 
    'CCT':'P', 
    'CAC':'H', 
    'CAT':'H', 
    'CAA':'Q', 
    'CAG':'Q', 
    'CGA':'R', 
    'CGC':'R', 
    'CGG':'R', 
    'CGT':'R', 
    'GTA':'V', 
    'GTC':'V', 
    'GTG':'V', 
    'GTT':'V', 
    'GCA':'A', 
    'GCC':'A', 
    'GCG':'A', 
    'GCT':'A', 
    'GAC':'D', 
    'GAT':'D', 
    'GAA':'E', 
    'GAG':'E', 
    'GGA':'G', 
    'GGC':'G', 
    'GGG':'G', 
    'GGT':'G', 
    'TCA':'S', 
    'TCC':'S', 
    'TCG':'S', 
    'TCT':'S', 
    'TTC':'F', 
    'TTT':'F', 
    'TTA':'L', 
    'TTG':'L', 
    'TAC':'Y', 
    'TAT':'Y', 
    'TAA':'STOP', 
    'TAG':'STOP', 
    'TGC':'C', 
    'TGT':'C', 
    'TGA':'STOP', 
    'TGG':'W', 
    } 
def translate(dna_seq):
    Codons = []
    for i in range(0,(len(dna_seq)-2),3):
        word = '{}{}{}'.format(dna_seq[i],dna_seq[i+1],dna_seq[i+2])
        Codons.append(word)
    prtn = ''
    for i in Codons:
        if i in ['TAA','TAG','TGA']:
            break
        else:
            for z in dna_codon:
                if i == z:
                    prtn += dna_codon[z]
    return prtn
def calc_mass(prot_seq):
    mass=0
    for i in prot_seq:
        mass+=mass_table[i]
    return mass
def parse(path):
    res_dict={}
    curr_id=''
    with open('fasta.txt') as file:
        for line in file:
            lineseq=line.strip().split(' ')
            if lineseq[0][0] == '>':
                curr_id=lineseq[0][1:]
                res_dict[curr_id]=''
            else:
                res_dict[curr_id]+=lineseq[0]
    return(res_dict)
def orf(dna_seq):
    rv=dna_seq[::-1]
    complements={'A':'T','C':'G','G':'C','T':'A'}
    rvcomp=''
    for i in rv:
        rcvcomp_elem=complements[i]
        rvcomp+=rcvcomp_elem
    trans_res=[]
    reading_frames=[[],[],[],[],[],[]]
    for i in range(0,(len(dna_seq)-2),3):
        wordf = '{}{}{}'.format(dna_seq[i],dna_seq[i+1],dna_seq[i+2])
        wordr = '{}{}{}'.format(rvcomp[i],rvcomp[i+1],rvcomp[i+2])
        reading_frames[0].append(wordf)
        reading_frames[1].append(wordr)
    for i in range(1,(len(dna_seq)-2),3):
        wordf = '{}{}{}'.format(dna_seq[i],dna_seq[i+1],dna_seq[i+2])
        wordr = '{}{}{}'.format(rvcomp[i],rvcomp[i+1],rvcomp[i+2])
        reading_frames[2].append(wordf)
        reading_frames[3].append(wordr)
    for i in range(2,(len(dna_seq)-2),3):
        wordf = '{}{}{}'.format(dna_seq[i],dna_seq[i+1],dna_seq[i+2])
        wordr = '{}{}{}'.format(rvcomp[i],rvcomp[i+1],rvcomp[i+2])
        reading_frames[4].append(wordf)
        reading_frames[5].append(wordr)
    started=0
    first_translations=[]
    orfs={}
    for i in range(len(reading_frames)):
        orfs[i]=[]
        crfs=[]
        for j in range(len(reading_frames[i])):
            if reading_frames[i][j] in ['TAA','TAG','TGA']:
                crfs.append(j)
        for m in range(len(reading_frames[i])):
            if reading_frames[i][m]=='ATG':
                orfs[i].append(m)
        if len(crfs)>0:
            max_crfs=crfs[-1]
        else:
            max_crfs=0
        orfs_to_remove=[]
        for z in orfs[i]:
            if z>max_crfs:
                orfs_to_remove.append(z)
        for n in orfs_to_remove:
            orfs[i].remove(n)
    for i in reading_frames:
        dnastr=''.join(i)
        first_translations.append(translate(dnastr))
    
    res_pep=[]
    for key in orfs:
        for value in orfs[key]:
            rf=reading_frames[key]
            fragment=''.join(reading_frames[key][value:])
            newpep=translate(fragment)
            res_pep.append(newpep)
    return(list(set(res_pep)))
