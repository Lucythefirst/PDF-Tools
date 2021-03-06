import PyPDF2

with open('dummy.pdf', 'rb') as file:  # read the file
    # 'rb' is read binary, for pdf we append 'b' to it.
    # so it converts the file to binary and PyPDF2 works with binary files.
    reader = PyPDF2.PdfFileReader(file)
    print(file)
    print(reader)
    print(reader.numPages)
    print(reader.getPage(0))

    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page) # now save the rotated page as a new file so it isn't only in memory
    with open('rotated.pdf', 'wb') as new_file:
        writer.write(new_file)

