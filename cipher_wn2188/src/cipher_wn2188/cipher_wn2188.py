def cipher(text, shift, encrypt=True):
    """
    Takes input of a text string and a shift number, outputs the encrypted string by shifting in alphabet the corresponding number.

    Parameters
    ----------
    text : string
        The input text.
    shift : int
        The number by which the encription will use to shift in alphabet.

    Returns
    -------
    new_text
      The encrypted text.

    Examples
    --------
    >>> from cipher_wn2188 import cipher_wn2188
    >>> text = 'Hello!'
    >>> shift = 1
    >>> cipher_wn2188.cipher(text,shift)
    'Ifmmp!'

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