#!/usr/bin/python3

numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep="-")


def add(a, b, c):
    print(f"Result: {a+b+c}")


add(*numeros)

my_list = [1, 2, 3, 4, 5, 6]
a, *b, c, d = my_list
print(a, b, c, d)


list_one = [1, 2, 4, 8, 16]
list_two = [32, 64, 128, 255]
join_list = [list_one, list_two]
print(join_list)
join_list = [*list_one, *list_two]
print(join_list)


dict_one = {"A": 1, "B":2, "C":3, "D":4}
dict_two = {"E":5, "F":6}
join_dict = {**dict_one, **dict_two}
print(join_dict)

list_char = [*"Jakepys"]
print(list_char)
print(*list_char, sep="")
print(*list_char, sep="/")
