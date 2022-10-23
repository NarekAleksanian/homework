# Հայտարարեք char տիպի զանգված և սկզբնարժեքավորեք այն “CheeseBurger” արտահայտությամբ:

ch = "CheseBurger"

def a(tmp):
	tmp_ch = tmp[0]
	tmp_bin = bytearray(tmp_ch.encode())
	for i in tmp:
		new_bin = bytearray(i.encode())
		if new_bin[0] <= tmp_bin[0]:
			tmp_ch = i
	return tmp_ch


print(a(ch))


def b(tmp):
	tmp_ch = tmp[0]
	tmp_bin = bytearray(tmp_ch.encode())
	for i in tmp:
		new_bin = bytearray(i.encode())
		if new_bin[0] >= tmp_bin[0]:
			tmp_ch = i
	return tmp_ch

print(b(ch))

def c(tmp):
	vowel = ['a', 'e', 'i', 'o', 'u', 'y']
	count = 0
	for i in tmp:
		if i in vowel:
			count += 1
	return count

print(c(ch))

def d(tmp):
	return tmp[::-1]

print(d(ch))

def e(tmp):
	ch = tmp[::-1]
	return ch

print(e(ch))

def f(tmp):
	ch = tmp.lower()
	return ch

print(f(ch))
