"""
Nombre:      Emiliano Rivas Rua
Matricula:   1723110398
Grupo:       TI 21
Fecha:       18 de Enero de 2024
Descripción: Programa que crea una clase y un objeto que imprime ambos metodos utilizados.
"""
class Alumnos:                               # Clase Alumnos
  matricula: None                            # Atributo matricula
  nombre: None                               # Atributo nombre
  def __init__(Self, matricula, nombre):       # Constructor de la clase Alumnos
    self.matricula=matricula                 # Asigna el valor de matricula
    self.nombre=nombre                     # Asigna el valor de nombres
    print("Objeto Alumno")                   # Imprime el mensaje "Objeto Alumno"
  def estudiar(self):                        # Método estudiar
    print(f"{self.nombre} estudia")          # Imprime el mensaje "nombre estudia"