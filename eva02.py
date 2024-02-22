"""
Programa:eva02.py
Nombre Completo:Emiliano Rivas Rua
Matricula:1723110398
Fecha: 29/01/2024
"""
class Libro:                                                                   # Define la clase Libro
  def __init__(self, titulo, autor, anio_publicacion, genero, prestado=False): # Define el constructor 
      self.titulo = titulo                                                     # Define el titulo
      self.autor = autor                                                       # Define el autor
      self.prestado = prestado                                                 # Define si lo tiene prestado
      self.anio_publicacion = anio_publicacion                                 # Define el año de publicación
      self.genero = genero                                                     # Define el genero

  def prestar(self):                                                           # Define el metodo prestar
      self.prestado = True                                                     # Cambia el estado a prestado
  
  def devolver(self):                                                          # Define el metodo devolver    
      self.prestado = False                                                    # Cambia el estado a disponible

  def mostrar_informacion(self):                                               # Define el metodo mostrar_informacion
      print(f"Título: {self.titulo}\n")                                        # Imprime el titulo
      print(f"Autor: {self.autor}")                                            # Imprime el autor  
      print(f"Año de publicación: {self.anio_publicacion}")                    # Imprime el año de publicación
      print(f"Género: {self.genero}")                                          # Imprime el genero
      print(f"Prestado: {'Sí' if self.prestado else 'No'}")                    # Imprime si esta prestado o no

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")   # Creamos el objeto libro1
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción", True) # Creamos el objeto libro2

libro1.prestar()                                                              # ¿Prestamos el libro1?
libro1.mostrar_informacion()                                                  # Mostramos la información del libro1
libro2.mostrar_informacion()                                                  # Mostramos la información del libro2
libro1.devolver()                                                             # ¿Devolvemos el libro1?  
libro1.mostrar_informacion()                                                  # Mostramos la información del libro1  
libro2.mostrar_informacion()                                                  # Mostramos la información del libro2

# Corregi las comillas de hasta arriba
# Las clases siempre empiezan con mayuscula
# Al int le falto un "_"
# Problemas con la indentacion
# Coloce el comando "self"
# Cambie el metodo de impresion para que imprimera bien ya que falto colocar el "self"