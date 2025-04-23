from reverse_string import *

def eh_palindromo(texto):
	original = ''.join(texto.lower().split())
	
	reversed_text = reverse_string(original)
	
	if (reversed_text == original):
		print('yes')
	else:
		print('no')