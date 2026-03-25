from plastico import Botella_plastica
from vidrio import Botella_vidrio
from base_datos import Base_datos

obj_base_datos = Base_datos()

material = input("material inicial: ")
capacidad = input("capacidad inicial: ")
forma = input("forma de la botella: ")

if material == "plastica":
    obj_botella = Botella_plastica(material, capacidad, forma)
else:
    obj_botella= Botella_vidrio(material, capacidad, forma)

obj_base_datos.agregar_botella(obj_botella)
print(obj_botella.ver_info()) 