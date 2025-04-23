def reverse_string(string):
	list_of_chars = list(string)
	stack = []
	
	for char in list_of_chars:
		stack.append(char)
	
	reversed_string = ''

	for i in range(len(stack)):
		reversed_string += stack.pop()
		
	return reversed_string