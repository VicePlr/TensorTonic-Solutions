import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    N = len(seqs)
    if not max_len:
        max_len = max(len(seq) for seq in seqs)
    pad_sq = np.full(shape=(N, max_len), dtype=int, fill_value=pad_value)
    for i, seq in enumerate(seqs):
        if len(seq) > max_len:
            pad_sq[i] = seq[:max_len]
        else:
            pad_sq[i][:len(seq)] = seq[:]
    return pad_sq
    pass