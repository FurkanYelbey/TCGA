import pandas as pd
import os
import win32api

def MergeTsv(filesPath, sampleSheetPath, outputPath, selectedColumn, dataType, mergedFileName):
    path=filesPath

    #sample_id_file = "files/gdc_sample_sheet.2022-10-22.tsv"
    sample_id_file = sampleSheetPath
    sample_id = pd.read_csv(sample_id_file, sep='\t')
    sample = sample_id['Sample ID'].tolist()            # Sample IDs
    sampleFile = sample_id['File Name'].tolist()        # Sample's File Name

    df = pd.DataFrame() #Creating Empty DataFrame

    subfolders = [f.path for f in os.scandir(path) if f.is_dir()] # named by fileID

    try:
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
                                df.insert(mergeIndex, sample[sampleIndex], gene_values, allow_duplicates= True)
                                mergeIndex += 1
    except KeyError:
        win32api.MessageBox(None, "You selected the blank columns. Please select again", "Warning")

    else:
        try:
            gene_names = file1[0]
            df.insert(0, None, gene_names)
            df.to_csv(outputPath + '\\' + mergedFileName + '.tsv', sep="\t", index=False)
            del df#destroy dataframe after merging process
        except UnboundLocalError:
            win32api.MessageBox(None, "You selected wrong data type. Please select again", "Warning")
        """ else:
            #print("Successfully merged.")
            win32api.MessageBox(None, "Successfully merged.", "") """
