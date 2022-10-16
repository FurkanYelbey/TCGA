import pandas as pd
import os

path = "E:\TCGA\\TCGA\\files" # path folder

dirs = os.chdir(path)

sample_id_file = "../files/gdc_sample_sheet.tsv"
sample_id = pd.read_csv(sample_id_file, sep='\t')
sample = sample_id['Sample ID'].tolist()            # Sample IDs
sampleFile = sample_id['File Name'].tolist()        # Sample's File Name

df = pd.DataFrame() #Creating Empty DataFrame

def MergeTsv():
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith("counts.tsv"):
            file_path = f"{path}\\{file}"

            file1 = pd.read_csv(file_path, sep='\t', skiprows=6, header=None)

            gene_values = file1[3].tolist()

            mergeIndex = 0 #merged table patient name column index
            for sampleIndex in range(len(sample)): #SampleCount
                if file == sampleFile[sampleIndex]: #Does file match sampleFile if matches put it into right index of columns
                    df.insert(mergeIndex, sample[sampleIndex], gene_values)
                    mergeIndex += 1

    gene_names = file1[0]
    df.insert(0, None, gene_names)
    df.to_csv('example.tsv', sep="\t", index = False)

MergeTsv()