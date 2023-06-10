from nodo import Nodo
import xml.etree.ElementTree as ET
from animal import Animal



class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def add(self, dato):
        nuevo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            
            while actual.siguiente is not None:
                actual = actual.siguiente
                
            actual.siguiente = nuevo
            
    def Imprimir(self):
        actual = self.cabeza
        #print(actual.dato)
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()
            #print(actual.dato)
            
    
    def modify(self, dato_nuevo, index):
        actual = self.cabeza
        indice = 0

        while actual is not None:
            if indice == index:
                actual.dato = dato_nuevo
                return
            else:
                actual = actual.siguiente
                indice += 1
    
    def Cargar(self, operacion):
        tree = ET.parse('Lista Enlazada\\animales.xml')
        root = tree.getroot()
        
        for indice, persona in enumerate(root.findall('persona')):
            codigo = persona.find('codigo').text
            nombre = persona.find('nombre').text
            edad = persona.find('edad').text
            encargado = persona.find('encargado').text
            raza = persona.find('raza').text
            
            objeto = Animal(codigo, nombre, edad, encargado, raza)
            
            
            if operacion == 1: #Agregar datos a la lista
                
                self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)
            
            #print(f"codigo: {codigo} nombre: {nombre}")
            
    def editarXML(self):
        tree = ET.parse('Lista Enlazada\\animales.xml')
        root = tree.getroot()
        
        nombre1 = root.find("persona[1]/nombre")
        nombre1.text = "Fido"
        
        tree.write("animales.xml")
        self.Cargar(2)