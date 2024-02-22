"""
Nombre:      Emiliano Rivas Rua
Matricula:   1723110398
Grupo:       TI 21
Fecha:       18 de Enero de 2024
Descripción: Imprime el Nombre y el Objeto Alumnos
"""
class Alumnos:                             # Define una clase de nombre Alumnos
  matricula = None                         # Declara una variable de nombre matricula
  nombre = None                            # Declara una variable de nombre nombre

  def __init__(self, matricula, nombre):   # Define el método init
      self.matricula = matricula           # Asigna un valor a matricula
      self.nombre = nombre                 # Asigna un valor a nombre

print("Objeto Alumnos")                    # Imprime Objeto Alumnos
objectA = Alumnos(1123, "Luisa")           # Crea un objeto de la clase Alumnos
print(objectA.nombre)                      # Imprime el valor de nombre y objeto Alumnos