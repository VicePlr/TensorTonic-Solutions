import numpy as np
from collections import defaultdict
def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    vocab_index = defaultdict()
    for i, v in enumerate(vocab):
        vocab_index[v] = i
    vocab = set(vocab)
    bags = np.zeros(shape=len(vocab), dtype=int)
    for token in tokens:
        if token not in vocab:
            continue
        bags[vocab_index[token]] += 1
    return bags
    pass