def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    if step <= 0:
        step = 1
    chunks = []
    for i in range(0, len(tokens), step):
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)
        if i + chunk_size >= len(tokens):
            break
    return chunks