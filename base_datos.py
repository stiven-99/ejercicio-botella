class Base_datos:
    def __init__(self):
        self.lista_botella = []

    def agregar_botella(self, nuevo_obj):
        self.lista_botella.append(nuevo_obj)
        print("botella guardada exitosamente")
    
    def eliminar_botella(self, posicion):
        for i in range(len(self.lista_botella)):
            if i == posicion:
                self.lista_botella.pop(posicion)
                print("botella en posicion {i} eliminado")
            else:
                print("posicion no encontrada")

    def modificar_botella(self, posicion, nuevo_material, nueva_capacidad, nueva_forma):
        for i in range(len(self.lista_botella)):
            if i == posicion:
                self.lista_botella[i].set_datos(nuevo_material, nueva_capacidad, nueva_forma)
                print("posicion {i} actualizacda")
            else:
                print("posicion para modificar no existe")
    