
def fibonacci(x): 
	if not isinstance(x, int):
		return None  # Only accept integers

	a, b = 0, 1
	for i in range(x):
		a, b = b, a + b
	return a

if __name__ == '__main__':
	print map(fibonacci, range(20))