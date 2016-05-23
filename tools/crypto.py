
def rand_string(size=6):
	import string, random
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(size))
	import os
	return os.urandom(size)

def caesar(plaintext, shift):
	import string
	alphabet = string.ascii_lowercase
	shifted_alphabet = alphabet[shift:] + alphabet[:shift]
	table = string.maketrans(alphabet, shifted_alphabet)
	return plaintext.translate(table)