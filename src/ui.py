from tkinter import filedialog
import os

def fileSelector():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a Xlsx file")
    print("Selected file:", filename)
    return filename

if __name__ == '__main__':
    fileSelector()