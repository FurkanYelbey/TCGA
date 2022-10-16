import pandas as pd
import os

path = "E:\TCGA\\TCGA\\files" # path folder

dirs = os.chdir(path)

sample_id_file = "../files/gdc_sample_sheet.tsv"

sample_id = pd.read_csv(sample_id_file, sep='\t')
sample = sample_id['Sample ID'].tolist()
sampleFile = sample_id['File Name'].tolist()

df = pd.DataFrame()

def firstfunction():
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith("counts.tsv"):
            file_path = f"{path}\\{file}"
            #print(file)

            file1 = pd.read_csv(file_path, sep='\t', skiprows=6, header=None)

            gene_values = file1[3].tolist()

            mergeIndex = 0 #merged table patient name column index
            for sampleIndex in range(len(sample)):
                #print(i)
                if file == sampleFile[sampleIndex]:
                    df.insert(mergeIndex, sample[sampleIndex], gene_values)
                    mergeIndex += 1

    gene_names = file1[0]
    df.insert(0, None, gene_names)

    print(df)
    #print(df.to_string(index=False))

    df.to_csv('example.tsv', sep="\t", index = False)

firstfunction()