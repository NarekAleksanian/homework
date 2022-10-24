"""Write a program that gets a string from the user containing a potential telephone number.
 The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise.
  A phone number is considered valid as long as it is written in the form abc-def-hijk or 1-abc-def-hijk.
   The dashes must be included, the phone number should contain only numbers and dashes,
    and the number of digits in each group must be correct. Test your program with the output shown below."""

phone_number = input("Enter a phone number: ")

if '-' not in phone_number:
    print('Invalid')
    exit()


for i in phone_number:
    if i.isalpha():
        print('Invalid')
        exit()

ch = '-'
i = 0
count = phone_number.count(ch)

if phone_number[0] == ch or phone_number[-1] == ch:
    print('Invalid')
    exit()


if 2 > phone_number.count(ch) > 3:
    print('Invalid')
    exit()


while i < len(phone_number) and count > 0:
    if phone_number[i].isdigit() and i == 0:
        i += 1
        continue
    elif phone_number[i] == '-':
        i += 4
        count -= 1
        continue
print("Valid")
