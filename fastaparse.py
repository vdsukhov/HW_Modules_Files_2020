from pathlib import Path

mass_table = {
    "G":57.021464, "A":71.037114, "S":87.032028,
    "P":97.052764, "V":99.068414, "T":101.047678,
    "C":103.009184, "I":113.084064, "L":113.084064,
    "N":114.042927, "D":115.026943, "Q":128.058578,
    "K":128.094963, "E":129.042593, "M":131.040485,
    "H":137.058912, "F":147.068414, "R":156.101111,
    "Y":163.063329, "W":186.079313}
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop', 
    'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W'}

def calc_mass(prot_seq):
    sum = 0
    for i in prot_seq:
        sum += mass_table.get(i)
    return round(sum,5)

def translate(s):
    f_start = s.find('ATG')
    f_start+=3
    separ_cod = [s[i:i+3] for i in range(f_start, len(s), 3)]
    prot = []
    k = 0
    while True:
        t = dna_codon.get(separ_cod[k]) 
        if t == 'Stop':
            break
        prot.append(t)
        k+=1
    m=''.join(x for x in prot)
    return m

def parse(file_path):
    pre_list = []
    my_keys = []
    my_values = []
    values_counter = 0
    
    filename = Path(file_path)
    
    with open(filename) as f:
        read_data = f.readlines()
        
    for line in read_data:
        pre_list.append(line.strip('\n'))
        

    for line in range(len(pre_list)):
        if pre_list[line][0] == '>':
            my_keys.append(pre_list[line][1:])
        else:
            if pre_list[line - 1][1:] in my_keys:
                my_values.append(pre_list[line])
                values_counter += 1
            else:
                my_values[values_counter-1].join(pre_list[line])
                
    my_dictionary = dict(zip(my_keys, my_values))
    
    return(my_dictionary)

def _prot(s):
    k = 0
    prot = []
    s = s[s.index('ATG'):]
    
    if ('TAG' in s) or ('TGA' in s) or ('TAA' in s):
        while k < len(s):
            t = dna_codon.get(s[k]) 
            if t == 'Stop':
                break
            prot.append(t)
            k+=1
            
    m = ''.join(x for x in prot)
    
    return m

def _get_prot(s):
    counter = s.count('ATG')
    m = []
    ktr = 0
    
    while ktr<counter:     
        m.append(_prot(s))
        s = s[(s.index('ATG'))+1:]
        ktr+=1
        if ktr == (counter-1) :
            if ('TAG' in s) or ('TGA' in s) or ('TAA'in s):
                m.append(_prot(s))
                break
                
    return m

def orf(s):
    ori = []
    pair = []
    full_tri = []
    fair = []
    ans = []
    prots = []
    s_pair = ''
    
    for letter in s:
        if letter == "A":
            s_pair += 'T'
        elif letter == "T":
            s_pair += 'A'
        elif letter == "G":
            s_pair += 'C'
        elif letter == "C":
            s_pair += 'G'
            
    s_pair_r = s_pair[::-1]
    
    for i in range(1,4):
        read = s[i:]
        read_p = s_pair_r[i:]
        ori.append(read)
        pair.append(read_p)
        
    full_lines = ori + pair
    
    for line in full_lines:
        full_tri.append([line[i:i+3] for i in range(0, len(line), 3)])
        
    for lst in full_tri:
        for tri in lst:
            if len(tri) != 3:
                lst.remove(tri)
                
    for seq in full_tri:
        if ("ATG" in seq):
            fair.append(seq)
            
    for line in fair:
        prots.append(_get_prot(line))
        
    for i in prots:
        for string in i:
            if string != '' and string not in ans:
                ans.append(string)

    return ans
