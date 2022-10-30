import pandas as pd
import os

def MergeTsv(filesPath, sampleSheetPath, outputPath, selectedColumn, dataType):
    #path = os.getcwd()+"\\files"
    path=filesPath

    #sample_id_file = "files/gdc_sample_sheet.2022-10-22.tsv"
    sample_id_file = sampleSheetPath
    sample_id = pd.read_csv(sample_id_file, sep='\t')
    sample = sample_id['Sample ID'].tolist()            # Sample IDs
    sampleFile = sample_id['File Name'].tolist()        # Sample's File Name

    df = pd.DataFrame() #Creating Empty DataFrame

    subfolders = [f.path for f in os.scandir(path) if f.is_dir()] # named by fileID

    for paths in subfolders:
        for file in os.listdir(paths):
            # Check whether file is in text format or not
            if dataType == 1:
                if file.endswith("counts.tsv"):
                    file_path = f"{paths}\\{file}"

                    file1 = pd.read_csv(file_path, sep='\t', skiprows=6, header=None)


                    gene_values = file1[selectedColumn].tolist()#selectedColumn yaz indexe

                    mergeIndex = 0 #merged table patient name column index
                    for sampleIndex in range(len(sample)): #SampleCount
                        if file == sampleFile[sampleIndex]: #Does file match sampleFile if matches put it into right index of columns
                            df.insert(mergeIndex, sample[sampleIndex], gene_values, allow_duplicates=True)
                            mergeIndex += 1
            if dataType == 2:
                if file.endswith("betas.txt"):
                    file_path = f"{paths}\\{file}"

                    file1 = pd.read_csv(file_path, sep='\t', header=None)

                    gene_values = file1[selectedColumn].tolist()#selectedColumn yaz indexe

                    mergeIndex = 0
                    for sampleIndex in range(len(sample)):
                        if file== sampleFile[sampleIndex]:
                            df.insert(mergeIndex, sample[sampleIndex], gene_values)
                            mergeIndex += 1

    gene_names = file1[0]
    df.insert(0, None, gene_names)
    df.to_csv(outputPath+'\\example.tsv', sep="\t", index = False)# outpputh path çalışıyor
    print("Success")

#MergeTsv()