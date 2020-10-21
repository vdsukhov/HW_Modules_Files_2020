# -*- coding: utf-8 -*-

#fastaparse.py


#The monoisotopic mass table for amino acids as a dictionary mass_table

mass_table = dict()
mass_table["G"] = 57.021464
mass_table["A"] = 71.037114
mass_table["S"]	= 87.032028
mass_table["P"] = 97.052764
mass_table["V"] = 99.068414
mass_table["T"] = 101.047678
mass_table["C"]	= 103.009184
mass_table["I"]	= 113.084064
mass_table["L"] = 113.084064
mass_table["N"] = 114.042927
mass_table["D"] = 115.026943
mass_table["Q"] = 128.058578
mass_table["K"]	= 128.094963
mass_table["E"] = 129.042593
mass_table["M"]	= 131.040485
mass_table["H"]	= 137.058912
mass_table["F"] = 147.068414
mass_table["R"] = 156.101111
mass_table["Y"] = 163.063329
mass_table["W"] = 186.079313

#DNA codon table as a dictionary dna_codon

#stocke les correspondance des triplets
dna_codon = dict()
dna_codon["TTT"] = "F"
dna_codon["TTC"] = "F"
dna_codon["TTA"] = "L"
dna_codon["TTG"] = "L"
dna_codon["TCT"] = "S"
dna_codon["TCC"] = "S"
dna_codon["TCA"] = "S"
dna_codon["TCG"] = "S"
dna_codon["TAT"] = "Y"
dna_codon["TAC"] = "Y"
dna_codon["TAA"] = "Stop"
dna_codon["TAG"] = "Stop"
dna_codon["TGT"] = "C"
dna_codon["TGC"] = "C"
dna_codon["TGA"] = "Stop"
dna_codon["TGG"] = "W"
dna_codon["CTT"] = "L"
dna_codon["CTC"] = "L"
dna_codon["CTA"] = "L"
dna_codon["CTG"] = "L"
dna_codon["CCT"] = "P"
dna_codon["CCC"] = "P"
dna_codon["CCA"] = "P"
dna_codon["CCG"] = "P"
dna_codon["CAT"] = "H"
dna_codon["CAC"] = "H"
dna_codon["CAA"] = "Q"
dna_codon["CAG"] = "Q"
dna_codon["CGT"] = "R"
dna_codon["CGC"] = "R"
dna_codon["CGA"] = "R"
dna_codon["CGG"] = "R"
dna_codon["ATT"] = "I"
dna_codon["ATC"] = "I"
dna_codon["ATA"] = "I"
dna_codon["ATG"] = "M"
dna_codon["ACT"] = "T"
dna_codon["ACC"] = "T"
dna_codon["ACA"] = "T"
dna_codon["ACG"] = "T"
dna_codon["AAT"] = "N"
dna_codon["AAC"] = "N"
dna_codon["AAA"] = "K"
dna_codon["AAG"] = "K"
dna_codon["AGT"] = "S"
dna_codon["AGC"] = "S"
dna_codon["AGA"] = "R"
dna_codon["AGG"] = "R"
dna_codon["GTT"] = "V"
dna_codon["GTC"] = "V"
dna_codon["GTA"] = "V"
dna_codon["GTG"] = "V"
dna_codon["GCT"] = "A"
dna_codon["GCC"] = "A"
dna_codon["GCA"] = "A"
dna_codon["GCG"] = "A"
dna_codon["GAT"] = "D"
dna_codon["GAC"] = "D"
dna_codon["GAA"] = "E"
dna_codon["GAG"] = "E"
dna_codon["GGT"] = "G"
dna_codon["GGC"] = "G"
dna_codon["GGA"] = "G"
dna_codon["GGG"] = "G"
#On rajoute le start !
dna_codon["ATG"] = "Start"

# parses a fasta file and returns a dictionary. The dictionary consists of pairs
# seq_id as string and the sequence itself seq as string or list.

def parse(file_path): #<FINISHED>
    try:
        res = dict()
        fileToRead = open(file_path,"r")
        titleSequence = ""
        for line in fileToRead.readlines():
            if len(line) != 0 and line[0] == ">":
                res[line[1:].replace("\n","")]= ""
                titleSequence = line[1:].replace("\n","")
            elif len(line) != 0:
                res[titleSequence] = line.replace("\n","")
        fileToRead.close()
        return res
    except:
        print("Error : can't read the file")

def translate(dna_seq): 
    res = ""
    #We go triplet by triplet
    i = 0
    while i < len(dna_seq):
        triplet = dna_seq[i:i+3]
        if len(triplet) != 0:
            try :
                res += dna_codon[triplet]
            except:
                pass #we go here if we have not a three letter part or the three letters mean nothing
        i+=3
    return res

# This function takes a string encoding a protein and returns the mass as float.

def calc_mass(prot_seq): 
    res = 0.0
    for letter in prot_seq:
        res += mass_table[letter]
    return res

# This function takes DNA sequence as a string and returns the protein string encoded by dna_seq as a string

def orf(dna_seq):
    res = list()
    candidate = list() #toutes les possibilités de parcours
    start = ["ATG"]
    stop = ["TAA","TAG","TGA"]
    endroit = dna_seq
    envers = dna_seq[::-1]
    #PRODUCTING THE SIX SEQUENCE (Reverse, Normal)
    candidate.append(endroit)
    candidate.append(endroit[1:])
    candidate.append(endroit[2:])
    candidate.append(envers)
    candidate.append(envers[1:])
    candidate.append(envers[2:])
    #PRODUCTING TRANSLATION
    toTranslate = list()
    for sequence in candidate:
        #Take what is between a start and a stop
        tampon = "" #The chain to be traited
        i = 0
        while i < len(sequence):
            if sequence[i:i+3] in start:
                tampon = "" # to encounter a start means reinitialisation
            elif sequence[i:i+3] in stop:
                toTranslate.append(tampon) #to encounter a stop means sending the actual composed sequence for traduction
            else:
                if len(sequence[i:i+3]) == 3: #traduction of the three letters if only they are actually three
                    tampon += sequence[i:i+3] 
                else:
                    tampon = "" #we have a wrong sequence, the sequence is reset !
            i+=3
    #After slice, time to do translation
    for element in toTranslate:
        if len(element) > 0: #we consider only the non empty sequences
            res.append(translate(element))
    return res
