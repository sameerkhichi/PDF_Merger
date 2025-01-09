from PyPDF2 import PdfWriter
import os

#creating a instance of the pdfwriter object
merger = PdfWriter()

#storing the current path
original_path = os.getcwd()

#changing directory to the folder with the pdf files
os.chdir('files_to_merge')

#storing the new directory
current_path = os.getcwd()

#for each pdf in the folder of files, append it to the merger
for file in os.listdir(current_path):
    merger.append(file)

#switching the working path back to the original one
os.chdir(original_path)

#writing the output to a separate pdf file
#note that the wb type will create a file if it doesn't already exist
output_pdf = open("merged_pdf.pdf", "wb")
merger.write(output_pdf)

#closing the files at the end
merger.close()
output_pdf.close()