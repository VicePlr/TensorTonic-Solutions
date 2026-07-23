def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopwords = set(stopwords)
    return [token for token in tokens if token not in stopwords]
    pass