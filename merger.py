#this merger uses tkinter to implement a GUi
import tkinter as tk
from tkinter import filedialog, messagebox, ttk #ttk is for the progress bar
from tkinterdnd2 import TkinterDnD, DND_FILES #to support drag and dropping files
import ctypes
import os
from PyPDF2 import PdfWriter

#adjusting the quality of the window for higher resolution displays
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#making the main window
root = TkinterDnD.Tk()
root.title("PDF Merger")
root.geometry('840x720')

#This is an array to hold the selected files
files_to_merge = []

#creates a file box to display the selected files
file_list = tk.Listbox(root, width=50, height=10)
file_list.pack(pady=10)

#this is for the progress bar, initially set to 0%
progress_label = tk.Label(root, text="Progress:")
progress_label.pack(pady=10)
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", maximum=100)
progress.pack(pady=10)

def clear_file_list():

    #clears the box for the list
    file_list.delete(0, tk.END)


#this is a function to display the user selected files
def update_file_list():

    #clearing the list before adding all the files back to it
    clear_file_list()

    #inserts each file selected
    for file in files_to_merge:
        file_name = os.path.basename(file)
        file_list.insert(tk.END, file_name)

def select_files():
    
    #using the global variable, asking user to select their files they want to merge
    global files_to_merge
    files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])

    if files:
        for file in files:
            #Avoid duplicate files and append to the list with the new file
            if file not in files_to_merge:
                files_to_merge.append(file)

        #making sure the box with the pdfs stay updated
        update_file_list()

def merge_pdfs():

    #incase there are no files selected, display error message
    if not files_to_merge:
        messagebox.showerror("There are no files selected!")
        return
    
    #asking the user where to save the final file
    #this uses methods from the tkinter class
    merged_pdf_location = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    #if the user cancels the save process
    if not merged_pdf_location:
        return
    
    #using logic from command line merger
    merger = PdfWriter()

    #setting the progress bar to 0 and updating it
    progress["value"] = 0
    root.update()

    for i, file in enumerate(files_to_merge):
        #converting the relative path to an absolute one
        file = os.path.abspath(file)
        merger.append(file)

        #update the progress bar with the value of the programs progress
        progress["value"] = (i+1) / len(files_to_merge) * 100

        #refresh the progress bar
        root.update_idletasks()

    #create a file using wb and open function as a simple name
    output_pdf = open(merged_pdf_location, "wb")
    #write to the merger with the contents of the file
    merger.write(output_pdf)
    merger.close()
    output_pdf.close()

    #success message
    messagebox.showinfo("Saved", f"PDFs merged and saved to:\n{merged_pdf_location}")


#Handle drag and drop files
def on_drop(event):
    files = event.data.split()
    for file in files:

        #cleaning file path
        file = file.strip()
        file = file.replace("file:///", "")

        #this is to avoid duplicate files
        if file not in files_to_merge:
            files_to_merge.append(file)

    #updating the box with the pdf's after each call
    update_file_list()

#binding the event of dragging and dropping to the window
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)


#this is making the button to select the files
select_button = tk.Button(root, text = "Select PDFs", command = select_files)
select_button.pack(pady=10)

#making a button to be able to merge the files
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=10)

#making a button to be able to merge the files
clear_button = tk.Button(root, text="Clear List", command=clear_file_list)
clear_button.pack(pady=10)

#running the main loop
root.mainloop()