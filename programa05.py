"""
Nombre:      Emiliano Rivas Rua
Matricula:   1723110398
Grupo:       TI 21
Fecha:       18 de Enero de 2024
Descripción: Programa que crea una clase y un objeto que imprime ambos metodos utilizados.
"""
class Alumnos:                                   # Definición de la clase Alumnos
  matricula = None                              # Atributo matricula
  nombre = None                                 # Atributo nombre

  def __init__(self, matricula, nombre):        # Constructor de la clase Alumnos
      self.matricula = matricula                # Asignación del valor del parámetro matricula al atributo matricula
      self.nombre = nombre                      # Asignación del valor del parámetro nombres al atributo nombres
      print("Objeto Alumno.")                   # Imprime el texto "Objeto Alumno"

  def estudiar(self):                           # Método estudiar
      print(f"{self.nombre} estudia.")         # Imprime el texto "nombre estudia"

  def sumar(self, numero1, numero2):            # Método sumar
      suma = numero1 + numero2                  # Asignación de la suma de los parámetros numero1 y numero2 al atributo suma
      print(f"{numero1} + {numero2} = {suma}.") # Imprime el texto "numero1 + numero2 = suma  

dejah = Alumnos(1111, "Dejah")                   # Creación del objeto de la clase Alumnos
dejah.estudiar()                                 # Llamada al método estudiar
dejah.sumar(10, 5)                      