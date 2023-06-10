import xml.etree.cElementTree as ET

tree = ET.parse("peliculas.xml")
root = tree.getroot()

#pelicula = root.find('categorias')

for categoria in root.findall('categoria'):
    nombre = categoria.find('nombre').text
    
    pelicula = categoria.find('peliculas')
    
    for peli in pelicula.findall('pelicula'):
        titulo = peli.find('titulo').text
        print(titulo)
    
    print(f"Nombre: {nombre.strip()}")