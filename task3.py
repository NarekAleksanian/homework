# a program that asks the user to enter n number and prints the n-th Fibonacci number.

num = int(input("enter the number: "))

def fib(n):
	if n <= 1:
		return n
	else:
		return (fib(n-1) + fib(n-2))

print(fib(num))
