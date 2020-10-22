# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:42:51 2020

@author: Alexandra Giraud 
"""

#monoisotopic mass table dictionnary
mass_table = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
              "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
              "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
              "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
              "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}

#dna codon table dictionnary 
dna_codon = {
    'TCA' : 'S',    # Serine
    'TCC' : 'S',    # Serine
    'TCG' : 'S',    # Serine
    'TCT' : 'S',    # Serine
    'TTC' : 'F',    # Phenylalanine
    'TTT' : 'F',    # Phenylalanine
    'TTA' : 'L',    # Leucine
    'TTG' : 'L',    # Leucine
    'TAC' : 'Y',    # Tyrosine
    'TAT' : 'Y',    # Tyrosine
    'TAA' : 'STOP',    # Stop
    'TAG' : 'STOP',    # Stop
    'TGC' : 'C',    # Cysteine
    'TGT' : 'C',    # Cysteine
    'TGA' : 'STOP',    # Stop
    'TGG' : 'W',    # Tryptophan
    'CTA' : 'L',    # Leucine
    'CTC' : 'L',    # Leucine
    'CTG' : 'L',    # Leucine
    'CTT' : 'L',    # Leucine
    'CCA' : 'P',    # Proline
    'CCC' : 'P',    # Proline
    'CCG' : 'P',    # Proline
    'CCT' : 'P',    # Proline
    'CAC' : 'H',    # Histidine
    'CAT' : 'H',    # Histidine
    'CAA' : 'Q',    # Glutamine
    'CAG' : 'Q',    # Glutamine
    'CGA' : 'R',    # Arginine
    'CGC' : 'R',    # Arginine
    'CGG' : 'R',    # Arginine
    'CGT' : 'R',    # Arginine
    'ATA' : 'I',    # Isoleucine
    'ATC' : 'I',    # Isoleucine
    'ATT' : 'I',    # Isoleucine
    'ATG' : 'M',    # Methionine #START ?
    'ACA' : 'T',    # Threonine
    'ACC' : 'T',    # Threonine
    'ACG' : 'T',    # Threonine
    'ACT' : 'T',    # Threonine
    'AAC' : 'N',    # Asparagine
    'AAT' : 'N',    # Asparagine
    'AAA' : 'K',    # Lysine
    'AAG' : 'K',    # Lysine
    'AGC' : 'S',    # Serine
    'AGT' : 'S',    # Serine
    'AGA' : 'R',    # Arginine
    'AGG' : 'R',    # Arginine
    'GTA' : 'V',    # Valine
    'GTC' : 'V',    # Valine
    'GTG' : 'V',    # Valine
    'GTT' : 'V',    # Valine
    'GCA' : 'A',    # Alanine
    'GCC' : 'A',    # Alanine
    'GCG' : 'A',    # Alanine
    'GCT' : 'A',    # Alanine
    'GAC' : 'D',    # Aspartic Acid
    'GAT' : 'D',    # Aspartic Acid
    'GAA' : 'E',    # Glutamic Acid
    'GAG' : 'E',    # Glutamic Acid
    'GGA' : 'G',    # Glycine
    'GGC' : 'G',    # Glycine
    'GGG' : 'G',    # Glycine
    'GGT' : 'G',    # Glycine
    }


#file_path = r"C:\Users\sacho\Documents\3A ITMO\Python\HW_Modules_Files_2020\fasta_data.txt"
def parse(file_path):
    '''
    function that parses a fasta file and returns a dictionary.
    The dictionary consists of pairs seq_id
    as string and the sequence itself seq as string.
    
    '''
    fasta = dict()
    try:
        key = ""
        val = ""         
        fafile = open(file_path,"r")
        lines = fafile.readlines()
        for i in range((len(lines))):
            if lines[i][0] == ">":
                key = lines[i][1: len(lines[i]) - 1] 
                val = ""
            else : 
                val += lines[i][:len(lines[i]) - 1] 
                if i == len(lines) - 1 or lines[i+1][0] == ">":
                    fasta[key] = val
        return fasta
    except:
        print("Error , the file can't be read")
        return {}
    
def translate(dna_seq):
    '''
    returns the protein string encoded by dna_seq as a string
    the starting codon is ATG
    stop codon is either TAA, TAG or TGA as in dna_seq table
    '''
    start = 'ATG'
    startPoint = dna_seq.find(start)
    seq = ''
    if startPoint != -1:   #if the function was able to fins at least one start codon 
        seqStart = dna_seq[int(startPoint):]
        for i in range(0, len(seqStart), 3):
            if len(seqStart[i:i + 3]) == 3:
                 if dna_codon[seqStart[i:i + 3]] == "STOP":
                     break
                 else:
                    seq += dna_codon[seqStart[i:i + 3]]
                    
        return(seq)
    elif seq != "":
        return(seq)
    
def calcul_mass(prot_seq):
    '''
     This function takes a string encoding a protein
     (need to use translate function before)
     and returns the mass as float
     '''
    mass = 0.0
    for l in prot_seq:
        mass += mass_table[l]
    return mass
    

def complementarySeq(dna_seq):
    '''
    takes a sequence and returns the string with the complementary seq (with complementary dna aminoAcid)
    and reversed
    '''
    comple_dna = {'A' : 'T','T' : 'A', 'C' : 'G', 'G': 'C'}
    seq = str()
    longueur = len(dna_seq)
    for i in range(longueur):
        seq+= comple_dna[dna_seq[i]]
    revseq = reversed(seq)
    return "".join(revseq)

def candidates(seq):
    '''
    tests for distinc candidates among a sequence
    '''
    candidates = []
    start = 'ATG'
    longueur = len(seq)
    for i in range(longueur -3):
        if seq[i:i+3] == start:
            if ('TAA' or 'TAG' or 'TGA' in seq[i+3:]):
                seqBis = translate(seq[i:])
                if len(seqBis) != 0 and (('M' + seqBis) not in candidates):
                    candidates.append('M' + seqBis)
    return candidates

def orf(dna_seq):
    '''
     This function takes a string encoding a protein
     and returns the mass as float.
     Function orf(dna_seq). This function
     takes DNA sequence as string and returns 
     list of every distinct candidate protein
     string that can be translated from Open Reading Frames of dna_seq
    '''
    result = list()
    seq_complementary = complementarySeq(dna_seq)
    result = candidates(dna_seq) + candidates(seq_complementary)
    return result
  
    
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
          




