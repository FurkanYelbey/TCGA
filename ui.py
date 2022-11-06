from inspect import getfile
from MergeTsv import *
import tkinter as tk
from tkinter import Button, filedialog

TCGAUI = tk.Tk()
TCGAUI.geometry('600x600')
TCGAUI.title("TCGA Merge Tool")

sampleSheetPath = ''
outputPath = ''
dataFilesPath = ''
selectedColumn = 0
dataType = 0
mergedFileName = tk.StringVar()

def selectSampleSheetPath():
    global sampleSheetPath
    sampleSheetPath = filedialog.askopenfilename()
    sampleSheetPathBox.delete(0, 'end')
    sampleSheetPathBox.insert('end', sampleSheetPath)

def selectOutputPath():
    global outputPath
    outputPath = filedialog.askdirectory()
    outputPathBox.delete(0, 'end')
    outputPathBox.insert('end', outputPath)

def selectDataFilesPath():
    global dataFilesPath
    dataFilesPath = filedialog.askdirectory()
    dataFilesPathBox.delete(0, 'end')
    dataFilesPathBox.insert('end', dataFilesPath)

def selectDataType(selectedDataType):
    global dataType
    dataType = selectedDataType

def selectColumn(selectedColumnIndex):
    global selectedColumn
    selectedColumn = selectedColumnIndex

def getFileName(*args):
    global mergedFileName
    mergedFileName = mergedFileNameBox.get()

def Merge():
    MergeTsv(dataFilesPath, sampleSheetPath, outputPath, selectedColumn, dataType, mergedFileName.get())

def showStatus(status):
    print(status)
    print(type(status))

label = tk.Label(text='Please select a data type').pack()

dataTypes = ['Transcriptome Profiling', 'Dna Methylation']
dataOption = tk.IntVar(value=0)
for dataonvalue in range(1, 3):
    dataTypeButton = tk.Checkbutton(
        TCGAUI,
        text=dataTypes[dataonvalue-1],
        onvalue=dataonvalue,
        variable=dataOption,
        command=lambda:selectDataType(dataOption.get())
    )
    dataTypeButton.pack()

label = tk.Label(text='Please select a column').pack()

columnOption = tk.IntVar(value=0)
for columnonvalue in range(1, 9):
    columnCheckbutton = tk.Checkbutton(
        TCGAUI,
        text="Column "+str(columnonvalue),
        onvalue=columnonvalue,
        variable=columnOption,
        command=lambda:selectColumn(columnOption.get())
    )
    columnCheckbutton.pack()

#columnselect1 = tk.Checkbutton(TCGAUI, text="")
dataFilesPathBox = tk.Entry(TCGAUI, textvariable=outputPath, width= 60)
dataFilesPathBox.pack()
dataFilesSelectButton = Button(TCGAUI, text="Select data files directory", command = selectDataFilesPath).pack()
#dataFilesSelectButton.grid()

sampleSheetPathBox = tk.Entry(TCGAUI, textvariable=sampleSheetPath, width=60)
sampleSheetPathBox.pack()
sampleSheetSelectButton = Button(TCGAUI, text="Select sample sheet file", command = selectSampleSheetPath).pack()
#sampleSheetSelectButton.grid(row=1, column=2)

outputPathBox = tk.Entry(TCGAUI, textvariable=outputPath, width= 60)
outputPathBox.pack()
outputPathSelectButton = Button(TCGAUI, text="Select output directory", command = selectOutputPath).pack()
#outputPathSelectButton.grid(row=3, column=2)

label = tk.Label(text='Please enter merged file name').pack()
mergedFileNameBox = tk.Entry(TCGAUI, textvariable=mergedFileName, validate="focusout", validatecommand=getFileName, width= 60)
mergedFileNameBox.pack()
#mergedFileName.trace_add('write', getFileName)# reads only first letter

mergeButton = Button(TCGAUI, text="Merge", command=Merge).pack()

TCGAUI.mainloop()