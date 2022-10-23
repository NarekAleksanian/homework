# a program that asks the user to enter a character, checks and prints whether the character is a consonant or a vowel.

ch = input("print character: ")

vowel = ['a', 'e', 'i', 'o', 'u']
if ch.lower() in vowel:
	print("the char is vowel")
else:
	print("the cahr is consonant")
