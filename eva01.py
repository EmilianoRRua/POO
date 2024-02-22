"""
Programa:eva01.py
Nombre Completo:Emiliano Rivas Rua
Matricula:1723110398
Fecha: 29/01/2024
"""
class Profesor:                        # Denfine la clase profesor
  def __init__(self, id, nombre):      # Define el constructor de la clase profesor
      self.id = id                     # Define el atributo id
      self.nombre = nombre             # Define el atributo nombre
      self.materias = []               # Define el atributo materias como una lista vacia
      print("Clase Profesor")          # Imprime la clase profesor

  def califica(self):                  # Define el metodo califica
      print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre,self.materias[0]))    # Imprime el metodo califica

  def pasa_asistencia(self):                                 # Define el metodo pasa_asistencia
      print(f"El profesor {self.nombre} pasa asistencia")    # Imprime el metodo pasa_asistencia

# Crear objeto profesor
profesor1 = Profesor(111, "Profesor 1")             # Crea el objeto profesor1
profesor1.materias.append("Materia 1")              # Agrega la materia 1 a la lista materias del objeto profesor1
profesor1.materias.append("Materia 2")              # Agrega la materia 2 a la lista materias del objeto profesor1
profesor1.califica()                                # Llama al metodo califica del objeto profesor1
profesor1.pasa_asistencia()                         # Llama al metodo pasa_asistencia del objeto profesor1

#En la parte de "califica" y "pasa_asistencia" (Linea 14 y 17) puse el comando self para definir los atributos.
#Cambié fprint por print 
# El nombre de la clase debe comenzar con mayúscula.
# Al comando Int le fatlaba un "_"
# corregi la variante de califica para que si imprimiera la materia pq estaba con mayusculas
# Corregi las comillas de la parte de arriba