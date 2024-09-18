print("Programacion POO")

class Perro:

    def morder(self):
        print("El perro me mordió")
    def Datos_perro(self, nombre,edad):
        print(f"Nombre: {nombre}, edad: {edad}")

pitbul = Perro()

pitbul.Datos_perro("Doggy", 4)
pitbul.morder()