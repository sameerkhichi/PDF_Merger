from PyPDF2 import PdfWriter

#creating a instance of the pdfwriter object
merger = PdfWriter()

#array to hold the files
files = []

#gets the file name and path from the user
while True:
    print("Enter the name of the file with its path enter 'done' to exit")
    filename = input("Name: ")

    if (filename == "done"):
        break
    
    else:
        files.append(filename)


#for each pdf in the array of files, append it to the merger
for pdf in files:
    merger.append(pdf)

#writing the output to a seperate pdf file
#note that the wb type will create a file if it doesnt already exist
output_pdf = open("merged_pdf.pdf", "wb")
merger.write(output_pdf)

#closing the files at the end
merger.close()
output_pdf.close()
