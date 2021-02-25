
from pathlib import Path
import os

pairname = ''
out1_paired = ''
out1_unpaired = ''
out2_paired = ''
out2_unpaired = ''

for el in Path('/scratch/mshumilova/filtered_by_tile/').rglob('*'):
    if '_R1_' not in str(el):
        continue
    pairname = str(el).replace('_R1_', '_R2_')

    out1_paired = str(el).replace('/filtered_by_tile/', '/trimm/') 
    out1_paired = out1_paired.replace('.fq.gz', '.trimm_20_paired_1.fq.gz')
    out1_unpaired = out1_paired.replace('_paired', '_unpaired')

    out2_paired = pairname.replace('/filtered_by_tile/', '/trimm/')
    out2_paired = pairname.replace('.fq.gz', '.trimm_20_paired_2.fq.gz')
    out2_unpaired = out2_paired.replace('_paired', '_unpaired')
    cmd = f'java -jar Trimmomatic-0.39/trimmomatic-0.39.jar PE -phred33 {str(el)} {pairname} {out1_paired} {out1_unpaired} {out2_paired} {out2_unpaired} LEADING:20 TRAILING:20 SLIDINGWINDOW:5:20 MINLEN:60'

    print(cmd)
    os.system(cmd) 




