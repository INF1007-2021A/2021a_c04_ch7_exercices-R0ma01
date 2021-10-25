#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(indice):
	f_0, f_1, temp = 0,1,0
	if indice <=1 :
		if indice == 0 :
			return f_0
		else:
			return f_1
	else:
		for i in range(1,indice):
			temp = f_0 +f_1
			f_0  = f_1
			f_1 = temp

		return f_1
def get_fibonacci_recursive(indice):
	pass

def get_fibonacci_sequence(taille):
	matrice = []
	for i in range(taille):
		matrice.append(get_fibonacci_number(i))

	return matrice

def get_sorted_dict_by_decimals(TODO):
	pass

get_sorted_dict_by_decimals = lambda dic: dict(sorted(dic.items(), key = lambda a: int( str(a[1]).split('.')[1] ) ))

def fibonacci_numbers(length):
	i = 0
	while length> i :
		yield get_fibonacci_number(i)
		i+=1

def build_recursive_sequence_generator(TODO):
	pass


if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
