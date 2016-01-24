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
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	charsAfterKey = len(message) - len(s) * n
	key = s * n + message[:charsAfterKey]
	
	i = 0
	cipherText = ''
	for char in message:
		print(char)
		char = alpha[(alpha.find(key[i]) + alpha.find(char)) % 26]
		print(char)
		i += 1
		cipherText += char

	return cipherText

def decode(cipherText, s, n):
	s = password