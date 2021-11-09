def cipher(text, shift, encrypt=True):
    """
    Enciphers a text string with a given shift number.
    Parameters
    ----------
    text : str
    shift : int
    encrypt : bool
    Returns
    -------
    new_text
      The new enciphered string.
    Examples
    --------
    >>> from cipher_wn2188 import cipher_wn2188
    >>> text = "Hello"
    >>> shift = 1
    >>> cipher_wn2188.cipher(text, shift)
    "Ifmmp"
    
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
