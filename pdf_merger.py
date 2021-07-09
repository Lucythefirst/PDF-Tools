#merge two pdf documents together

import PyPDF2
import sys

inputs = sys.argv[1:]   # this will take all the arguments passed (except arg 0) and store them in a list

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_merger(inputs)


