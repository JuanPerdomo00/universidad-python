#!/usr/bin/python3


my_list = [1, 2, 3, 4, 5]

# agregar a lista con operador +
my_list += [26]

for i in range(len(my_list)):
    print("i: %d, my_list[%d] = %d" % (i, i, my_list[i]))
