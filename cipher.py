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

    longKey = getLongKey(cleanMessage, s, n)
    
    i = 0
    cipherText = ''
    # Shifts each character based on the index of the pertinent character in the key
    for char in cleanMessage:
        cipherText += alpha[(alpha.find(char) + alpha.find(longKey[i])) % 26]
        i += 1
        
    return cipherText

def decode(cipherText, s, n):
    '''
    Decodes text that has ben encoded with a double Caesar cipher.
    
    Parameters:
    cipherText - Encoded text to be decoded
    s          - Password or key string, must be the longKey
    n          - Number of times to use the key before the message is used
    
    Returns: the string message 
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    longKey = s

    i = 0
    message = ''
    for char in cipherText:
        message += alpha[alpha.find(char) - (alpha.find(longKey[i])) % 26]
        i += 1

    return message

def getLongKey(cleanMessage, s, n):
    '''
    Calculates how many characters of the message to use after the key

    Parameters:
    cleanMessage - Plain text, only alpha characters
    s            - Password or key string
    n            - Number of times to use the key before the message is used

    Returns: The long version of the key with message characters included.
    '''
    charsAfterKey = len(cleanMessage) - len(s) * n
    if charsAfterKey > 0:
        longKey = s * n + cleanMessage[:charsAfterKey]
    else:
        longKey = ''
        for i in range(len(cleanMessage)):
            longKey += s[i % len(s)]

    print('Your longKey is:', longKey)
    print('Keep it secret! Keep it safe!')
    return longKey

def main():
    operation = input('Would you like to encode or decode? ')

    while True:
        if operation.lower() == 'encode':
            message = input('Enter text to encode: ')
            s = input('Enter a key: ')
            n = input('Enter times to repeat the key: ')
            encode(message, s, n)
            break
        elif operation.lower() == 'decode':
            message = input('Enter the encoded text: ')
            s = input('Enter your longKey: ')
            decode(message, s, n = 1)
            break
        else:
            'Please type either "Encode" or "Decode".'

if __name__ == '__main__':
    main()