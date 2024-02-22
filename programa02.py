"""
Nombre:      Emiliano Rivas Rua
Matricula:   1723110398
Grupo:       TI 21
Fecha:       18 de Enero de 2024
Descripción: Imprime el nombre del alumno
"""
class Alumno:                                            # Crea la clase Alumno
  matricula = None                                       # Crea la variable matricula
  nombre = None                                      # Crea la variable nombre
 
  def __init__(self, matricula, nombre):                # Crea el metodo constructor
      print("Constructor de la clase Alumno")           # Imprime el mensaje
      self.matricula = matricula                        # Asigna el valor de matricula
      self.nombre = nombre                              # Asigna el valor de nombre

objectA = Alumno(111111,"Luis")                         # Crea el objeto objectA
print(objectA.nombre)                                   # Imprime el nombre