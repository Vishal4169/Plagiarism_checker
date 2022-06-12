import os                                                                #for operating files
from numpy import vectorize                                                 #operated multidimentional comparable array
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
from pdftotext import pdftotxt
from browse import search_for_file_path

sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]       #files to be compared
sample_contents = [open(File).read() for File in sample_files]              #file contents to be compared
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()    #transforms text to array
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])             #finds the similarities using consine formula
vectors = vectorize(sample_contents)                                        #holds the sample content vectors 
s_vectors = list(zip(sample_files, vectors))                                #pairs each sample file with its vectors
def check_plagiarism():
    results = set()                                                         #an empty set of results
    global s_vectors                                                     
    for sample_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((sample_a, text_vector_a))        
        del new_vectors[current_index]
        for sample_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]      #similarity score assigned
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], str(round(sim_score*100,2))+" % similar"
            results.add(score)                                              #appending the score to results
    return results
for data in check_plagiarism():
    print(data)   