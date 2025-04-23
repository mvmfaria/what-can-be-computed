def is_increasing(number):
	amount = 0
	counter = 1
	last_number = 9
	while amount < number:
		remainder = number % (10 * counter)
		current = remainder // counter
		amount += (current * counter)
		counter *= 10
		if (current > last_number):
			return False
		last_number = current
	return True
		
def is_decreasing(number):
	amount = 0
	counter = 1
	last_number = -1
	while amount < number:
		remainder = number % (10 * counter)
		current = remainder // counter
		amount += (current * counter)
		counter *= 10
		if (current < last_number):
			return False
		last_number = current
	return True

def is_bouncy(number):
	if (is_increasing(number)):
		return False
	elif (is_decreasing(number)):
		return False
	else:
		return True

def prop_of_bouncy_numbers(n):
	amount = 0
	for i in range(1, n+1):
		if (is_bouncy(i)):
			amount += 1
	print(amount / n)
	return amount / n

def find_least_bouncy(prop):
	number = 1586990
	while prop_of_bouncy_numbers(number) < prop:
		number += 1
		print(number)
	print(number)

find_least_bouncy(0.99)
#Resposta: 1587000