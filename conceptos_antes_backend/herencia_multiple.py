class A:
    def saludar(self):
        print("Hola desde la clase A")

class B:
    def saludar(self):
        print("Hola desde la clase B")

class C(A, B):
    pass

c = C()
c.saludar()  # ¿Qué saludar() se ejecutará?


C.__mro__ #método de resolucion de orden 

print(C.__mro__)

