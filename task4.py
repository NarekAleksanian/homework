# a program that asks the user to enter a number and prints the sum of its digits on the screen.

nums = input("please enter the number: ")

ls = list(nums)

sums = 0

for i in ls:
	sums += int(i)

print(sums)

