import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    documents = [str.lower(doc) for doc in documents]
    vocabs = list(set([word for doc in documents for word in doc.split()]))
    vocabs.sort()
    print(vocabs)
    N_doc = len(documents)
    N_vocabs = len(vocabs)
    tfidf_matrix = np.full(shape=(N_doc, N_vocabs), dtype=float, fill_value=0)
    def TF(term, doc):
        term_count = sum(1 for token in doc.split() if token == term)
        total_terms = len(doc.split())
        return term_count/total_terms
    def IDF(term, documents):
        N_docs = len(documents)
        DF_term = sum([1 for doc in documents if term in doc.split()])
        return np.log(N_docs/DF_term)
        
    for j_vocab in range(len(vocabs)):
        for i_doc in range(len(documents)):
            term = vocabs[j_vocab]
            doc = documents[i_doc]
            tfidf_matrix[i_doc][j_vocab] = TF(term, doc) * IDF(term, documents)
    for row in tfidf_matrix:
        print(row)
    return (tfidf_matrix, vocabs)
    pass