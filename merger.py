from PyPDF2 import PdfWriter
import os

#creating a instance of the pdfwriter object
merger = PdfWriter()

#getting the current path
current_path = os.getcwd()

#for each pdf in the folder of files, append it to the merger
for file in os.listdir("current_path/files_to_merge"):
    merger.append(file)

#writing the output to a separate pdf file
#note that the wb type will create a file if it doesn't already exist
output_pdf = open("merged_pdf.pdf", "wb")
merger.write(output_pdf)

#closing the files at the end
merger.close()
output_pdf.close()