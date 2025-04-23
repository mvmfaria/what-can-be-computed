def count_elements(elements):
	list_of_items = elements.split(', ')
	dict = {}
	for item in list_of_items:
		if not item in dict:
			dict[item] = 1
		else:
			dict[item] += 1
	result = ''
	for elem in dict:
		result += elem+':'+str(dict[elem])+', '
	print(result[:-2])