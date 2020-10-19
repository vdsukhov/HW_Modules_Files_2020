# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:07:51 2020

@author: Camille BENOIT
"""

complementary_dna = {"A" : "T", "C" : "G", "G": "C", "T" : "A"}

mass_table = {"A": 71.037114, "C": 103.009184, "D": 115.026943, "E": 129.042593, "F": 147.068414,
        "G": 57.021464, "H": 137.058912, "I": 113.084064, "K": 128.094963, "L": 113.084064,
        "M": 131.040485, "N": 114.042927, "P": 97.052764, "Q": 128.058578, "R": 156.101111,
        "S": 87.032028, "T": 101.047678, "V": 99.068414, "W": 186.079313, "Y": 163.063329 }

dna_codon = {"A" : ["GCT","GCC","GCA","GCG"], "R" : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"], 
             "N" : ["AAT", "AAC"], "D" : ["GAT", "GAC"], "C" : ["TGT", "TGC"], "Q": ["CAA", "CAG"],
             "E" : ["GAA", "GAG"], "F": ["TTT", "TTC"], "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
             "I": ["ATT", "ATC", "ATA"], "M" : ["ATG"], "V": ["GTT", "GTC", "GTA", "GTG"],
             "S" : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"], "P" : ["CCT", "CCC", "CCA", "CCG"],
             "T" : ["ACT", "ACC", "ACA", "ACG"], "Y" : ["TAT", "TAC"], "H" : ["CAT", "CAC"],
             "K" : ["AAA", "AAG"], "W" : ["TGG"], "G" : ["GGT", "GGC", "GGA", "GGG"]
             }


def parse(path_file):
    fasta_dic = dict()
    key = ""
    value = ""
    try :
        fasta_f = open(path_file, "r")
        lines = fasta_f.readlines()
        nb_lines = len(lines)
        i = 0
        while i < nb_lines :
            n_line = len(lines[i])
            if lines[i][0] == ">":
                key = lines[i][1: n_line - 1] ##we remove the "\n" of the end of the line
                value = ""
            else : 
                value += lines[i][:n_line - 1] ##we remove the "\n" of the end of the line
                if i == nb_lines - 1 or lines[i+1][0] == ">":
                    fasta_dic[key] = value
            i+=1
        return fasta_dic
    except FileNotFoundError :
        print("Error, such file doesn't exist")
        return {}

def translate(dna_seq): 
    n = len(dna_seq)
    start_codon = "ATG"
    result= ""
    i = dna_seq.index(start_codon) + 3
    is_there_end_codon = False
    while n - i >= 3 :
        if dna_seq[i:i+3] in ["TAA", "TAG", "TGA"] :
            is_there_end_codon = True
            break
        else :
            result += which_prot(dna_seq[i: i+3])
        i += 3
    if is_there_end_codon == False :
        return None
    return result

def which_prot(codon):
    for prot, codons in dna_codon.items() :
        if codon in codons :
            return prot
        
def calc_mass(prot_seq):
    mass = sum(mass_table[p] for p in prot_seq)
    return mass

def orf(dna_seq):
    result = []
    i = 0
    dna_seq_comp = get_complementary_dna(dna_seq)
    for i in range (len(dna_seq)-3) :
        if dna_seq[i:i+3] == "ATG" :
            if ("TAA" in dna_seq[i+3:]) or ("TAG" in dna_seq[i+3 :]) or ("TGA" in dna_seq[i + 3:]) :
                seq = translate(dna_seq[i :])
                if seq != None and ("M" + seq not in result):
                    result.append("M" + seq)
    for i in range (len(dna_seq_comp)-3) :
        if dna_seq_comp[i:i+3] == "ATG" :
            if ("TAA" in dna_seq_comp[i+3:]) or ("TAG" in dna_seq_comp[i+3 :]) or ("TGA" in dna_seq_comp[i + 3:]) :
                seq = translate(dna_seq_comp[i :])
                if seq != None and ("M" + seq not in result):
                    result.append("M" + seq)
    return result


def get_complementary_dna(dna_seq) :
    s = ""
    for i in range(len(dna_seq)):
        s += complementary_dna[dna_seq[i]]
    return "".join(reversed(s))
