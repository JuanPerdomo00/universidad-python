#!/usr/bin/python3


def main():
    n = int(input("Ingrese un numero: "))
    if n % 2 == 0:
        print(f"{n} es un numero par")
    else:
        print(f"{n} no es un numero par")
        option = input("Quiere intentarlo de nuevo[Y/n]: ")
        if option == "" or option == "Y" or option == "y":
            main()
        else:
            print("Bye")


if __name__ == "__main__":
    main()
