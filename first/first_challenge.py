def print_sequence():
	for number in range(1,101):

		message = number
		if number % 3 == 0 and number % 5 == 0:
			message = "FooBar"
		elif number % 3 == 0:
			message = "Foo"
		elif number % 5 == 0:
			message = "Bar"

		print message


if __name__ == '__main__':
	print_sequence()
