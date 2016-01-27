'''cipher.py

    Martin Hoffman
    Sam Nozaki

    Created 1/22/2015
    Python Version: 3.5

    Allows the user to encode text with a password via a double Caesar (Vignere) cipher.

    CS111, Winter 2016
'''

def encode(message, s, n):
    '''
    Encodes text via a double Caesar cipher.

    Parameters:
    message - Plain text to be encoded
    s       - Password or key string
    n       - Number of times to use the key before the message is used

    Returns: the string cipherText.
    '''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    
    cleanMessage = ''
    # Removes non-alpha characters from message
    for char in message:
        if char in alpha:
            cleanMessage += char

    # Calculates how many characters of the message to use after the key
    print(cleanMessage)
    charsAfterKey = len(cleanMessage) - len(s) * n
    longKey = s * n + cleanMessage[:charsAfterKey]
    print(longKey)
    i = 0
    cipherText = ''
    # Shifts each character based on the index of the pertinent charcter in the key
    for char in cleanMessage:
        cipherText += alpha[(alpha.find(longKey[i]) + alpha.find(char)) % 26]
        i += 1
        
    return cipherText

def decode(cipherText, s, n):
    '''
    Decodes text that has ben encoded with a double Caesar cipher.
    
    Parameters:
    cipherText - Encoded text to be decoded
    s          - Password or key string
    n          - Number of times to use the key before the message is used
    
    Returns: the string message 
    '''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    message = ''
    
    cipherText = cipherText.lower()
    clean = ''
    # Removes all non-alpha characters from cipherText
    for ch in cipherText:
        if ch in alpha:
            clean += ch
            
    # longKey is a string that represents the complete key for the message
    longKey = s * n + clean[:len(clean) - len(s) * n]
    i = 0
    for ch in clean:
        message += alpha[(alpha.find(ch) - alpha.find(longKey[i])) % 26]
        # only works while the key is still s, when the loop reaches the part of longKey where it changes to the original message being the key, it stops working
        i += 1
       
    return message

def encodeSpace(message, s, n):
    '''
    Encodes text with spaces and new line characters via a double Caesar cipher.

    Parameters:
    message - Plain text to be encoded
    s       - Password or key string
    n       - Number of times to use the key before the message is used

    Returns: the string cipherText.
    '''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz \n'
    message = message.lower()

    # Calculates how many characters of the message to use after the key
    charsAfterKey = len(message) - len(s) * n
    longKey = s * n + message[:charsAfterKey]
    i = 0
    cipherText = ''
    # Shifts each character based on the index of the pertinent charcter in the key
    for char in message:
        cipherText += alpha[(alpha.find(longKey[i]) + alpha.find(char)) % 28]
        i += 1
        
    return cipherText