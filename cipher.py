<<<<<<< HEAD
<<<<<<< HEAD
def encode(message, s, n):
    
=======
=======
>>>>>>> origin/master
'''cipher.py

	Martin Hoffman
	Sam Nozaki

	Created 1/22/2015
	Python Version: 3.5

	Allows the user to encode text with a password via a Double Caesar 
	(Vignere) cipher.

	CS111, Winter 2016
'''

def encode(message, s, n):
	'''Encodes text via a Double Caesar cipher.

<<<<<<< HEAD
def decode(ciphertext, s, n):
<<<<<<< HEAD
    password = s
>>>>>>> origin/master
=======
    password = s
>>>>>>> origin/master
=======
	Parameters:
	message - Plain text to be encoded
	s		- Password or key
	n 		- Number of times to use the key before the message is used

	Returns: The string cipherText.
	'''
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	
	cleanMessage = ''
	# Removes non-alpha characters from message
	for char in message:
		if alpha.find(char) != -1:
			cleanMessage += char

	# Calculates how many characters of the message to use after the key
	charsAfterKey = len(cleanMessage) - len(s) * n
	longKey = s * n + cleanMessage[:charsAfterKey]
	
	i = 0
	cipherText = ''
	# Shifts each character based on the index of the pertinent charcter in the key
	for char in cleanMessage:
		char = alpha[(alpha.find(longKey[i]) + alpha.find(char)) % 26]
		cipherText += char
		i += 1

	return cipherText

def decode(cipherText, s, n):
	s = password
>>>>>>> origin/master
