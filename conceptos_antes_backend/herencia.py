# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        print(f"{self.nombre} está comiendo.")
        
    def emitir_sonido(self,sonido):
        print(sonido)

# Clase derivada (subclase)
class Perro(Animal):
    def __init__(self, nombre, raza):
        self.raza = raza
        self.nombre = nombre
        
    def jugar_palo():
        pass
        
        
# Crear una instancia de la clase Perro
mi_perro = Perro("Rex", "Pastor Alemán")
mi_perro.emitir_sonido("WOOF")

# Clase derivada (subclase)
class Mascota(Perro):
    def __init__(self, nombre, raza):
        self.raza = raza
        self.nombre = nombre
    
    def jugar(self):
        print(f"WOF WOF")
        

# Clase derivada (subclase)
class Gato(Animal):
    def __init__(self, nombre, raza):
        self.raza = raza
        self.nombre = nombre


# Crear una instancia de la clase Perro
mi_perro = Perro("Rex", "Pastor Alemán")
mi_perro.comer()  # Llama al método comer()


"""
Actividad:

Crea una clase Mascota que herede de Perro


"""

class Mascota(Perro):
    def __init__(self, nombre, raza, dueno):
        super().__init__(nombre, raza)
        self.dueno = dueno
    
    def __str__(self):
        return f"Mascota de {self.dueno}"
        
mascota1 = Mascota("toby", "pincher", "Jakepys")

print(mascota1)
print(Mascota)