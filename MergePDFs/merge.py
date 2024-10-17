"""
Merging PDF files
"""

import PyPDF2 as pdf

#Initialise instance of PdfFileMerger() class
merge = pdf.PdfMerger()

#List of PDF files
list_pdfs = ['paper1.pdf', 'paper2.pdf']

for file in list_pdfs:
	merge.append(file)

merge.write("merged.pdf")