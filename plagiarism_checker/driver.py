from pdf_similarity import pdf_similarity
from pdftotext import pdftotxt
from similarity import similarity
import webbrowser

input_var = int(input("Press 1 to deal with text files \n"))
if (input_var == 2):
    pdftotxt()
    pdf_similarity()
    filename = r"G:\report.html"
    webbrowser.open_new_tab(filename)
elif (input_var == 1):
    similarity()
    filename = r"G:\report.html"
    webbrowser.open_new_tab(filename)
else:
    print("INVALID")

