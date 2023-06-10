from nodo import Nodo
import xml.etree.cElementTree as ET
class Lista_Doble:
    def __init__(self):
        self.cabeza = None
        
        
    def add(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            
    def imprimir(self):
        actual = self.cabeza
        actual.dato.imprimir #falta la clase Usuario (es similar al de Animal de la Lista Enlazada)
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()
            
    def pelis(self):
        tree = ET.parse("peliculas.xml")
        root = tree.getroot()

        #pelicula = root.find('categorias')
        

        for categoria in root.findall('categoria'):
            nombre = categoria.find('nombre').text
            
            pelicula = categoria.find('peliculas')
            
            for peli in pelicula.findall('pelicula'):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora = peli.find('hora').text
                
                print(titulo)
            
            print(f"Nombre: {nombre.strip()}")
            
            