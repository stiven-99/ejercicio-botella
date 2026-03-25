from plastico import Botella_plastica
from vidrio import Botella_vidrio
from base_datos import Base_datos

obj_base_datos = Base_datos()

while True:
    print("----- MENU DE OPCIONES ---- ")
    print("1. guardar una nueva botella de plastica")
    print("2. guardar una nueva botella de vidrio")
    print("3. mostrar listas de botellas")
    print("4. eliminar una posicion de botella")
    print("5. salir del menu")

    opcion = input("selecciona una opcion")

    if opcion == "1":
        material = input("ingrese el material: ")
        capacidad = input("ingrese la cantidad: ")
        forma = input("ingrese la forma: ")

        obj_botella = Botella_plastica(material, capacidad, forma)
        obj_base_datos.agregar_botella(obj_botella)

    
