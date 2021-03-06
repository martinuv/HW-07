'''cipher.py

    Martin Hoffman
    Sam Nozaki

    Created 1/22/2015
    Python Version: 3.5

    Allows the user to encode text with a password via a double Caesar (Vignere)
    cipher.

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

    cleanMessage = getCleanMessage(message, alpha)
    longKey = getLongKey(cleanMessage, s, n)

    i = 0
    cipherText = ''

    # Encodes each character based on index of pertinent character in the key
    for char in cleanMessage:
        cipherText += alpha[(alpha.find(char) + alpha.find(longKey[i])) % 26]
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
    i = 0
    message = ''

    # Decodes each character based on index of pertinent character in the key
    for char in cipherText:
        message += alpha[alpha.find(char) - alpha.find(s[i])]
        i += 1
        # Adds decoded characters to key to be used later
        s += alpha[alpha.find(char) - alpha.find(s[i])]

    return message


def encodeSpace(message, s, n):
    '''
    Encodes text via a double Caesar cipher, inlcuding spaces and newlines.

    Parameters:
        message - Plain text to be encoded
        s       - Password or key string
        n       - Number of times to use the key before the message is used

    Returns: the string cipherText.
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz \n'
    message = message.lower()

    cleanMessage = getCleanMessage(message, alpha)
    longKey = getLongKey(cleanMessage, s, n)

    i = 0
    cipherText = ''

    # Encodes each character based on index of pertinent character in the key
    for char in cleanMessage:
        cipherText += alpha[(alpha.find(char) + alpha.find(longKey[i])) % 28]
        i += 1

    return cipherText


def decodeSpace(cipherText, s, n):
    '''
    Decodes text that has ben encoded with a double Caesar cipher, inlcuding 
    spaces and newlines.

    Parameters:
        cipherText - Encoded text to be decoded
        s          - Password or key string
        n          - Number of times to use the key before the message is used

    Returns: the string message 
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz \n'
    i = 0
    message = ''

    # Decodes each character based on index of pertinent character in the key
    for char in cipherText:
        message += alpha[alpha.find(char) - alpha.find(s[i])]
        i += 1
        # Adds decoded characters to key to be used later
        s += alpha[alpha.find(char) - alpha.find(s[i])]
       
    return message


def getCleanMessage(message, alpha):
    '''Removes characters not present in the "alphabet" from message.

    Parameters:
        message - Text to be cleaned
        alpha   - Alphabet to base cleaning off of

    Returns: The cleaned message.
    '''
    cleanMessage = ''

    for char in message:
        if char in alpha:
            cleanMessage += char
            
    return cleanMessage


def getLongKey(cleanMessage, s, n):
    '''Calculates how many characters of the message to use after the key.

    Parameters:
        cleanMessage - Plain text, only alpha characters
        s            - Password or key string
        n            - Number of times to use the key before the message is used

    Returns: The long version of the key with message characters included.
    '''
    charsAfterKey = len(cleanMessage) - len(s) * n

    if charsAfterKey > 0:
        # Sets longKey to the key repeated n times, concatenates requisite
        # number of characters after key repetitions from original message
        longKey = s * n + cleanMessage[:charsAfterKey]
    else:
        longKey = ''
        # Ensures that key repetitions don't excede characters of message
        for i in range(len(cleanMessage)):
            longKey += s[i % len(s)]

    return longKey


def main():
    '''Prompts the user to supply all the information necessary to encode
    or decode text. Prints relevant information to the console.
    '''
    while True:
        spaces = input('Will your message have spaces or newlines? (Y/N) ')
        operation = input('Would you like to encode or decode? ')

        # Checks that the user correctly answered the spaces prompt
        if spaces.lower() == 'y':
            # Checks that the user correctly enter the encode/decode prompt
            if operation.lower() == 'encode':
                # Collects parameters for encodeSpace from user
                message = str(input('Enter text to encode: '))
                s = str(input('Enter a key: '))
                n = int(input('Enter times to repeat the key: '))
                print('Your encoded message is:\n', encodeSpace(message, s, n))
                input('[Enter] to exit...')
                break
            elif operation.lower() == 'decode':
                # Collects parameters for decodeSpace from user
                message = str(input('Enter the encoded text: '))
                s = str(input('Enter your key: '))
                n = int(input('Enter times to repeat the key: '))
                print('Your decoded message is:\n', decodeSpace(message, s, n))
                input('[Enter] to exit...')
                break
            else:
                # Re-prompts the user if input was other than encode or decode
                print('Please type either "Encode" or "Decode".')
        elif spaces.lower() == 'n':
            # Checks that the user correctly enter the encode/decode prompt
            if operation.lower() == 'encode':
                # Collects parameters for encode from user
                message = str(input('Enter text to encode: '))
                s = str(input('Enter a key: '))
                n = int(input('Enter times to repeat the key: '))
                print('Your encoded message is:\n', encode(message, s, n))
                input('[Enter] to exit...')
                break
            elif operation.lower() == 'decode':
                # Collects parameters for decode from user
                message = str(input('Enter the encoded text: '))
                s = str(input('Enter your key: '))
                n = int(input('Enter times to repeat the key: '))
                print('Your decoded message is:\n', decode(message, s, n))
                input('[Enter] to exit...')
                break
            else:
                # Re-prompts the user if input was other than encode or decode
                print('Please type either "Encode" or "Decode".')
        else:
            # Re-prompts the user if input was other than y or n
            print('Please enter either "Y" or "N".')


if __name__ == '__main__':
    main()