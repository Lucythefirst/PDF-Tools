# a program that watermarks pdfs by merging: a pdf with a watermark, onto all the pages of other pdfs

# the first method uses inputs from the terminal
# the first input is the pdf with the watermark
# the following inputs are the pdfs that you want to be watermarked
import PyPDF2
import sys

watermark_str = sys.argv[1]  # creates a string object from the argument input
to_mark_str = sys.argv[2:]
watermark = PyPDF2.PdfFileReader(open(watermark_str, 'rb'))  # open the string object so it is classed as a pdf so you can use the PyPDF2 modules
output = PyPDF2.PdfFileWriter()

for pdf in to_mark_str:
    pdfx = PyPDF2.PdfFileReader(open(pdf, 'rb'))
    for i in range(pdfx.getNumPages()):
        page = pdfx.getPage(i)
        page.mergePage(watermark.getPage(0))  # get the first page of the watermark file
        output.addPage(page)

with open('watermarked.pdf', 'wb') as file:
    output.write(file)


# Or this second method gives a pdf in code and will run with the console:

pdf_to_mark = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark2 = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output2 = PyPDF2.PdfFileWriter()

for i in range(pdf_to_mark.getNumPages()):
    page2 = pdf_to_mark.getPage(i)
    page2.mergePage(watermark.getPage(0))
    output2.addPage(page2)

    with open('watermarked_output.pdf', 'wb') as file2:
        output2.write(file2)
