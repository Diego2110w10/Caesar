def encode (message, shift):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    partialStart=''
    partialEnd=''
    shiftedAlphabet=''

    if shift == 0:
        shiftedAlphabet = alphabet
    elif shift > 0 and shift < 26:
        partialStart = alphabet[:shift]
        partialEnd = alphabet[shift:]
        shiftedAlphabet = partialStart + partialEnd

        print(shiftedAlphabet)
    
    return message
