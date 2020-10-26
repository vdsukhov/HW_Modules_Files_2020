import fastaparse

res_dict = fastaparse.parse("fasta_data.txt")
print(res_dict)

translated = fastaparse.translate("ACAGGACGGCATTGCCACGTCACGC"\
           "CGTTTTGCCAGAGACATCGATCGCG"\
           "AAGCCGATTTCGATGAGTCCCGCAT"\
           "GCCTAAGGCACAATAGAATGTAGCA"\
           "TCCAGACACTGAGGTGCGTCTGGAA"\
           "AAAGACACTCAGGGATAAAAATCAC"\
           "AGTACCACACAGTGCCGCAGCTCCG"\
           "AATGTCGAGGTTCATATAATCGGAC"\
           "CTTCTCTCTCGAAAGCTGACCTTCG"\
           "ACATGTAAAAGATAAATCCAGCAGA"\
           "TGCATGTAACCAAGGTCGGACCAGA")
print("Translated:",translated)

mass_prot = fastaparse.calc_mass(translated)
print("This is the protein's mass:",mass_prot)

orfs = fastaparse.orf("ACAGGACGGCATTGCCACGTCACGC"\
           "CGTTTTGCCAGAGACATCGATCGCG"\
           "AAGCCGATTTCGATGAGTCCCGCAT"\
           "GCCTAAGGCACAATAGAATGTAGCA"\
           "TCCAGACACTGAGGTGCGTCTGGAA"\
           "AAAGACACTCAGGGATAAAAATCAC"\
           "AGTACCACACAGTGCCGCAGCTCCG"\
           "AATGTCGAGGTTCATATAATCGGAC"\
           "CTTCTCTCTCGAAAGCTGACCTTCG"\
           "ACATGTAAAAGATAAATCCAGCAGA"\
           "TGCATGTAACCAAGGTCGGACCAGA")
print("ORF'S",orfs)