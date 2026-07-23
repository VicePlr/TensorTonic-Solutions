from collections import defaultdict
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    dicta = defaultdict(int)
    for sentence in sentences:
        print(sentence)
        for word in sentence:
            dicta[word] += 1
    return dicta
    pass