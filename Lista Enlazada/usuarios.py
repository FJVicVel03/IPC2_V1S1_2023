import xml.etree.cElementTree as ET
tree = ET.parse("usuario.xml")
root = tree.getroot()


for indice, personas in enumerate(root.findall("usuario")):
    correo = personas.find("correo").text
    print(correo)