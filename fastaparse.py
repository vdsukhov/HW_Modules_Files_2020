
mass_table={'G':57.021464, 'A':71.037114, 'S':87.032028, 'P':97.052764, 'V':99.068414,
            'T':101.047678, 'C':103.009184, 'I':113.084064, 'L':113.084064, 'N':114.042927,
            'D':115.026943, 'Q':128.058578, 'K':128.094963, 'E':129.042593, 'M':131.040485, 
            'H':137.058912, 'F':147.068414, 'R':156.101111, 'Y':163.063329, 'W': 186.079313}

dna_codon={'GCT' : 'A', 'GCC' :'A', 'GCA' : 'A', 'GCG' : 'A' , 
           'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGA' : 'R', 'AGG' : 'R', 
           'AAT' :'N', 'AAC' :'N', 'GAT' :'D', 'GAC' :'D', 'TGT' :'C', 'TGC' :'C', 
           'CAA' :'Q', 'CAG' :'Q', 'GAA' :'E', 'GAG' :'E', 'GAG' :'Z', 'GGT' :'G', 'GGC' :'G', 
           'GGA' :'G', 'GGG' :'G', 'CAT' :'H', 'CAC' :'H', 'ATT' :'I', 'ATC' :'I', 'ATA' :'I', 
           'CTT' :'L', 'CTC' :'L', 'CTA' :'L', 'CTG' :'L', 'TTA' :'L', 'TTG' :'L', 
           'AAA' :'K', 'AAG' :'K', 'ATG' :'M', 'TTT' :'F', 'TTC' :'F', 
           'CCT' :'P', 'CCC' :'P', 'CCA' :'P', 'CCG' :'P', 
           'TCT' :'S', 'TCC' :'S', 'TCA' :'S', 'TCG' :'S', 'AGT' :'S', 'AGC' :'S', 
           'ACT' :'T', 'ACC' :'T', 'ACA' :'T', 'ACG' :'T', 
           'TGG' :'W', 'TAT' :'Y', 'TAC' :'Y', 'GTT' :'V', 'GTC' :'V', 'GTA' :'V', 'GTG' :'V'}

def parse(file_path):
  keyid=[]
  seqs=[]
  with open(file_path, "r") as inpf:
    for line in inpf:
      line=line.strip()
      if ">" in line:
        keyid.append(line[1:])
      else:
        seqs.append(line)
  res={i:j for i in keyid for j in seqs}
  return(res)

def translate(dna_seq):
  stop=('TAA', 'TGA', 'TAG')
  seqsrt=''
  for n in range(len(dna_seq)):
    if dna_seq[n:n+3] == 'ATG':
      seqsrt=dna_seq[n+3:]
      break
    n+=3
  ss=''
  n=0
  while n < len(seqsrt):
    if seqsrt[n:n+3] in stop:
      break
    else:
      ssend=seqsrt[:n]
      ss+=dna_codon[seqsrt[n:n+3]]
    n+=3
  return(ss)

def calc_mass(prot_seq):
  ms=0
  for chr in seq:
    ms+=ld[chr]
  return(ms)

def orf_one(ls):
  starts=[]
  i=0
  while i < len(ls):
    if ls[i:].find('ATG') != -1:
      starts.append(i+ls[i:].find('ATG'))
    i+=ls[i:].find('ATG')+3

  stop=('TAA', 'TGA', 'TAG')
  ends=[]
  for elem in stop:
    i=0
    while i < len(ls):
      if ls[i:].find(elem) != -1:
        ends.append(i+ls[i:].find(elem))
      i+=ls[i:].find(elem)+3

  seqs=[]
  for i in starts:
    for j in sorted(ends):
      if j>i and (j - i) % 3 == 0:
        codons=str()
        n=0
        while n < len(ls[i:j]):
          if ls[i:j][n:n+3] in stop:
            break
          else:
            codons+=dna_codon[ls[i:j][n:n+3]]
          n+=3
        if codons not in seqs:
          seqs.append(codons)
        break
  return seqs

def orf(dna_seq):
  orfs=[]
  orf_one(dna_seq)
  orfs+=orf_one(dna_seq)
  revers=dna_seq[::-1]
  revers_c=str()
  for i in revers:
    if i == "A": 
      i = "T"
    elif i == "T":
      i = "A"
    elif i == "C":
      i = "G"
    else:
      i = "C"
    revers_c+=i
  orf_one(revers_c)
  orfs+=orf_one(revers_c)
  orfs_end=[]
  for elem in orfs:
    if elem not in orfs_end:
      orfs_end.append(elem)
  return orfs_end

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
