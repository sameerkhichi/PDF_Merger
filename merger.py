#this merger uses tkinter to implement a GUi
import tkinter as tk
from tkinter import filedialog

#making the main window
root = tk.Tk()
root.title("PDF Merger")
root.geometry('800x600')

#This is an array to hold the selected files
files_to_merge = []

#creates a file box to display the selected files
file_list = tk.Listbox(root, width=50, height=10)
file_list.pack(pady=10)


def select_files():
    
    #using the global variable, asking user to select their files they want to merge
    global files_to_merge
    files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])

    if files:
        files_to_merge = list(files)
        update_file_list()
    

#this is a function to display the user selected files
def update_file_list():

    #clears the box for the list
    file_list.delete(0, tk.END)

    #inserts each file selected
    for file in files_to_merge:
        file_list.insert(tk.END, file)


#this is making the button to select the files
select_button = tk.Button(root, text = "Select PDFs", command = select_files)
select_button.pack(pady=10)

#running the main loop
root.mainloop()