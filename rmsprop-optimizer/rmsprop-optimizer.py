import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    w = np.asarray(w)
    g = np.asarray(g)
    s = np.asarray(s)
    s = beta * s + (1 - beta) * (g ** 2)
    w = w - lr / (np.sqrt(s + eps)) * g
    return w, s
    pass