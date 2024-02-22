"""
Nombre:      Emiliano Rivas Rua
Matricula:   1723110398
Grupo:       TI 21
Fecha:       18 de Enero de 2024
Descripción: Imprime muchos datos acerca de los alumnos de la clase
"""
class Alumnos:                                              # Clase Alumnos
  matricula:None                                            # Atributo matricula
  nombre:None                                               # Atributo nombre
  def __init__(self, matricula, nombre):                      # Constructor
      self.matricula=matricula                              # Asigna matricula
      self.nombre = nombre                                  # Asigna nombre
      print("Objeto Alumnos")                               # Imprime objeto Alumnos
objectAlumnos=Alumnos(12312, "Luis")                        # Crea objeto Alumnos
print(objectAlumnos.nombre)                                 # Imprime nombre 
print(objectAlumnos.matricula )                             # Imprime matricula
objectAlumnos=Alumnos(nombre="Guayabo", matricula=2020)     # Crea el objeto Alumnos
print(objectAlumnos.nombre)                                 # Imprime nombre
print(objectAlumnos.matricula)                              # Imprime matricula