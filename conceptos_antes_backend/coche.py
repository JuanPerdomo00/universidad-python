
class Coche:
    def __init__(self, marca, modelo, color, dueno):
        self.marca = marca  
        self.modelo = modelo
        self.color = color
        self.dueno = dueno
        
    def conducir(self):
        print(f"Conduciendo el coche {self.marca} {self.modelo} de color {self.color}.")
        
    def hacer_mantenimiento(self):
        if self.marca == "Toyota":
            print("El mantenimiento es cada 5 años")
        else:
            print("El mantenimiento es cada 3 años")

    def vender_auto(self,dueno):
        self.dueno = dueno
        print("Auto vendido")
        
mi_coche = Coche("Toyota", "Corolla", "Rojo", "Angie")

tu_coche = Coche("Chevrolet", "Onix", "Negro","Juan")

mi_coche.conducir()

mi_coche.hacer_mantenimiento()

mi_coche.vender_auto("Sofia")

print(mi_coche.dueno)

"""
Actividad:

Crea un metodo vender_auto()

El coche debe tener atributo dueño, precio
"""