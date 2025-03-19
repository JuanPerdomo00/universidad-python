#
#
#      |       |     |
#     <|>      |     |
#    <<|>>     |     |
#   <<<|>>>    |     |
#  ---------------------
#      A       B     C
# A: Origin
# B: Auxliaty
# C: Destination

# move tomara dos parametros
# o, origen d, destino
def move(o, b):
    print(f"Move disc {o} to {b}")


# move("A", "C")


# Movernos de A, C atravez de B
def move_thoug(o, a, d):
    move(o, a)
    move(a, d)


# move_thoug("A", "B", "C")


def torre_hanoi(n, o, a, d):
    if n == 0:
        pass
    else:
        torre_hanoi(n - 1, o, d, a)
        move(o, d)
        torre_hanoi(n - 1, a, o, d)


torre_hanoi(10, "A", "B", "C")
