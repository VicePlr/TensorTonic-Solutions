import math
from collections import Counter, defaultdict
import numpy as np

def bm25_score(query_tokens: list[str], docs: list[list[str]], k1: float = 1.2, b: float = 0.75) -> np.ndarray:
    """
    Returns a NumPy array with one score per document.
    """
    N = len(docs)
    
    D_length = np.asarray([len(doc) for doc in docs])
    
    avgdl = np.mean(D_length)
    
    tf_counters = [Counter(doc) for doc in docs]
    def tf(term, Di):
        return tf_counters[Di][term]

    vocab = set([token for doc in docs for token in doc])
    df_counters = defaultdict(int)
    for token in vocab:
        for doc in tf_counters:
            df_counters[token] += (doc[token] > 0)
            
    def df(term):
        return df_counters[term]

    def idf(term):
        return math.log((N - df(term) + 0.5) / (df(term) + 0.5) + 1)

    def term_score(Di, term):
        return idf(term) * (tf(term, Di) * (k1 + 1) / (tf(term, Di) + k1 * (1 - b + b * D_length[Di] / avgdl)))

    def score(Di, query):
        return sum([term_score(Di, term) for term in query])

    scores = np.zeros(shape=(N))

    for i in range(N):
        scores[i] = score(i, query_tokens)

    return np.asarray(scores)
    pass