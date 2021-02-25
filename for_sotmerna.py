from pathlib import Path
import os


for el in Path('/scratch/mshumilova/samples').glob('*'):
    if '_R1_' not in str(el):
        continue
    pairname = str(el).replace('_R1_', '_R2_')
    #print(str(el), pairname)

    #1. unzip two reads of sample (R1,R2)

    ######### was trying to use a shutil, but it was too difficult for .gz format

    unzip_el = Path('/scratch/mshumilova/gunzip/')/el.stem 
    unzip_pairname = str(unzip_el).replace('_R1_', '_R2_')     

    cmd_unzip_el = f'gunzip -c {str(el)} > {unzip_el}'
    cmd_unzip_pairname = f'gunzip -c {pairname} > {unzip_pairname}'
    
    print('\n', '#1 gunzip R1', '\n\n', cmd_unzip_el)
    print('\n', '#1 gunzip R2', '\n\n', cmd_unzip_pairname)
    
    #os.system(cmd_unzip_el)
    #os.system(cmd_unzip_pairname)

    #2. Merge two reads into one

    end = unzip_el.name.replace('_R1_', '_merged_')
    outfile = '/scratch/mshumilova/sortmerna-2.1/merged/' + end

    cmd_merged = f'/scratch/mshumilova/sortmerna-2.1/scripts/merge-paired-reads.sh {unzip_el} {unzip_pairname} {outfile}'
    print('\n','#2 merge R1 and R2', '\n\n', cmd_merged)
    #os.system(cmd_merged)

    #3. Sort

    reads = outfile #take a merged file as input

    aligned = reads.replace('_001','_001_rRNA') #output_aligned file's name
    aligned = aligned.replace('/sortmerna-2.1/merged/', '/sortme/rRNA/') #output_aligned directory
    #print(aligned)
    other = aligned.replace('_rRNA', '_non_rRNA') #output_other file's name
    other = other.replace('/rRNA/', '/non_rRNA/') #outpur_other directory
    #print(other)
    
    cmd_sort = f'/scratch/mshumilova/sortmerna-2.1/sortmerna \
--ref /scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/silva-bac-23s-id98.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/silva-bac-23s-db:\
/scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/silva-arc-16s-id95.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/silva-arc-16s-db:\
/scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/silva-arc-23s-id98.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/silva-arc-23s-db:\
/scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/silva-euk-18s-id95.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/silva-euk-18s-db:\
/scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/silva-euk-28s-id98.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/silva-euk-28s:\
/scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/rfam-5s-database-id98.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/rfam-5s-db:\
/scratch/mshumilova/sortmerna-2.1/sortmerna_db/rRNA_databases/rfam-5.8s-database-id98.fasta,/scratch/mshumilova/sortmerna-2.1/sortmerna_db/index/rfam-5.8s-db \
--reads {reads} \
--aligned {aligned} \
--other  {other} \
--paired_out \
--fastx \
--log \
-a 32 \
-v' 

    print('\n','#3 sort', '\n\n', cmd_sort)
    #os.system(cmd_sort)

    #4. Unmerge
    
    merged_read = other
    forward_read = merged_read.replace('_merged_', '_R1_')
    forward_read = forward_read.replace('/non_rRNA/', '/samples_after_sortme/')
    reverse_read = forward_read.replace('_R1_', '_R2_')

    cmd_unmerge = f'/scratch/mshumilova/sortmerna-2.1/scripts/unmerge-paired-reads.sh {merged_read} {forward_read} {reverse_read}'
    print('\n','#4 unmerge', '\n\n', cmd_unmerge)
    #os.system(cmd_unmerge)
    
    #5. Zip

    cmd_gzip = f'gzip {forward_read}'
    print('\n','#5 gzip samples after sortmerna', '\n\n', cmd_gzip)
    #os.system(cmd_gzip)

    #6. Removing of intermediate files 

    cmd_clear_gunzip_dir = f'rm /scratch/mshumilova/gunzip/*'
    cmd_clear_merge_dir = f'rm /scratch/mshumilova/sortmerna-2.1/merged/*'
    cmd_clear_rRNA_dir = f'rm /scratch/mshumilova/sortme/rRNA/*'
    cmd_clear_non_rRNA_dir = f'rm /scratch/mshumilova/sortme/non_rRNA/*'
    
    print('\n','#6 removing of intermediate files', '\n\n', cmd_clear_gunzip_dir, '\n', cmd_clear_merge_dir,'\n', cmd_clear_rRNA_dir, '\n', cmd_clear_non_rRNA_dir)

    #os.system(cmd_clear_gunzip_dir)
    #os.system(cmd_clear_merge_dir)
    #os.system(cmd_clear_rRNA_dir)
    #os.system(cmd_clear_non_rRNA_dir)
    
