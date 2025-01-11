# PDF Merger

## Description
This is a PDF merger that will merge the PDFs that you give to the program. No saved files and no security leaks.

---

## Installation

Use these steps to download and install the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <this-repository-url>
   cd <this-repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run GUI Program**:
   ```bash
   python merger.py
   ```

   You can select files manually or you can drag and drop them into the window, then click merge and save the file where you prefer.

Alternatively, if you would rather not interact with GUI and use the terminal, After installing the program and its requirements follow the steps below: 
   
1. **Create the merging folder**:
   
   Add the PDF files that you wish to merge into a folder named "files_to_merge",
   note that it will merge in the order of the files in the folder.
   
   
2. **Run the Application for Terminal**:
   ```bash
   python mergerCL.py
   ```
